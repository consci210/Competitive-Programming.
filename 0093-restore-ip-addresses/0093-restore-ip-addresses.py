class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        res = []
        
        if len(s) > 12 :
            return res
        
        def backtrack(start=0 , dots=0 , curr="" ):
            if dots == 4 and start == len(s):
                res.append(curr[:-1:])
                return 
            if dots >= 4 :
                return 
            
            for end in range(start , min(start+3 , len(s))):
                if ((int(s[start:end+1]) < 256 ) and ((start == end) or (s[start] != "0"))) :
                    backtrack( end + 1 , dots+1 , curr+s[start:end+1]+ ".")
            
        
        backtrack()
        return res 