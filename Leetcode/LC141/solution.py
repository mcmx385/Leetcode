class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        queue = []
        while head != None:
            if head in queue:
                return True
            queue.append(head)
            head = head.next
        return False


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
