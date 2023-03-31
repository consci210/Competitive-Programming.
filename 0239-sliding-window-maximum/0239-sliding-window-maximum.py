import collections 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:   
        deque = collections.deque( [nums.index(max((nums[0:k:] ) ))])
        maximum = [nums[deque[0]]]  
        for i in range( deque[0] , k):
            while deque and nums[deque[-1]] < nums[i]:
                deque.pop()
            deque.append(i)
        l = 1
        r = k
        while r < len(nums) :
            while deque and deque[0] < l :
                deque.popleft()  
            
            while deque and nums[deque[-1]] <= nums[r] :
                deque.pop()
                
            deque.append(r)
            r+=1 
            l+=1
            maximum.append(nums[deque[0]])
        return maximum 