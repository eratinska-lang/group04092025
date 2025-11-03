import threading
import time


def worker(num):
    print(555)
    print (f'Worker {num}')
    return (f'Worker {num}')

# threaders = []
# for i in range(5):
#     t = threading.Thread(target=worker, args=(i,))
#     t.start()
#
# for t in threaders:
#     t.join()

numbers = 0

def do_job(num, second_arg=None):
    print(555)
    for i in range(50):
        print(f'From child tread1 {num}: {i=}, {second_arg=}')
        time.sleep(1)

def do_job2(num, second_arg=None):
    print(555)
    for i in range(50):
        print(f'From child tread2 {num}: {i=}, {second_arg=}')
        time.sleep(1)


thread1 = threading.Thread(target=do_job, args=(2,))
thread2 = threading.Thread(target=do_job2, args=(50,))
thread1.start()
thread2.start()

for i in range(100):
    print(f'From main tread: {i=}')
    time.sleep(0.3)