class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.answer = []

        def backtrack(idx, curr):
            if len(curr) >= 2:
                self.answer.append(curr.copy())
            used = set()
            for i in range(idx, len(nums)):
                if nums[i] in used:
                    continue
                if not curr or nums[i] >= curr[-1]:
                    used.add(nums[i])
                    curr.append(nums[i])
                    backtrack(i + 1, curr)
                    curr.pop()

        backtrack(0, [])
        return self.answer
