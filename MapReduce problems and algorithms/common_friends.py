# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 21:16:55 2023

@author: dimit
"""

import numpy as np
import functools
from collections import Counter
#Common Friends MapReduce

fdic = {}

#preprocessing and adding to the dictionary

file = 'data/friends.txt'
with open(file) as f:
    for line in f:
        spl = line.strip().split(':')
        spl[0] = int(spl[0].strip())
        for i in spl[1].split(','):
            
            if spl[0] not in fdic:
                fdic[spl[0]] = [int(i.strip())]
            else:
                fdic[spl[0]].append(int(i.strip()))
n = max(fdic)

mat = [[0 for _ in range(n)] for _ in range(n)]
for i in fdic:
    for j in fdic[i]:
        mat[i-1][j-1] = 1
        
mat2 = [[0 for _ in range(n)] for _ in range(n)]
comms_dic = {}
for i in range(n):
    for j in range(i+1,n):
        comms_dic[tuple(sorted((i,j)))] = []
        

for i in range(n):
    for j in range(n):
        if i !=j:
            if mat[i][j] == 1:
                for p in comms_dic:
                    if i in p:
                        comms_dic[p].append(j)
#mapped and merged all the friends per pair

#reduce
print(comms_dic)

def reducer(key1, key2):
    print('redukujem',key1,key2)
    if key1 !=None:
        values1 = comms_dic[key1]
        values2 = comms_dic[key2]
        
        # Use Counter to count occurrences for both sets of values
        count1 = Counter(values1)
        count2 = Counter(values2)
        filtered_values1 = [item for item in values1 if count1[item] > 1]
        filtered_values2 = [item for item in values2 if count2[item] > 1]
        reduced_filtered_values1 = []
        reduced_filtered_values2 = []
        
        for item in filtered_values1:
            if item not in reduced_filtered_values1:
                reduced_filtered_values1.append(item)
        
        for item in filtered_values2:
            if item not in reduced_filtered_values2:
                reduced_filtered_values2.append(item)
        comms_dic[key1] = reduced_filtered_values1
        comms_dic[key2] = reduced_filtered_values2
    else:
        values2 = comms_dic[key2]
        
        # Use Counter to count occurrences for both sets of values
        count2 = Counter(values2)
        filtered_values2 = [item for item in values2 if count2[item] > 1]
        reduced_filtered_values2 = []
        
        for item in filtered_values2:
            if item not in reduced_filtered_values2:
                reduced_filtered_values2.append(item)
        comms_dic[key2] = reduced_filtered_values2

functools.reduce(reducer,comms_dic)
        
print('Note that numeration begins from 0 in the output!\n',comms_dic)        



