class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefixSum = [1 if n & 1 else 0 for n in nums]
        for idx in range(len(nums)):
            prefixSum[idx] += prefixSum[idx-1] if idx-1 >= 0 else 0
        result = 0
        dic = {0: 1}
        for num in prefixSum:
            if num - k in dic:
                result += dic[num-k]
            dic[num] = dic.get(num, 0) + 1
        return result