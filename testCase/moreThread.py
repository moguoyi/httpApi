import threading

import time





def showinfo():

    print('currentthread = {}'.format(threading.current_thread()))

    print('main thread = {}'.format(threading.main_thread()))

    print('active count = {}'.format(threading.active_count()))



def worker():

    count = 0

    showinfo()

    while True:

        if count>5:

            break

        time.sleep(5)

        count += 1

        print('finsh')



t = threading.Thread(target=worker,name='work')

showinfo()

t.start()



print('end')