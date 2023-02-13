class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        answer = 0

        piles = sorted(piles ,reverse=True)
        count = 0
        for i , value in enumerate(piles , 1):
            if i%2 == 0 and count < len(piles)//3  :
                answer+=value
                count += 1
        return answer 
            