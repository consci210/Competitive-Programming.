from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = [0 for _ in range(len(nums))]
        total = 0
        count = 0
        complement = defaultdict(int)
        complement[0] = 1  # base case to count subarrays starting at index 0

        for i in range(len(nums)):
            total += nums[i]
            prefixSum[i] = total

        for subArray in prefixSum:
            count += complement[subArray - k]
            complement[subArray] += 1

        return count
