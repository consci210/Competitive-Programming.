# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:  
        
        if not head: return 
        node = head 
        
        D = {} 
        
        while node: 
            if node.val not in D.keys():
                D[node.val] = [] 
            D[node.val].append(node) 
            tmp = node.val 
            node = node.next
            D[tmp][-1].next = None 
        
        nodes = [] 
        for k , v in D.items():
            if len(v) == 1 : 
                nodes.append(v[0])
        
        if not nodes: return 

        dum = nodes[0]
        
        node = dum
        
        for i in range(1,len(nodes)):
            
            node.next = nodes[i]
            node = node.next
        
        return dum