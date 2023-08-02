# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        locations = []
        while head:
            locations.append(head)
            head = head.next
        for i in range(len(locations) - 1, 0, -1):
            locations[i].next = locations[i - 1]
        locations[0].next = None
        return locations[-1]


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        values = []
        while head:
            values.append(head.val)
            head = head.next
        head = ListNode(values[-1])
        curr = head
        for i in range(len(values) - 2, -1, -1):
            curr.next = ListNode(values[i])
            curr = curr.next
        return head


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        curr = head
        while curr.next:
            temp = curr.next
            curr.next = temp.next
            temp.next = head
            head = temp
        return head


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return temp
