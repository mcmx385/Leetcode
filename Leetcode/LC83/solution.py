class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: list[ListNode]) -> list[ListNode]:
        if head == None:
            return None
        curr = head
        next = curr.next
        while next != None:
            if curr.val != next.val:
                curr.next = next
                curr = next
            next = next.next
        curr.next = None
        return head


class Solution:
    def deleteDuplicates(self, head: list[ListNode]) -> list[ListNode]:
        curr = head
        while curr:
            while curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next
            curr = curr.next
        return head


class Solution:
    def deleteDuplicates(self, head: list[ListNode]) -> list[ListNode]:
        if head == None or head.next == None:
            return head
        head.next = self.deleteDuplicates(head.next)
        if head.val == head.next.val:
            return head.next
        return head


def printList(head):
    while head != None:
        print(head.val)
        head = head.next


if __name__ == "__main__":
    solution = Solution()
    arr = [1, 1, 2]
    head = ListNode(arr[0])
    for i in range(1, len(arr)):
        head.next = ListNode(arr[i])
    printList(head)
