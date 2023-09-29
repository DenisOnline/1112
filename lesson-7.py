# import datetime
#
# date_time = datetime.datetime(2021,
#                               9,
#                               16,
#                               hour=11,
#                               minute=26,
#                               second=46,
#                               microsecond=789)
# date_1 = datetime.date(2022, 4, 21)
# time_1 = datetime.time(21, 4, 21)
# date_time_2 = datetime.datetime.combine(date_1, time_1)
# print(f"object - {type(date_time)}")
# print(f"datetime - {date_time.replace(1790)}")
# print(f"date - {date_time.date()}")
# print(f"date_1 - {date_1}")
# print(f"time - {date_time.time()}")
# print(f"time_1 - {time_1}")
# print(f"date_time_2 - {date_time_2}")
#
# date_now = datetime.datetime.now()
# date_today = datetime.datetime.today()
# date_data = datetime.date.today()
# print(f"date_now - {date_now}")
# print(f"date_today - {date_today}")
# print(f"date_data - {date_data}")
# print(f"weekday - {date_now.weekday()}")
# print(f"isoweekday - {date_now.isoweekday()}")
# data_str = "30/04/2008 22:22"
# print(f"strftime - {date_now.strftime('%d.%m.%Y - %H:%M')}")
# print(f"strptime = {date_now.strptime(data_str, '%d/%m/%Y %H:%M')}")

import os, datetime


def collector(path, res_path):
    res_path = os.path.normpath(res_path)
    path = os.path.normpath(path)
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            file_time = os.path.getmtime(f"{dirpath}\\{file}")
            datetime_file = datetime.datetime.fromtimestamp(file_time)
            file_date = datetime_file.strftime("%d.%m.%Y")
            if os.path.isdir(f"{res_path}\\{file_date}"):
                os.replace(f"{dirpath}\\{file}", f"{res_path}\\{file_date}\\{file}")
            else:
                os.mkdir(f"{res_path}\\{file_date}\\")
                os.replace(f"{dirpath}\\{file}", f"{res_path}\\{file_date}\\{file}")


path = ""
res_path = ""
collector(path, res_path)
