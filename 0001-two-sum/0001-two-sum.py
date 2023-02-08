class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited= {}
        for i in range (len(nums)):
            j = target - nums[i]
            if j in visited :
                return (visited[j] , i)
            else :
                visited[nums[i]] = i 
        return visited 
    