class Solution:
    def largestInteger(self, num: int) -> int:
        nums = list(str(num))
        odds = []
        evens = []
        for num in nums :
            if int(num) % 2 == 0 :
                evens.append(num)
            else :
                odds.append(num)
        odds.sort()
        evens.sort()
        
        for i in range(len(nums)):
            if int(nums[i]) % 2 == 0 :
                nums[i] = evens.pop()
            else:
                nums[i] = odds.pop()
        
        result = "".join(nums)
        return int(result)
        