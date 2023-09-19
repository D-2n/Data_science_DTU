# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:43:03 2023

@author: dimit
"""

import time
st = time.time()
# Here it's basically the same as common_friends, so I re-did the code to fit the
# MapReduce standards more
 
# The algorithm is slow with the goal of displaying all the steps of a MapReduce shown in class
dic = {}
file = 'data/roadnet.txt'
# Adding edges to a dictionary 
#-------------------------------------------------
with open(file) as f:
    for line in f:
        spl = line.strip().split(' ')
        if spl[0] not in dic:
            dic[spl[0]] = []
            dic[spl[0]].append(spl[1])
        else:
            dic[spl[0]].append(spl[1])
        if spl[1] not in dic:
            dic[spl[1]] = []
            dic[spl[1]].append(spl[0])
        else:
            dic[spl[1]].append(spl[0])  
print("Mapping") 
# Mapping
#-------------------------------------------------
def mapper(key):
    pair_dic = {}
    for i in dic[key]:
        newk = tuple(sorted((key, i)))
        pair_dic[newk] = []
        for j in dic[key]:
            if j not in newk:
                pair_dic[newk].append(j)
    return pair_dic

res = list(map(mapper,dic))
print("Grouping")
# Grouping by key
#-------------------------------------------------   
main = res[0]
for i in res[1:]:
    for j in i:
        if j in main:
            main[j]+= i[j]
        else:
            main[j] = i[j]
        #main[j] = clean(j,main[j])
# Reducing
#-------------------------------------------------





print("Reducing")
tria_counter = set()

for i in main.keys():
    seen_values = set()
    
    for j in main[i]:
        if j not in seen_values:
            seen_values.add(j)
        else:
            tup = tuple(sorted((i[0], i[1], j)))
            tria_counter.add(tup)

# If you need the result as a list, you can convert the set to a list


print('Number of triangles is: ',len(tria_counter))
et = time.time()
print('Time taken: ', et - st)  
        