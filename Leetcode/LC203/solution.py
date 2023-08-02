# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head != None and head.val == val:
            head = head.next
        if head == None:
            return head
        curr = head
        while curr != None and curr.next != None:
            while curr.next != None and curr.next.val == val:
                curr.next = curr.next.next
            curr = curr.next
        return head
