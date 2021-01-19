import time
from multiprocessing import Process


def do_something():
    print('sleeping 1 second...')
    time.sleep(1)
    print('Done sleeping...')

#this is needed in windows
if __name__ == '__main__':

    start = time.perf_counter()

    p1 = Process(target=do_something)
    p2 = Process(target=do_something)


    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start,2)} seconds(s)')