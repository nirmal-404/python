
import datetime

date = datetime.date(2025, 4, 13)
print(date)

today = datetime.date.today()
print(today)

time = datetime.time(2, 30, 0)
print(time)

now = datetime.datetime.now()
print(now)

now = now.strftime("%H:%M:%S %d-%m-%Y")
print(now)

target_datetime = datetime.datetime(2048, 9, 18, 14, 30, 38)
print(target_datetime)