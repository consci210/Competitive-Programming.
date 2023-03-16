class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size = maxSize 
        self.stack = []
        self.count = 0
        
    def push(self, x: int) -> None:
        if self.count < self.max_size :
            self.stack.append(x)
            self.count+=1 
        else :
            pass 
        
    def pop(self) -> int:
        if self.stack :
            self.count-=1 
            return self.stack.pop()
        else:
            return -1 

    def increment(self, k: int, val: int) -> None:
        if self.count <= k :
            for i in range(self.count) :
                self.stack[i] = self.stack[i] + val 
        else :
            for i in range(k):
                self.stack[i] = self.stack[i] + val 


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)