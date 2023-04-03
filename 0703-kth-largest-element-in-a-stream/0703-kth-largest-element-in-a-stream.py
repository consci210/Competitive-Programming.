class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.storage = nums
        heapq.heapify(self.storage)
        self.k = k     
        while len(self.storage) > k :
            heapq.heappop(self.storage)
            
    def add(self, val: int) -> int:
        heapq.heappush( self.storage , val ) 
        if len (self.storage) > self.k :
            heapq.heappop(self.storage)
    
        return self.storage[0]
    
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)