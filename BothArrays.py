import math
import random
import numpy as np 
class Statsort1:
   def main():
        upperlimit=100
        intbucketf=[]
        for i in range (upperlimit):
            intbucketf.append((int)(random.uniform(0,upperlimit)))
        print(intbucketf) #obtaining initial array to check accuracy of program
        for x in range (1):
            Statsort1.stats(intbucketf,upperlimit)
   def stats(intBucket,upperlimit):
        intBucketF=np.array(intBucket) #implement numpy array to take away for loop
        Max=np.amax(intBucketF)
        Min=np.amin(intBucketF)
        Range=np.ptp(intBucketF)
        Mean=np.mean(intBucketF)
        lowerRange=Mean-Min 
        upperRange=Max-Mean
        buckets=(int)(round(upperlimit/1000))+1 #bucket creation
        lowerGroups=round(lowerRange/Range) 
        lowerGroups=max(1,lowerGroups) 
        upperGroups=buckets-lowerGroups 
        intbucket1 = [([]*buckets) for row in range(1000)] #one of the many ways that failed - trying to create an appropriate 2D list
        print(intbucket1) #printing out this list to see how it is formatted (not how i wanted)
        bucketSelectLower=lowerGroups/lowerRange #tried to see if reducing complexity of function in for loop will reduce time
        bucketSelectUpper=upperGroups/upperRange
        y=0
        for x in range(upperlimit):
            value=intBucketF[x] 
            if Mean<value: 
                bucketSelect=(int)(math.ceil(bucketSelectLower*(value-Min)))#simpler function than before - reduces some time (milliseconds)
                intbucket1[bucketSelect][y]=value #storing value in 2d list - not sure if this is right 
                y=y+1 #incrementing index each time so that no index is repeated
                
            else:
                bucketSelect=lowerGroups+(int)(math.ceil(bucketSelectUpper*(value-Mean))) 
                intbucket1[bucketSelect][y]=value
                y=y+1
                
            bucketSelect=(int)(((value-Min)/Range)*upperlimit/1000) 
        for y in range(buckets):
            intbucket1.sort() #tried multiple sorts here - other sorts took TOO MUCH TIME - not even able to collect stats without computer shutting down
        print(intbucket1) #printing to see if it worked (it doesn't)
      
