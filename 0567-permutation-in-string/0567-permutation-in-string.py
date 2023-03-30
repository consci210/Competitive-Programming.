from collections import defaultdict

class Solution:
    def checkInclusion(self ,s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
    
        freq = defaultdict(int)
    
        for char in s1:
            freq[char] += 1

        left, right = 0, 0

        while right < len(s2):
            freq[s2[right]] -= 1

            if right - left + 1 > len(s1):
                freq[s2[left]] += 1
                left += 1

            if right - left + 1 == len(s1) and all(val == 0 for val in freq.values()):
                return True

            right += 1

        return False