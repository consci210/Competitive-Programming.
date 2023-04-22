class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]
        nums.sort()
        def backtrack(idx , arr) :
            prev = -11
            for i in range(idx , len(nums)):
                if nums[i] == prev :
                    continue 
                arr.append(nums[i])
                backtrack(i+1 , arr)
                answer.append(arr.copy())
                arr.pop()
                prev = nums[i]
                
        backtrack(0 , [])
        return answer 
            