from selenium.webdriver.common.by import By
from ics import Calendar, Event
import datetime
import login

def get_timetable(driver, username, password):

    driver.get('https://dt-ctt.hust.edu.vn/Students/Timetables.aspx')
    login.login_ctt(driver, username, password)
    W_rows  = driver.find_elements(By.XPATH, r"//tr[starts-with(@id, 'ctl00_ctl00_contentPane_MainPanel_MainContent_gvStudentRegister_DXDataRow')]")
    data = []
    for row in W_rows:
        processed = __format_row(row)
        if processed != None:
            data.append(processed)
    return data

def __get_time(time):
    # '9h32' --> datetime.time(9, 32)
    h, m = time.split('h')
    return datetime.time(hour = int(h), minute=int(m))

def __format_row(row):

    # [thoi gian, tuan hoc, phong hoc, ma lop, loai lop, nhom, ma HP, ten hoc phan, ....]
    cells = row.find_elements(By.CSS_SELECTOR, '*')
    r_row = []
    prev_cell = ''
    for cell in cells:
        if cell.text == prev_cell:
            continue
        r_row.append(cell.text)
        prev_cell = cell.text

    # Skip current row if the class is not scheduled
    if r_row[0] == ' ':
        return

    # ['Thứ', 'Start time', 'End time', [Tuần học (chia rõ các tuần)], 'Phòng học', 'Mã lớp', 'Loại lớp', 'Mã học phần', 'Tên học phần' , [Các thông tin khác]]
    # 'Thứ 2,6h45 - 9h10' --> | 2 | 06:45:00 | 09:10:00 |
    days = ('dumb', 'dumb', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
    day, time = r_row[0].split(',')
    day = int(day.replace('Thứ ', ''))
    start, end  = time.split(' - ')
    start = __get_time(start)
    end = __get_time(end)

    # '27-35,37-42,44' --> [27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44]
    weeks = __get_weeks(r_row[1])

    room = r_row[2]
    class_code = r_row[3]
    class_type = r_row[4]
    course_code = r_row[6]
    course_name = r_row[7]

    row_data = [days[day], start, end, weeks, room, class_code, class_type, course_code, course_name, r_row[8:]]
    return row_data

def __get_weeks(w):
    rw = w.split(',')
    ws = []
    for a in rw:
        if (a.find('-') != -1):
            s, e = a.split('-')
            ws.extend(range(int(s), int(e)+1))
        else:
            ws.append(int(a))
    return ws

def to_ics(first_day, data, file_path = 'time_table.ics'):
    # [{0}'Thứ', {1}'Start time', {2}'End time', {3}[Tuần học (chia rõ các tuần)], {4}'Phòng học', {5}'Mã lớp', {6}'Loại lớp', {7}'Mã học phần', {8}'Tên học phần' , {9}[Các thông tin khác]]
    c = Calendar()
    days = ('dumb', 'dumb', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
    for row in data:
        room = row[4]
        class_code = row[5]
        class_type = row[6]
        course_code = row[7]
        course_name = row[8]
        detail = f"Mã học phần: {course_code}\nMã lớp: {class_code}\n" + '\n'.join(row[9])
        for w in row[3]:
            s_delta = datetime.timedelta(weeks=w - 1, days = (days.index(row[0]) - 2), hours = row[1].hour, minutes = row[1].minute)
            e_delta = datetime.timedelta(weeks=w - 1, days = (days.index(row[0]) - 2), hours = row[2].hour, minutes = row[2].minute)
            start = first_day + s_delta
            end = first_day + e_delta
            event = Event(name=class_type + ' - ' + course_name, begin=start, end = end, location=room, description=detail)
            c.events.add(event)

    open(file_path, 'w', encoding='UTF-8').writelines(c)

def main():
    print('¯\_(ツ)_/¯')
    

if __name__ == '__main__':
    main()