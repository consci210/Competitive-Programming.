class MedianFinder:

    def __init__(self):
        self.length = 0 
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.length += 1
        
    def findMedian(self) -> float:
        self.nums.sort()
        if self.length % 2 == 0 :
            index1 = len(self.nums)//2 
            index2 = index1-1
            median = (self.nums[index1]+self.nums[index2]) /2 
            return median 
        
        else :
            index = len(self.nums) // 2
            return self.nums[index]
            


        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()