class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(str)     
        curr = 0 
        longest = 0 
        left  = 0 
        for right in range(len(s)):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]]+1 
            curr = right - left + 1 
            longest = max(curr,longest)
            seen[s[right]] = right 

        return longest
