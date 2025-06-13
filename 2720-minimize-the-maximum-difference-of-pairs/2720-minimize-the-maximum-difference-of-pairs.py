class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0 :
            return 0 
        nums.sort()
        def isValid(answer):
            i , count = 0 , 0 
            while (i < len(nums)-1):
                if abs(nums[i] - nums[i+1]) <= answer:
                    count +=1 
                    i+=2 
                else: 
                    i+=1 
                if count == p:
                    return True 
            return False 
        
        l,r = 0 , 10**9
        ans = 10**9 
        while l<=r:
            md = (l+r)//2
            if isValid(md) :
                ans = md 
                r = md-1 
            else:
                l = md+1 
        return ans 
