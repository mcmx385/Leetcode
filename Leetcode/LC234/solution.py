# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values == values[::-1]


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        values = []
        while head:
            values.append(head.val)
            head = head.next
        for i in range(len(values) // 2):
            if values[i] != values[-i - 1]:
                return False
        return True


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        value = 0
        while head:
            value = value * 10 + head.val
            head = head.next
        return str(value) == str(value)[::-1]


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        value = ""
        while head:
            value += str(head.val)
            head = head.next
        return value == value[::-1]
