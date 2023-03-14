# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next :
            return None  
        
        current = head
        length_of_list = 0 
        
        while current :
            length_of_list +=1 
            current = current.next
        
        current = head 
        target = length_of_list +1 - n
        count = 1
        prev = None 
        while current :
            if count == target :
                if prev :
                    prev.next = current.next 
                    break    
                else :
                    if current.next :
                        head = current.next  
                    else :
                        head = None 
                    break 
                    
            prev = current      
            current = current.next
            count +=1 
            
        return head  
          
                
            