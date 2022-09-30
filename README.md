# Hust_Timetable_toICS

Script lấy thời khoá biểu từ https://dt-ctt.hust.edu.vn/Students/Timetables.aspx và chuyển thành file .ics có thể import vào Google Calendar, Outlook,..

Hướng dẫn sử dụng:

1. Cài đặt Chrome [Webdriver](https://chromedriver.chromium.org/downloads) hoặc dùng chocolatey thì gõ 

```console
choco install chromedriver
```

2. Cài đặt [Python](https://www.python.org/downloads/) hoặc [Pycharm](https://www.jetbrains.com/help/pycharm/installation-guide.html). Giờ mà máy còn chưa có sẵn python thì chịu đấy.
3. Clone repo này về rồi chạy file main.py, hoặc nếu không biết gì thì làm theo bước 4.
4. Ấn vào cái nút Code màu xanh lá, chọn Download ZIP. Giải nén tệp tin vừa chọn ra 1 folder bất kỳ.
5. Mở folder vừa giải nén ra, ấn vào đường dẫn thư mục và gõ "cmd" lên đó rồi ấn Enter
![Cmd](https://husteduvn-my.sharepoint.com/:i:/g/personal/tuan_nm214940_sis_hust_edu_vn/EV81GnZIgQ5LpPdsW3dWsIUB_3v-IXJhVI0oYAt6UyhLzg?e=cvTktD "Cmd")
6. Gõ 
```console
python main.py
```
7. Đợi tí cho nó tải các packages cần thiết về rồi nhập các thông tin được yêu cầu.