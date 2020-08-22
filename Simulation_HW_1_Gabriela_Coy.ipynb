import numpy as np
import matplotlib.pyplot as plt
import time # Information about time of execution -->https://stackoverflow.com/questions/7370801/how-to-measure-elapsed-time-in-python
from datetime import timedelta

#Recursive formula option
#This code is very slow! It just can to compute the first  45  Lucas Numbers in an hour!

def lucas(n):
    if(n == 0): #Initial condition
        return 1
    if(n == 1): #Initial condition
        return 3
    else:
        return lucas(n-1)+lucas(n-2) #Recursive formula
        
print('Lucas Numbers')
x=int(input('Write the value of n: ')) 

l=[]

start = time.time()
for i in range(x):
    l.append(lucas(i))
    print(i+1, ': ', lucas(i))
end = time.time()
print('Tiempo de ejecución: ',timedelta(seconds=end-start))

plt.plot([i for i in range(x)],l)

# For loop option
#This code computes a very large amount of Lucas numbers quickly, but for large  𝑛 , the plot present some problems, because  𝐿𝑛  is too large.

n = int(input('Write the value of n: '))
l1=1 #Initial condition
l2=3 #Initial condition
lucas=[l1, l2]

print('1: ',l1)
print('2: ', l2)

start1 = time.time()
for i in range(n-2):
    l_n = l2 + l1
    l1 = l2 
    l2 = l_n
    lucas.append(l_n)
    print(i+3, ':', l_n)
end1 = time.time()

print('Tiempo de ejecución: ',timedelta(seconds=end1-start1))
plt.plot([i for i in range(n)], lucas)

#Analog of Binet's Fibonacci number formula for Lucas numbers

n = int(input('Write the value of n: '))

def binetsanalog(n):
    return int(round(((1+np.sqrt(5))/2)**n+((1-np.sqrt(5))/2)**n))

start = time.time()
for i in range(n):
    print(i+1, ':', binetsanalog(i+1))
end1 = time.time()

print('Tiempo de ejecución: ',timedelta(seconds=end1-start))
plt.plot([i for i in range(n)], [binetsanalog(i) for i in range(n)])

#The diference in these algorithms is the number of iterations. So, since the recursive algorithm need to do more iterations is more slowly.
