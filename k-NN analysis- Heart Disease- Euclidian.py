#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import seaborn as sns
from matplotlib import rcParams
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('pylab', 'inline')
import math
import operator


# In[2]:


training_ds= pd.read_csv('C:/Users/mridul/Desktop/heart-disease-classification/heart- training.csv')
print(len(training_ds))
testing_ds= pd.read_csv('C:/Users/mridul/Desktop/heart-disease-classification/heart- testing.csv')


# In[3]:


#method to calculate euclidian distance (takes testing data, training data and total number of columns as parameters)
#length: the total number of columns in each data row
def euclidianDistance(data1, data2, length):
    d=0
    for x in range(length):
        d= d+ np.square(data1[x] - data2.iloc[x])
    return np.sqrt(d)
#method to give the response for k-NN respective to k and each iLoc of test_data
def knn(training_data, test_data, k, value):
    #k: the closest neighbours on which the analysis is being done
    distance={}
    for x in range(training_data.shape[0]):
        distance[x]= euclidianDistance(training_data.iloc[x], test_data, test_data.shape[0])[value]
    #distance is being calculated for the entire training data set but the closest k would be chosen    
    sorted_distance= sorted(distance.items(), key= operator.itemgetter(1), reverse=False)
    nearest_neighbour= []
    
    for x in range(k):
        nearest_neighbour.append(sorted_distance[x])
    classVotes={}
    for x in range(len(nearest_neighbour)):
        response= training_data.iloc[nearest_neighbour[x][0]][-1]
    
        if response in classVotes:
            classVotes[response]+= 1
        else:
            classVotes[response]= 1
        
    sortedVotes= sorted(classVotes.items(), key= operator.itemgetter(1), reverse= True)    
    print(classVotes)
    print(sortedVotes[0][0])
    


# In[6]:


k=5
for x in range (len(testing_ds)):
    knn(training_ds, pd.DataFrame(testing_ds.iloc[x]), k, x)
 


# In[ ]:





# In[ ]:




