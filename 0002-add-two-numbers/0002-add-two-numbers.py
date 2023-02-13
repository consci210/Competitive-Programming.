# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1=l1
        node2=l2
        carry=0
        newLinkedListNode=ListNode(0)
        currentNode=newLinkedListNode
        while node1 is not None or node2 is not None or carry!=0:
            value1=node1.val if node1 is not None else 0
            value2=node2.val if node2 is not None else 0
            sumValue=value1+value2+carry
        
            newNode=ListNode(sumValue%10)
            currentNode.next=newNode
            currentNode=newNode
        
        
            carry=sumValue//10
            node1=node1.next if node1 is not None else None
            node2=node2.next if node2 is not None else None
     
        return newLinkedListNode.next