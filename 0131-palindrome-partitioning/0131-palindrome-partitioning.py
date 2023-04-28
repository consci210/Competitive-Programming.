from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []
        
        def part(idx=0):
            if idx == len(s):
                res.append(curr.copy())
                return  
            for i in range(idx, len(s)):
                if self.is_palindrome(s[idx:i+1]):
                    curr.append(s[idx:i+1])
                    part(i+1)  
                    curr.pop()
        part()
        return res
    
    def is_palindrome(self, string):
        return string == string[::-1]
