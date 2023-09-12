# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:46:23 2023

@author: dimit
"""
import functools
#THIS WAS TREATED LIKE WORD_FREQUENCY, AS IT IS A SIMILAR PROBLEM IN IT'S CORE
file = 'data/eulerGraphs1.txt'
edge_list = []
with open(file) as f:
    for line in f:
        spl = line.strip().split(' ')
        if (spl[0],spl[1]) not in edge_list:
            edge_list.append((spl[0],spl[1]))
    
# can be treated similar to word frequency, so change the code

def count(lis):
    dic = {}
    for i in lis:
        for j in i:
            if j in dic:
                dic[j] +=1
            else:
                dic[j] = 1
    return dic

def reducer(f,s):
    for i in s:
        if i in f:
            f[i] += s[i]
        else:
            f[i] = s[i]
    return f

def mapreduce_wordcount(lis):
    def word_count(lis):
        n=len(lis)
        if n > 20: #split the list into 3 for better complexity
            l1 = word_count(lis[:n//3])
            l2 = word_count(lis[n//3:(2*n)//3])
            l3 = word_count(lis[(2*n)//3:])
            return l1 + l2 + l3
        else:
            return list(map(count,[lis]))
    res = functools.reduce(reducer, word_count(lis))
    odd = 0
    even = 0
    for i in res.keys():
        if res[i]%2 == 0:
            even +=1
        else:
            odd +=1
    if odd == 0:
        print("Euler circuit exists")
    else:
        print("No Euler circuit")
    if odd > 2:
        print('No Euler path')
    else:
        print('Euler path exists')
    return (even, odd)
print(mapreduce_wordcount(edge_list))