# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        slow = head
        fast = head
        count = 1
        while fast is not None:
            if fast.next is not None:
                if fast.next.next is not None:
                    fast = fast.next.next
                    slow = slow.next
                    count += 1
                else:
                    slow = slow.next
                    count += 1
                    break
            else:
                break
        return slow
