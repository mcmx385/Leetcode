class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp != None:
            length += 1
            temp = temp.next
        temp = head
        if n == length:
            return head.next
        for i in range(length):
            if i == (length - n - 1):
                temp.next = temp.next.next
                return head
            temp = temp.next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        for i in range(n):
            fast = fast.next
        if fast == None:
            return head.next
        slow = head
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
