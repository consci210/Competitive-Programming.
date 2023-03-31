class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        l = 0 
        r = len(cardPoints)-k
        
        current_sum = sum(cardPoints[l:r])
        minimum = current_sum
        
        while r < len(cardPoints) :
            current_sum -= cardPoints[l]
            current_sum += cardPoints[r]
            minimum = min(current_sum , minimum)
            l+=1
            r+=1 
        
        return total - minimum
            
        
        