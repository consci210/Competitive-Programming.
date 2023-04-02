class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        answer = []
        potions.sort()
        for spell in spells :
            total = 0 
            l = 0
            r = len(potions)-1
            while l <= r :
                mid = (l+r)//2
                if potions[mid]*spell >= success :
                    total += r-mid +1
                    r = mid -1
                if potions[mid]*spell < success :
                    l = mid +1 
            answer.append(total)
            
        return answer 
                    