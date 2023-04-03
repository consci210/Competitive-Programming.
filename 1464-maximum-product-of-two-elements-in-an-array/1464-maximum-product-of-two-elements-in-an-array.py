class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        num1 = heapq.heappop(nums)
        num2 = heapq.heappop(nums)
        return ((num1 + 1)*(num2+1) )
    