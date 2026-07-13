class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        array = []
        current = head
        while current is not None:
            array.append(current)
            current = current.next
        
        l, r = 0, len(array) - 1
        while l < r:
            array[l].next = array[r]
            l += 1
            if l == r:
                break
            array[r].next = array[l]
            r -= 1
        
        array[l].next = None