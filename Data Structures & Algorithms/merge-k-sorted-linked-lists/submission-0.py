# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        array = []
        for i in range(len(lists)):
            cur = lists[i]
            while cur:
                array.append(cur.val)
                cur = cur.next
        array.sort()
        res = ListNode()
        cur = res

        for num in array:
            cur.next = ListNode(num)
            cur = cur.next
        return res.next