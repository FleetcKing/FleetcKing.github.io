input_time = (input("set your time using seconds(25) or by min (2:57): "))
while len(input_time) > 4 or len(input_time) < 1:
    print(f"{input_time} is invalid. try typing in seconds (56) or min (3:47)")
    input_time = (input("set your time: "))

sec_or_min = input_time.find(":")

if sec_or_min != -1:
    min = input_time[:sec_or_min]
    sec = input_time[1+ sec_or_min:]

else: 
    sec = int(input_time)
    min = 0

print(min,":",sec)

sec = int(sec)
min = int(min)
timer = min * 60 + sec + 1
import time 

for i in reversed(range(timer)):
    print(i)
    time.sleep(1)
