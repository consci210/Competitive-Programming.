class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        total = 0 
        prefix_sum = [0]
        hashmap = {}
        for i in range (len(nums)) :
            prefix_sum.append(prefix_sum[-1] + nums[i])
         
        l = r = 0 
        while r < len(prefix_sum) :
            
            if prefix_sum[r] - goal in hashmap:
                total += hashmap[prefix_sum[r]-goal]
            
            hashmap[prefix_sum[r]] = hashmap.get(prefix_sum[r] , 0 ) + 1
            r+=1
            
        return total