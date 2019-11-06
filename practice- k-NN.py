#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd 
import numpy as np
import math
import operator


# In[47]:


df= pd.read_csv('C:/Users/mridul/Desktop/Heart Disease Analysis/iris.csv')
df.head(10)


# In[60]:


test= [[7.2, 3.6, 5.1, 2.5]]
print(df.shape[0])


# In[61]:


testdata=pd.DataFrame(test)
print(testdata)
print(testdata.shape[1])
print(df)


# In[62]:


def euclidiandistance(data1, data2, length):
    dist=0
    for x in range(length):
        dist=dist+np.square(data1[x] - data2[x])
    return np.sqrt(dist)
d={}
distance={}
for y in range(df.shape[0]):
    distance[y]= euclidiandistance(df.iloc[y], testdata, testdata.shape[1])[0]
sorted_distance= sorted(distance.items(), key= operator.itemgetter(1), reverse= False)
#print(sorted_distance)
k=3
nearest_neighbour=[]
for x in range(k):
    nearest_neighbour.append(sorted_distance[x])
#print(nearest_neighbour)
classVotes={}
for x in range(len(nearest_neighbour)):
    response= df.iloc[nearest_neighbour[x][0]][-1]
    
    if response in classVotes:
        classVotes[response] += 1
    else:
        classVotes[response] = 1

sortedVotes= sorted(classVotes.items(), key= operator.itemgetter(1), reverse= True)
print(sortedVotes[0][0], nearest_neighbour)
print(distance[141])


# In[ ]:




