class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.helper(s, 0, [], res)
        return res
    
    def helper(self, s, start, path, res):
        if len(path) == 4 and start == len(s):
            res.append(".".join(path))
            return
        if len(path) == 4 or start == len(s):
            return
        for i in range(start, min(start+3, len(s))):
            if i > start and s[start] == '0':
                break
            if int(s[start:i+1]) <= 255:
                path.append(s[start:i+1])
                self.helper(s, i+1, path, res)
                path.pop()
