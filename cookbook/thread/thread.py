#https://www.youtube.com/watch?v=IEEhzQoKtQU

"""I/O bound operation go for threading (illusion of //)
    CPU bound go multiprocessing real //"""

import threading
import time
def do_something():
    print('sleeping 1 second...')
    time.sleep(1)
    print('Done sleeping...')

start = time.perf_counter()

#création des threads
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

#démarrage des threads
t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} seconds(s)')