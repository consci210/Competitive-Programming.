# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = [] 
        answer = []
        current = head
        prev = None 
        if not head.next :
            return [0]
        
        while current :
            next_node = current.next 
            current.next = prev  
            prev = current
            current = next_node 

        current = prev 
        while current :
            if stack :
                while stack and stack[-1] <= current.val :
                    stack.pop()
                if stack :
                    answer.append(stack[-1])
                    stack.append(current.val)
                else :
                    stack.append(current.val)
                    answer.append(0)
            else :
                stack.append(current.val)
                answer.append(0)
                
            current = current.next  
        answer.reverse() 
        return answer
        
            