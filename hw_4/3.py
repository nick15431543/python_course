from multiprocessing import Process, Queue
import time
import codecs


def a(qma, qab):
    while True:
        s = qma.get()
        s = s.lower()
        qab.put(s)
        time.sleep(5)




def b(qab, qbm, start):
    while True:
        s = qab.get()
        s = codecs.encode(s, 'rot_13')
        print(f"output at {time.time() - start:.4f}s")
        print(f"output {s}")
        qbm.put(s)

if __name__ == '__main__':
    qma = Queue(maxsize=20)
    qab = Queue(maxsize=20)
    qbm = Queue(maxsize=20)
    start = time.time()
    a_proc = Process(target = a, args=(qma, qab, ))
    b_proc = Process(target = b, args=(qab, qbm, start, ))
    a_proc.start()
    b_proc.start()
    while True:
        s = str(input())
        print(f"input at {time.time() - start:.4f}s")
        qma.put(s)


