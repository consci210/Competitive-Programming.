"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head :
            return 
        values = []
        current = head
        length = 0 
        while current :
            values.append(current.val)
            current = current.next
            length+=1 
            
        hashmap = {}
        current = head
        for i in range(length):
            hashmap[current] = i 
            current= current.next
        
        node_list = [Node(val) for val in values]
        node_list.append(None)
        
        current = head
        for i in range(length):
            node_list[i].next = node_list[i+1]
            if current.random :
                node_list[i].random = node_list[hashmap[current.random]]
            current = current.next 
            
        return node_list[0]
        
        
        
        
        
#         if not head :
#             return 
#         current = head
#         l_list = []
#         new_l_list = []
#         count = 0
#         prev = None 
    
#         while current :
#             l_list.append(current)
#             new_node = Node(current.val)
#             new_l_list.append(new_node)
#             if prev :
#                 prev.next = new_node
#             prev = new_node  
#             current = current.next
#             count+=1 
#         for i in range(count):
#             if not l_list[i].random :
#                 next_random = None 
#             else :
#                 next_random_index = l_list.index(l_list[i].random)
#                 next_random = new_l_list[next_random_index]
#             new_l_list[i].random = next_random 
            
#         return new_l_list[0]
            
            