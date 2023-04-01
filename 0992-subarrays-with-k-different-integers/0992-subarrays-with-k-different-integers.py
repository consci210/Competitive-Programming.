class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def subarrayWithAtMostK( k ) :
            hashmap = {}
            l = r = 0 
            total = 0
            while r < len(nums) :
                hashmap[nums[r]] = hashmap.get(nums[r] , 0 ) + 1 
                while len(hashmap) > k :
                    hashmap[nums[l]] -= 1
                    if hashmap[nums[l]] == 0 :
                        del hashmap[nums[l]]
                    l+=1   
                r+=1
                total += (r-l +1 )
                
            return total 
        return subarrayWithAtMostK(k) - subarrayWithAtMostK( k-1)