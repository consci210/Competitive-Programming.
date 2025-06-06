class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = defaultdict(int)
        for l in magazine:
            letters[l]+=1
        
        for l in ransomNote:
            letters[l]-=1 
            if letters[l] < 0:
                return False 
        return True 
            