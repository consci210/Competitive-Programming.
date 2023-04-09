class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        N = len(letters)
        start = 0 
        end = N - 1
        smallest = letters[end]
        
        while start <= end :
            mid = (start+end) // 2
            if letters[mid] <= target :
                start = mid + 1
            elif letters[mid] > target :
                smallest = min(letters[mid] , smallest )
                end = mid - 1
                
        if start == N :
            return letters[0]
        else:
            return smallest 
             
    