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

required = {'selenium', 'ics', 'webdriver_manager'}
setup(required)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


import datetime
from get_timetable import *

def main():
    os.system('cls')
    first_day = input('Nhập ngày đầu tiên của tuần 1 của năm học theo định dạng YYYY-MM-DD (Nhấn Enter nếu là năm 2021): ')
    if first_day == '':
        first_day = datetime.datetime(year=2021, month=9, day = 27, tzinfo = datetime.datetime.now().astimezone().tzinfo)
    else:
        date = datetime.date.fromisoformat(first_day)
        first_day = datetime.datetime(year = date.year, month = date.month, day = date.day, tzinfo = datetime.datetime.now().astimezone().tzinfo)
    file_path = input('Nhập đường dẫn cho file .ics hoặc nhấn enter để dùng đường dẫn mặc định (/time_table.ics): ')
    if file_path == '':
        file_path = 'time_table.ics'
    username = input('Nhập email sis: ')
    os.system('cls')
    password = input('Nhập password: ')
    os.system('cls')
    driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
    driver.maximize_window()
    time_table = get_timetable(driver, username, password)
    to_ics(first_day, time_table, file_path)

if __name__ == '__main__':
    main()