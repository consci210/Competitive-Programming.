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
