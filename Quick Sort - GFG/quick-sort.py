class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if low < high:
            pivot = self.partition(arr, low, high)
            self.quickSort(arr, low, pivot-1)
            self.quickSort(arr, pivot+1, high)
        return arr 
    
    def partition(self,arr,low,high):
        pivot = low 
        i = low 
        j = high 
        while i < j :
            # Look for larger elts 
            while i < high :
                if arr[i] <= arr[pivot]:
                    i += 1 
                else:
                    break
            # look for smaller elts 
            while j > low :
                if arr[j] > arr[pivot]:
                    j -= 1
                else:
                    break
            if i < j :
                arr[i] , arr[j] = arr[j] , arr[i]
        arr[j] , arr[pivot] = arr[pivot] , arr[j]
        return j

        
        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends