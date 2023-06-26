# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        arr = []
        while head is not None:
            arr.append(head)
            head = head.next
        k %= len(arr)
        arr = arr[-k:] + arr[:-k]
        if len(arr):
            head2 = ListNode(arr[0].val)
            curr = head2
            for i in range(1, len(arr)):
                curr.next = ListNode(arr[i].val)
                curr = curr.next
            return head2
        else:
            return None


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        arr = []
        while head is not None:
            arr.append(head)
            head = head.next
        k %= len(arr)
        head2 = arr[-k]
        arr[-1].next = arr[0]
        arr[-k - 1].next = None
        return head2


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        curr = head
        n = 0
        while curr is not None:
            curr = curr.next
            n += 1
        k %= n
        if k == 0:
            return head
        curr = head
        for i in range(n - k - 1):
            curr = curr.next
        head2 = curr.next
        curr.next = None
        curr = head2
        while curr.next is not None:
            curr = curr.next
        curr.next = head
        return head2
