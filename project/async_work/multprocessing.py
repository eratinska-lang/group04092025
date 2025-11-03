import modulefinder
import multiprocessing

print(multiprocessing.cpu_count())

def worker(num):
    print(555)
    print(f'Worker {num}')

# processes = []

# if __name__ == '__main__':
#     for i in range(7):
#         p = multiprocessing.Process(target=worker, args=(i, ))
#         processes.append(p)
#         p.start()
#
#     for j in processes:
#         j.join()

# if __name__ == '__main__':
#     with multiprocessing.Pool(processes=4) as pool:
#         results = pool.map(worker, range(10))
#         print(results)