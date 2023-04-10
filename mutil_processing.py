# from multiprocessing import Process

# import os

# def run_proc(name):
#     print("run child process %s (%s)..." % (name, os.getpid()))
# if __name__ == "__main__":
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('text',))
#     print('Child process will start.')
#     p.start()
#     p.join()
# print('Child process end')


from multiprocessing import Pool

def test(i):
    print(i)

if __name__ == "__main__":
    lists = range(100)
    pool = Pool(8)
    pool.map(test,lists)
    pool.close()
    pool.join()
