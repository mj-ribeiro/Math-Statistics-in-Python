# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 19:06:22 2020
@author: Marcos J Ribeiro
"""

import time as tm
import concurrent.futures as cf


def do_something(sec):
    print(f'sleep {sec} second(s) ...')
    tm.sleep(sec)
    return f'Done sleeping...{sec}!'


if __name__ == '__main__':
    with cf.ProcessPoolExecutor() as executor:
        start = tm.perf_counter()    
        sec = [5, 4, 3, 2, 1]
        res = executor.map(do_something, sec)
#        for result in res:
#            print(result)        
        finish = tm.perf_counter()
    print(f'Finished in {round(finish - start, 2)} seconds')
  


# def main():
#     processes = []
#     for _ in range(10):
#         p = mp.Process(target = do_something)
#         p.start()
#         processes.append(p)
#     for processes in processes:
#         processes.join()


# if __name__ == '__main__':
#     start = tm.perf_counter()    
#     main()  
#     finish = tm.perf_counter()
#     print(f'Finished in {round(finish - start, 2)} seconds')


