class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 1
        profit = 0 
        while r < len(prices):
            if prices[r] > prices[l] :
                profit = max(profit , prices[r]-prices[l])
            else:
                l = r
            r+=1 
        return profit 
    
    
    # greatest_to_right = [0]
        # difference = 0
        # for i in range(len(prices)-1 , -1 ,-1):
        #     greatest_to_right.append(max(greatest_to_right[-1] , prices[i])) 
        # greatest_to_right.reverse()
        # for i in range(len(prices)):
        #     difference = max (difference , greatest_to_right[i]-prices[i])
        # return difference 