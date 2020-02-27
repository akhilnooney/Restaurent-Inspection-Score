#!/usr/bin/env python
# coding: utf-8

# In[15]:


#Question 1.1
#Complete the function one resampled mean below. It should take in an original table data, with a column Score,
#and return the mean score of one resampling from data.
import datascience as ds
from datascience import Table
import numpy as np
restaurents=Table.read_table('restaurant_inspection_scores.csv').drop('Address','Facility ID')#To read File
restaurant_sample=restaurents.sample(100, with_replacement=False)#It would take samples of 100
def one_resampled_mean(data): #Function Defintion
    resampled_data=data.select('Score').sample().column(0)
    return np.mean(resampled_data) #Finding Average of sampled data
this_mean=one_resampled_mean(restaurant_sample)#Function call
this_mean


# In[16]:


#Question 1.2
#Complete the function bootstrap scores below. It should take no arguments. It should simulate drawing 5000
#resamples from restaurant sample and compute the mean restaurant score in each resample. It should return an
#array of those 5000 resample means.
import datascience as ds
from datascience import Table
import numpy as np
import time
restaurents=Table.read_table('restaurant_inspection_scores.csv').drop('Address','Facility ID')#Read CSV file
restaurant_sample=restaurents.sample(100, with_replacement=False)#Take samples of 100
def bootstrap_scores(): #Function Defintion
    resampled_means = ds.util.make_array()#Create a Array
    for i in range(5000): #To get 5000 sampled means
        resampled_mean = one_resampled_mean(restaurant_sample)#Function Call
        resampled_means = np.append(resampled_means, resampled_mean)#Store all sampled means in this variable
    return resampled_means
resampled_means = bootstrap_scores() #Function Call
resampled_means


# In[17]:


#Question 1.3
#Compute a 95 percent confidence interval for the average restaurant score using the array resampled means.
import datascience as ds
from datascience import Table
import numpy as np
restaurents=Table.read_table('restaurant_inspection_scores.csv').drop('Address','Facility ID')#To read CSV file
restaurant_sample=restaurents.sample(100, with_replacement=False)#Take samples of 100
def bootstrap_scores():#Function Defintion
    resampled_means = ds.util.make_array()#Create an Array
    for i in range(5000):##To get 5000 sampled means
        resampled_mean = one_resampled_mean(restaurant_sample)#Function Call
        resampled_means = np.append(resampled_means, resampled_mean)#Store all sampled means in this variabl
    return resampled_means
resampled_means = bootstrap_scores()#Function call
resampled_means
lower_bound = np.percentile(resampled_means,2.5)#Take 2.5 percentile of normal Distribution
upper_bound = np.percentile(resampled_means,97.5)#Take 97.5 percentile of normal Distribution
print("95% confidence interval for the average restaurant score, computed by bootstrapping:\n(",lower_bound,',',upper_bound,")")


# In[18]:


#Question1.4
#What distribution is the histogram between question 2 and 3 displaying (that is, what data are plotted), and why
#does it have that shape?

get_ipython().run_line_magic('matplotlib', 'inline')
Table().with_column('Resampled Means', resampled_means).hist()

#Ans:

#From the Histogram which we see below we can state that sample means are in normal distribution shape.This is becuase of
#Central Limit Theorem.Theorem states that sampling distribution of the mean of any independent, random variable will be normal or nearly normal, 
#if the sample size is large enough that's why it has bell curve(Normal Distibution) shape.


# In[13]:


#Question1.5
#Does the distribution of the sampled scores look normally distributed? State \yes" or \no" and describe in one
#sentence why you should expect this result.

#Ans

#No, becuase Central Limit Theorem is not applicable to the distribution of sampled scores. 
#It is only applicable to the sum or average of the sampled scores.


# In[19]:


#Question 1.6
#Without referencing the array resampled means or performing any new simulations, calculate an interval around
#the sample mean that covers approximately 95% of the numbers in the resampled means array. This con
dence
#interval should look very similar to the one you computed in Question 3.
sample_mean = np.mean(restaurant_sample.column(3))
Standard_deviation_sample = np.std(restaurant_sample.column(3))
sample_row_size = restaurant_sample.num_rows
means_standard_deviation = Standard_deviation_sample/np.sqrt(sample_row_size)
lower_bound_distribution = sample_mean-(2*means_standard_deviation)
upper_bound_distribution = sample_mean+(2*means_standard_deviation)
print(f"95% confidence interval for the average restaurant score is \n({lower_bound_distribution},{upper_bound_distribution})")


# In[20]:


#Question 2.1
#Define the function one statistic prop heads which should return exactly one simulated statistic of the proportion
#of heads from n coin flips.
coin_proportions = ds.util.make_array(.5, .5) #Fair Coin
def one_statistic_prop_heads(n):#Function Defintion
    simulated_proportions = ds.util.sample_proportions(n, coin_proportions)#Coin Proportion
    prop_heads = simulated_proportions.item(0)#Proportion of Heads
    return prop_heads
one_statistic_prop_heads(10)#Function call


# In[21]:


#Question 2.2
import datascience as ds
import numpy as np
def sample_size_n(n):#Function Defintion
    coin_proportions = ds.util.make_array(.5, .5) # Fair Coin
    heads_proportions = ds.util.make_array()#create an Array
    for i in np.arange(5000):#It will simulate for 5000 times
        prop_heads = one_statistic_prop_heads(n)
        heads_proportions = np.append(heads_proportions, prop_heads)#Sample of heads
    return heads_proportions
sample_size_n(10)#Function call


# In[22]:


#Question 2.3
#Write a function called empirical sample mean sd that takes a sample size n as its argument. The function should
#simulate 500 samples with replacement of size n from the flight delays dataset, and it should return the standard
#deviation of the means of those 500 samples.
import datascience as ds
from datascience import Table
import numpy as np
flight_delay=Table.read_table("united_summer2015.csv")#Read CSV file
def emperical_sample_mean_sd(n):#Function Defintion
    sample_means=ds.util.make_array()#It will create an array
    for i in np.arange(500):#Simulation for 500 times
        sample=flight_delay.sample(10, with_replacement=True)#Sample Size of 10
        sample_mean=np.mean(sample.column('Delay'))#Average Calculation of Sample
        sample_means=np.append(sample_means,sample_mean)#It will append all samples means in this variable
    return np.std(sample_means) #Calculate Standard Deviation and returns to function call
emperical_sample_mean_sd(10)#Function Call


# In[23]:


#Quetion 2.4
#Now, write a function called predict sample mean sd to find the predicted value of the standard deviation of means
#according to the relationship between the standard deviation of the sample mean and sample size that is discussed
#in the textbook. It takes a sample size n (a number) as its argument. It returns the predicted value of the standard
#deviation of the mean delay time for samples of size n from the flight delays.
def predict_sample_mean_sd(n):
    return np.std(flight_delay.column('Delay'))/n**0.5 #Calculate Sd of original Population
predict_sample_mean_sd(10)


# In[ ]:




