class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        prefix_sum = [0] 
        hashmap = {}
        for i in range(len(nums)):
            prefix_sum.append(prefix_sum[-1]+nums[i])
        print(prefix_sum)
        
        for i in range(len(prefix_sum)):         
            if (prefix_sum[i] - k) in hashmap :
                total+= hashmap[prefix_sum[i]-k]
            if prefix_sum[i] in hashmap :
                hashmap[prefix_sum[i]] +=1 
            else :
                hashmap[prefix_sum[i]] = 1
        return total
           