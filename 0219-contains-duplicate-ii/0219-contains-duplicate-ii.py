class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = r = 0 
        seen = {}
        while r < len(nums) :
            if nums[r] in seen and abs(r-seen[nums[r]]) <= k:
                return (True)
            seen[nums[r]] = r
            r+=1
        return False