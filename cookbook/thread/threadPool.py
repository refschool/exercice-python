import concurrent.futures
import time

import time
def do_something(seconds):
    print('sleeping 1 second...')
    time.sleep(seconds)
    return 'Done sleeping...'

start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_something, 1)
    f2 = executor.submit(do_something, 1.5)

finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} seconds(s)')



