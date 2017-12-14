import java.time.LocalDateTime;
import java.util.*;
import java.lang.*;
public class BucketRange
{
   //creating normal distribution array and printing out runtimes
    public static void main(String[] args) {
        int upperLimit = 1000;
        int [] intBucket = new int[upperLimit];
        for (int i = 0; i < upperLimit; i++){
           intBucket[i] = (int)(Math.random()*100 + 1); 
        }
        sorterSimple(intBucket);
        sorterBucket(intBucket);    
    }
    //using parallelsort (similar to mergesort) and sorting array created above
    private static void sorterSimple(int [] intBucket) {
        debug_msg("Start ParallelSort " + LocalDateTime.now());
        Arrays.parallelSort(intBucket);
        debug_msg("End ParallelSort " + LocalDateTime.now());
    }
    //proposed sorting algorithm
     private static void sorterBucket(int [] intBucket) {
        debug_msg("Start Algorithm " + LocalDateTime.now());
        int upperLimit = 1000;
        int buckets = (int)Math.round(upperLimit/1000);
        int [][] intBucket1 = new int[buckets][1000];       
        int iMin = intBucket[0];
        int iMax = intBucket[0];
        int iSum = 0;
        //figuring out min, max, sum, mean, ranges of array 
        for (int i = 0; i < upperLimit; i++){
           iMin = Math.min(iMin, intBucket[i]);
           iMax = Math.max(iMax, intBucket[i]);
           iSum+=intBucket[i];      
        }
        int iMean;
        iMean = Math.round(iSum/upperLimit);
        //determining number of buckets using lower and upper ranges
        int lowerRange = iMean - iMin;
        int upperRange = iMax - iMean;
        int iRange = iMax - iMin;
        int lowerGroups = Math.round((lowerRange)/(iRange))*10;
        //if the number of elements is less than 1000, there will be only 1 group
        lowerGroups = Math.max(1, lowerGroups);
        int upperGroups = buckets - lowerGroups;
        int [] jCounter = new int [buckets];
        int bucketSelect;
        int jSelect;
        //assigning elements to respective buckets using distance from mean and lower/upper bounds
        for (int i = 0; i < upperLimit; i++){
            int iValue = intBucket[i];    
            if (iMean > iValue) {
                bucketSelect = (int)Math.ceil(lowerGroups * (iValue - iMin)/lowerRange);
            }
            else {
                bucketSelect = lowerGroups + (int)Math.ceil(upperGroups * (iValue - iMean)/upperRange);    
            }            
            bucketSelect = (int)((iValue - iMin)/iRange)*upperLimit/1000;
         /*   if (bucketSelect < 1000){ 
                jSelect = jCounter[bucketSelect];
            
                if (jSelect < 1000){
                    intBucket1[bucketSelect][jSelect]= (int)iValue;
                    jCounter[bucketSelect]+=1;
                } 
              }*/
        }
        //using parallel sort to sort buckets - will implement multithreading here later
        for (int i = 0; i < buckets; i++){
        Arrays.parallelSort(intBucket1[i]);    
        }
        debug_msg("End algorithm " + LocalDateTime.now());
    }         
    private static void debug_msg (String printMessage){
    System.out.println(printMessage);
    }
    }