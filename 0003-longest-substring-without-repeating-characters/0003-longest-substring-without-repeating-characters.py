class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow = 0
        fast = 0
        max_len = 0
        if len(s) <2:
            return len(s)
        dic = {}

        for k, t in enumerate(s):
            if t not in dic or slow > dic[t]:
                dic[t] = k
                fast += 1
                max_len = max(max_len, fast-slow)
            else:
                slow = dic[t] + 1
                dic[t] = k
                fast +=1
                max_len = max(max_len, fast-slow)

        return max_len