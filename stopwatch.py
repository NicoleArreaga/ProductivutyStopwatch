#Julia & Nicole's stopwatch timer
import time
def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print ("Time lapsed = {0} : {1} : {2} ". format(int(hours), int(mins), sec))

input("Press Enter to start the Stopwatch")
start_time = time.time()
try:
    hours = 0
    while True:
        for minutes in range(0, 60):   #minutes to seconds
            for seconds in range(0, 60): #seconds to minutes
                time.sleep(1)
                print(hours, ":", minutes, ":", seconds+1)
except KeyboardInterrupt:
    end_time = time.time()
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
