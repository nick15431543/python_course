import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from threading import Lock
import time
import multiprocessing

class MyLock:
    def __init__(self):
        self._lock = Lock()

    def __getstate__(self):
        return {}

    def __setstate__(self, state):
        self.__init__()

    def acquire(self):
        return self._lock.acquire()

    def release(self):
        return self._lock.release()

class SharedCounter:
    def __init__(self, value):
        self._value = value
        self._lock = Lock()

    def increment(self, delta=1):
        with self._lock:
            self._value += delta

    def get(self):
        return self._value
    
class SharedFile:
    def __init__(self, file):
        self._file = file
        with open(self._file, 'w') as f:
            f.write('')
        self._lock = MyLock()

    def write(self, str):
        self._lock.acquire()
        with open(self._file, 'a') as f:
            f.write(str)
        self._lock.release()

    def get(self):
        return self._file
    
def one_part(start, finish, step, f, a, file):
    s = time.time()
    file.write(f"Pool with start = {start} started\n")
    acc = 0
    for i in range(start, finish):
        acc += f(a + i * step) * step
    e = time.time()
    file.write(f"Pool with start = {start} ended in {e - s:.4f}s\n")
    return acc

def integrate(f, a, b, exec, n_jobs=1, n_iter=10000000):
    acc = SharedCounter(0)
    step = (b - a) / n_iter
    executor = exec(max_workers=n_jobs)
    fut = []
    length = n_iter // n_jobs
    remainder = n_iter % n_jobs
    file = SharedFile('/Users/nikitakocherin/workspace/python_course/hw_4/log.txt')
    for i in range(n_jobs):
        if i == 0:
            fut.append(executor.submit(
                one_part, 0, length + remainder, step, f, a, file))
        else:
            fut.append(executor.submit(one_part, 
                length * i + remainder, length * (i + 1) + remainder, step, f, a, file))
    for i in fut:
        acc.increment(i.result())
    return acc

if __name__ == '__main__':
    with open("/Users/nikitakocherin/workspace/python_course/hw_4/time_comp_2_task.txt", 'w') as f:
            f.write('')
    for i in range(1, multiprocessing.cpu_count() * 2):
        start = time.time()
        res = integrate(math.cos, 0, math.pi / 2, ThreadPoolExecutor, n_jobs=i)._value
        end = time.time()
        with open("/Users/nikitakocherin/workspace/python_course/hw_4/time_comp_2_task.txt", 'a') as f:
            f.write(f"{i} Threads, res = {res}, time = {end - start:.4f}s\n")
    for i in range(1, multiprocessing.cpu_count() * 2):
        start = time.time()
        res = integrate(math.cos, 0, math.pi / 2, ProcessPoolExecutor, n_jobs=i)._value
        end = time.time()
        with open("/Users/nikitakocherin/workspace/python_course/hw_4/time_comp_2_task.txt", 'a') as f:
            f.write(f"{i} Processes, res = {res}, time = {end - start:.4f}s\n")