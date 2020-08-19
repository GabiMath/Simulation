#!/usr/bin/env python
# coding: utf-8

# # 1. 

# In[3]:


from IPython.display import Image
Image(filename='juramento.png')


# In[9]:


def lucas(n):
    if(n == 0):
        return 1
    if(n == 1):
        return 3
    else:
        return lucas(n-1)+lucas(n-2)


# In[22]:


import matplotlib.pyplot as plt
print('Lucas Numbers\n')
x=int(input('Write the number of Lucas Numbers list '))
l=[]
for i in range(x):
    l.append(lucas(i))
    print(i, ': ', lucas(i))
plt.plot([i for i in range(x)],l)

