import time
import threading
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
    print(f'Going to sleep for {seconds} second(s)')
    time.sleep(seconds)
    return (f'Done Sleeping {seconds}')
    
# Serial Calls , this will take 2 Secs
#do_something()
#do_something()
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = [executor.submit(do_something,sec) for sec in secs]
    for completed in concurrent.futures.as_completed(results):
        print(completed.result())
    
'''
threads = []
for _ in range(10):
    t= threading.Thread(target=do_something,args = [1.5])
    t.start()
    threads.append(t)

# Wait for Threads to Complete
for thread in threads:
    thread.join()

'''
finish = time.perf_counter()

print(f'Time {round(finish-start,2)}')