# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 13:37:34 2023

@author: dimit
"""
import time, numba
#Numba vs Python comparison

#Naive Python implementation:
    
def summy(n):
    sum1 = 0
    for i in range (1, n+1):
        sum1 += 1 / i**2
    return sum1

#run 2000 times to measure time
start_time = time.perf_counter()
for i in range(2000):
    summy(10000)
end_time = time.perf_counter()
print(f'Naive python execution time: {round(end_time - start_time,2)} seconds')


start_time = time.perf_counter()
@numba.jit(nopython=True)
def numbasum():
    def go_fast(n): # Function is compiled and runs in machine code
        sum1 = 0
        for i in range (1, n+1):
            sum1 += 1 / i**2
        return sum1
    for i in range(2000):
        go_fast(10000)
numbasum()      
end_time = time.perf_counter()
print(f'Numba execution time: {round(end_time - start_time,2)} seconds')

#In the end, we get 4.72 vs 0.39 seconds, a very good result