class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_of_nums = set(nums)
        longest = 0
        for num in set_of_nums :
            length = 0 
            if (num-1) not in set_of_nums :
                while num in set_of_nums :
                    length += 1
                    num+=1
                longest = max(longest , length)
        return longest
                    
            
        