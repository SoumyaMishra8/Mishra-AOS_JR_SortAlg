import java.util.Random;
import java.time.LocalDateTime;
public class Bucket_Sort 
{
    static int[] sort(int[] sequence, int maxValue) 
    {
        // Bucket Sort
        int[] Bucket = new int[maxValue + 1];
        int[] sorted_sequence = new int[sequence.length];
        for (int i = 0; i < sequence.length; i++)
            Bucket[sequence[i]]++;
        int outPos = 0;
        for (int i = 0; i < Bucket.length; i++)
            for (int j = 0; j < Bucket[i]; j++)
                sorted_sequence[outPos++] = i;
        return sorted_sequence;
    }
    static void printSequence(int[] sorted_sequence) 
    {
        for (int i = 0; i < sorted_sequence.length; i++)
            System.out.print(sorted_sequence[i] + " ");
    }static int maxValue(int[] sequence) 
    {
        int maxValue = 0;
        for (int i = 0; i < sequence.length; i++)
            if (sequence[i] > maxValue)
                maxValue = sequence[i];
        return maxValue;
    }
    public static void main(String args[]) 
    {
        System.out.println("Sorting of randomly generated numbers using BUCKET SORT");
         int upperLimit = 100000000;
      int [] intBucket = new int [upperLimit];
      for (int i = 0; i < upperLimit; i++){
      intBucket[i] = (int)(Math.random()*100);
      }
      System.out.println(LocalDateTime.now());
      int maxValue = maxValue(intBucket);
      sort(intBucket,maxValue);
		System.out.println(LocalDateTime.now());
      }
}