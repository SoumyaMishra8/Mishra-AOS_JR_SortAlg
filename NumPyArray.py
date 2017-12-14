# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 13:45:57 2017

@author: mishr
"""

import math
import itertools 
import random
import datetime
import numpy as np 
class Statsort:
    #program to compare python embedded sort and new sort being created
    #main - creating integer normal distribution list of varying lengths, print out times 
    def main():
        upperlimit=100
        intbucketf=[]
        for i in range (upperlimit):
            intbucketf.append((int)(random.uniform(0,upperlimit)))
        print(intbucketf)
      #  intBucketf=np.array(intbucketf)
        for x in range (1):
            Statsort.sorterBucket(intbucketf,upperlimit)
    def sorterBucket(intBucket,upperlimit):
        sort_start_time=datetime.datetime.now()
        buckets=(int)(round(upperlimit/1000))+1#reating the number of buckets by dividing list length (elements) by 1000 - elements in each bucket 
        #intbucket1=np.empty([1000, buckets], dtype=int) #creating a 2D list in which number of rows is buckets and columns is 1000
        intbucket1=[[0 for x in range(1000)] for y in range(buckets)]
        numpy_start=datetime.datetime.now()
        intBucketF=np.array(intBucket)
        numpy_end=datetime.datetime.now()
        stat_start=datetime.datetime.now()
        Max=np.amax(intBucketF)
        Min=np.amin(intBucketF)
        Range=np.ptp(intBucketF)
        Mean=np.mean(intBucketF)
        stat_end=datetime.datetime.now()
        lowerRange=Mean-Min #half of the range of the data set - used to create buckets for each range
        upperRange=Max-Mean
        lowerGroups=round(lowerRange/Range) #number of buckets for lowerRange 
        lowerGroups=max(1,lowerGroups) #if the number of elements 1000 or less than 1000, number of groups will be 1 instead of 0
        upperGroups=buckets-lowerGroups #number of buckets for upperRange
        print(upperGroups)
        bucketing_start=datetime.datetime.now()
        bucketSelectLower=lowerGroups/lowerRange
        bucketSelectUpper=upperGroups/upperRange
        for x in range(upperlimit):
            value=intBucketF[x] #calling value at index of list 
            if Mean<value: #determining which range it will fall into 
                bucketSelect=(int)(math.ceil(bucketSelectLower*(value-Min))) #seeing where in the lowerRange does this element lie in - distance from mean 
            else:
                bucketSelect=lowerGroups+(int)(math.ceil(bucketSelectUpper*(value-Mean))) #seeing where in the upperRange does element lie - distance between mean and max
            bucketSelect=(int)(((value-Min)/Range)*upperlimit/1000) #reinstantiating bucketSelect
        bucketing_end=datetime.datetime.now()
        for y in range(buckets):
            intbucket1.sort(intbucket1[y])
        print(np.matrix(intbucket1))
        sort_end_time=datetime.datetime.now()
        print("The time for NUMPY ARRAY was")
        print(numpy_end-numpy_start)
        print("The time for STATS was")
        print(stat_end-stat_start)
        print("The time for BUCKETING was ")
        print(bucketing_end-bucketing_start)
        print("THE TOTAL TIME FOR THIS SORT WAS ")
        print(sort_end_time-sort_start_time)
        print("--------------------------------------------------------------")
        
