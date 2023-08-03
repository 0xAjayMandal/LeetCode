# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        left = dummyNode
        right = head

        #Shifting right as per n value
        while n > 0 and right:
            right = right.next
            n -= 1
        
        #Shifting both pointer till right become NULL
        while right:
            left = left.next
            right = right.next
        
        #Delete the nth Node
        left.next = left.next.next
        return dummyNode.next
        