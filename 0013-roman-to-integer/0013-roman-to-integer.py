class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1 , "V": 5, "X": 10,"L": 50 , "C": 100 ,"D": 500 ,"M": 1000 }
        result = 0 
        before = 1
        for num in reversed(s):
            if values[num] < before:
                result -= values[num]
            else:
                result += values[num]
            before = values[num]
        return result 