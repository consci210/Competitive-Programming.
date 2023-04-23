class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def permutation(idx=0, arr=nums):
            if idx == len(nums):
                answer.append(arr.copy())
                return

            for i in range(idx, len(nums)):
                arr_copy = arr.copy()
                arr_copy[i], arr_copy[idx] = arr_copy[idx], arr_copy[i]
                permutation(idx+1, arr_copy)

        permutation()
        return answer