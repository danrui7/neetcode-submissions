# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        k = 0 # index
        curr = head
        while curr.next is not None:
            curr = curr.next
            k += 1
        if n>k +1 :
            return head
        if k - n + 1== 0:
            head = head.next
            return head
        curr = head
        for i in range(0,k-n+1):
            if (i +1) == k-n + 1:
                curr.next = curr.next.next
                break
            curr = curr.next
        
        return head



        