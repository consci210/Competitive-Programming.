class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        if sum(nums) == 0 :
            return 0 
        
        l = 0 
        r = len(nums) - 1
        neg = 0 
        pos = 0 
        while l<=r :
            mid = (l+r)//2 
            if nums[mid] > 0 :
                pos += r-mid +1
                r = mid -1 
            
            elif nums[mid] < 0 :
                neg += mid - l +1 
                l = mid + 1
                
            else :
                while nums[mid] == 0 and mid<len(nums)-1:
                    mid+=1 
                pos += r - mid +1
                mid-=1
                while nums[mid] == 0  and mid > 0 :
                    mid-=1
                neg += mid - l + 1     
                return(max(neg , pos))
            
        return( max( pos,neg ) )
                    