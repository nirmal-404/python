import time

my_time= int(input("Enter the time in seconds: "))

for i in range(my_time, 0, -1):
    seconds = i % 60
    minutes = int( i / 60) % 60
    hrs = int(i / 3600)
    print(f"{hrs:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)


print("Time's up")