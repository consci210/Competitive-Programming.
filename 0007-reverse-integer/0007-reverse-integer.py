class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        negative = 0            
        str_x = str(abs(x))
        rev = int(str_x[::-1])
        if rev >= pow(2,32)/2:
            return 0
        if x < 0: 
            rev = 0-rev     
        return rev