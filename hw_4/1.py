import time
from threading import Thread
from multiprocessing import Process

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
def synchronous(n, s):
    start = time.time()
    for _ in range(10):
        fib(n)
    end = time.time()
    s += f"Time synchronous: {end - start:.4f}s"
    s += '\n'
    return s

def threads(n, s):
    start = time.time()
    res = []
    for _ in range(10):
        a = Thread(target=fib, args=(n,))
        a.start()
        res.append(a)
    for i in res:
        i.join()
    end = time.time()
    s += f"Time threading: {end - start:.4f}s"
    s += '\n'
    return s

def processes(n, s):
    start = time.time()
    res = []
    for _ in range(10):
        a = Process(target=fib, args=(n, ))
        a.start()
        res.append(a)
    for i in res:
        i.join()
    end = time.time()
    s += f"Time processes: {end - start:.4f}s"
    s += '\n'
    return s


if __name__ == '__main__':
    n = 40
    s = ''
    s = synchronous(n, s)
    s = threads(n, s)
    s = processes(n, s)
    with open('/Users/nikitakocherin/workspace/python_course/hw_4/time_first.txt', 'w') as f:
        f.write(s)