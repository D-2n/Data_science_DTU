# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 18:56:59 2023

@author: dimit
"""

import functools
import random

#Generate a large list with these words, I couldn't find any ready-to-use
PsudoRandomWords = ["Apple", "Banana", "Tree", "Pickle", "Toothpick", "Coffee", "Done"]

document_list = [] #document number is the list index

for i in range (1,51):
    wordlist = []
    
    index = 0
    
    for x in range(20):
        
       index = random.randint(0,6)
       wordlist.append(PsudoRandomWords[index])
    document_list.append((i,wordlist))

#Function to print out the document list nicely
def print_doclist():
    for i in range(len(document_list)):
        print(f'Document {i+1}: {document_list[i]}\n')

print_doclist()

def count(lis):
    #print('lis',lis)
    dic = {}
    for i in lis:
        for j in i[1]:
            if j in dic:
                if i[0] not in dic[j]:
                    dic[j].append(i[0]) 
            else:
                dic[j] = [i[0]]
    return dic

def reducer(f,s):
    for i in s:
        if i in f:
            f[i] += s[i]
        else:
            f[i] = s[i]
    return f

def mapreduce_appearance_index(lis):
    def word_count(lis):
        n=len(lis)
        if n > 5: #split the list into 3 for better complexity
            l1 = word_count(lis[:n//3])
            l2 = word_count(lis[n//3:(2*n)//3])
            l3 = word_count(lis[(2*n)//3:])
            return l1 + l2 + l3
        else:
            return list(map(count,[lis]))
    return functools.reduce(reducer, word_count(lis))

print(mapreduce_appearance_index(document_list))

#everything works but due to the nature of data generation, if we add >=7 words to each document,
# chances are all the words will just appear in each document
