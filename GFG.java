import java.io.*;
class GFG{
    public static void main(String[]args)
    {
    int arr[]={3,5,6,7,8,22};
    int val=25;
    int arrSize=arr.length;
    System.out.println(isPairSum(arr,arrSize,val));
    }
    public static int isPairSum(int A[],int N,int X){
        int i=0;
        int j=N-1;
        while(i<j){
            if(A[i]+A[j]==X)
            return 1;
            else if (A[i]+A[j]<X){
                i++;
            }
            else 
            j--;
        

            
        }
        return 0;
    }
    
}