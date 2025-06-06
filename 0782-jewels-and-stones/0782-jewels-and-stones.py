class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        is_jewel = set(jewels)
        result = 0 
        for s in stones:
            if s in is_jewel :
                result +=1
        return result 