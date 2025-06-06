class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        is_jewel = defaultdict(int)
        result = 0 
        for j in jewels:
            if j in is_jewel:
                is_jewel[j]+=1
            else:
                is_jewel[j]=1
        for s in stones:
            if s in is_jewel:
                result+= is_jewel[s]
        return result 
            