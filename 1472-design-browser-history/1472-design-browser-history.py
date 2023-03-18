class Node :
    def __init__(self , value):
        self.val = value
        self.prev = None 
        self.next = None 
             
class BrowserHistory:
     
    def __init__(self, homepage: str):
        self.current = Node(homepage)

    def visit(self, url: str) -> None:
        self.visited_node = Node(url)
        self.visited_node.prev = self.current 
        self.current.next = self.visited_node
        self.current =  self.visited_node
        
    def back(self, steps: int) -> str:
        while self.current.prev and steps :
            self.current = self.current.prev 
            steps -=1 
        return self.current.val 
    
    def forward(self, steps: int) -> str:
        while self.current.next and steps :
            self.current = self.current.next
            steps-=1
        return self.current.val 


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)