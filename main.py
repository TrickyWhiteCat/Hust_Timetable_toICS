import os
import sys
import subprocess
import pkg_resources

def setup(required):
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing   = required - installed

    if missing:
        # implement pip as a subprocess:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing])

required = {'selenium', 'ics'}
setup(required)

from selenium import webdriver
from selenium.webdriver.edge.options import Options
import datetime
from get_timetable import *

def main():
    first_day = input('Nhập ngày đầu tiên của học kỳ theo định dạng YYYY-MM-DD (Nhập "Y" nếu là năm 2021): ')
    if first_day == 'Y':
        first_day = datetime.datetime(year=2021, month=9, day = 20, tzinfo= datetime.datetime.now().astimezone().tzinfo)
    else:
        first_day = datetime.date.fromisoformat(first_day)

    username = input('Nhập email sis: ')
    os.system('cls')
    password = input('Nhập password: ')
    opt = Options()
    opt.add_argument('Inprivate')
    driver = webdriver.Edge(options = opt)
    driver.maximize_window()
    time_table = get_timetable(driver, username, password)
    to_ics(first_day, time_table)

if __name__ == '__main__':
    main()