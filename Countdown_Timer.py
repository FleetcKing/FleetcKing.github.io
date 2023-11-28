#choose how long the timer should be 
input_time = input('''stopwatch or timer. ("s" for stopwatch and "t" for timer): ''')
input_time == input_time.lower
while input_time != "s" and input_time != "t":
    print(f"{input_time} is invalid")
    input_time = input('''stopwatch or timer. ("s" for stopwatch and "t" for timer): ''')

def timer():
    count = int(input("how long do you want the timer to be?: "))
    import time
    for numb in range(0,count):
        print(numb)
        time.sleep(1)
    print(f"It has been {numb} seconds.")

def stopwatch():
    import time
    count = input('''type "start" to start the timer and "stop" to stop the timer: ''')
    count == count.lower()
    timer = int()
    while count == "start":
        for numb in range(0,1000000):
            print(numb)
            time.sleep(1)
stopwatch()
