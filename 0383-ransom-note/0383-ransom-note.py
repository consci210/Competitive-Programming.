class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = defaultdict(int)
        answers = defaultdict(int)
        for l in ransomNote:
            if l in letters:
                letters[l]+=1
            else:
                letters[l] = 1
        
        for a in magazine:
            if a in answers:
                answers[a]+=1
            else:
                answers[a]= 1
        
        for l in letters:
            if letters[l] > answers[l]:
                return False 
        return True 

            