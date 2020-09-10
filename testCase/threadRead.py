import threading

import time



def worker():
    start_time=time.time()
    print('before')

    time.sleep(3)

    print('finished')
    end_time=time.time()
    print(end_time-start_time)


def worker2():

    count = 0
    while True:
        count += 1
        print('before')
        time.sleep(3)
        if count >5:
            print('finished')
            break



t = threading.Thread(target=worker2)  #线程对象

t.start()   #启动