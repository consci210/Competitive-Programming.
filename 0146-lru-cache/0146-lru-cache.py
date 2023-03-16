class Node :
    def __init__(self, key , val ) :
        self.key = key 
        self.val = val 
        self.prev = None 
        self.next = None 

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity 
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right 
        self.right.prev = self.left 
        self.cache = dict()
        
    def insert(self , node ) :
        prev = self.right.prev
        nxt = self.right 
        nxt.prev = node 
        prev.next = node 
        node.next = nxt
        node.prev = prev
        
    def remove(self ,node ) :
        prev = node.prev
        nxt = node.next 
        prev.next = nxt
        nxt.prev = prev
        
    def get(self, key: int) -> int:
        if key in self.cache : 
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return (node).val 
        else :
            return -1 
            
    def put(self, key: int, value: int) -> None:
        if key in self.cache :
            node = self.cache[key]
            self.remove(node)
            node.val = value 
            self.insert(node)
        else :
            node = Node(key,value)
            self.cache[key] = node 
            self.insert(node)
            
            if len(self.cache) > self.cap :
                lru = self.left.next 
                del self.cache[lru.key]
                self.remove(lru)
                

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)