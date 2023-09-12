# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 18:07:08 2023

@author: dimit
"""

import functools
import random

#Generate a large list with these words, I couldn't find any ready-to-use
PsudoRandomWords = ["Apple", "Banana", "Tree", "Pickle", "Toothpick", "Coffee", "Done"]
wordlist = []

index = 0

for x in range(1500):
    
   index = random.randint(0,6)
   wordlist.append(PsudoRandomWords[index])


def count(lis):
    dic = {}
    for i in lis:
        if i in dic:
            dic[i] +=1
        else:
            dic[i] = 1
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
    return functools.reduce(reducer, word_count(lis))

print(mapreduce_wordcount(wordlist))
   
