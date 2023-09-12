# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 12:10:59 2023

@author: dimit
"""

import scipy
import matplotlib.pyplot as plt
import numpy as np
import requests
#------------------------------------------------

url = 'https://pastebin.com/raw/ENyYffaq'
response = requests.get(url)
data = response.text.split('\n')
data = [line.split() for line in data if line.strip()]
points = [(float(x), float(y)) for x, y in data]

plist1, plist2 = zip(*points)

def polynomial_3deg(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d


plist1=np.array(plist1)
plist2=np.array(plist2)
params, covariance = scipy.optimize.curve_fit(polynomial_3deg, plist1, plist2)

a_fit, b_fit, c_fit, d_fit = params
y_fit = polynomial_3deg(plist1, *params)

plt.scatter(plist1, plist2, label='Data')
plt.plot(plist1, y_fit, label='Fitted Curve', color='red')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('3-Degree Polynomial Fit')
plt.show()

#---------------------------------------------------------------

def root_fn(x):
    return polynomial_3deg(x, *params)

rootsy=scipy.optimize.root(root_fn,[1.1,-2,2],method='hybr',tol = 10 ** (-10))

for i in range(len(rootsy.x)):
    if abs(polynomial_3deg(rootsy.x[i],*params)) < 0.01:
        print('Real root found: ',rootsy.x[i])
#There is only one real root as we can see on the graph
