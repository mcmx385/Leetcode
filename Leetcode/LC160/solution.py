# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        tempA = headA
        tempB = headB
        while tempA != tempB:
            if tempA.next is None and tempB.next is None:
                return None  # condition not met
            else:
                if tempA.next is None:
                    while tempB.next is not None:
                        tempB = tempB.next
                        if headB.next is None:
                            return None
                        headB = headB.next
                    tempA = headA
                    tempB = headB
                elif tempB.next is None:
                    while tempA.next is not None:
                        tempA = tempA.next
                        if headA.next is None:
                            return None
                        headA = headA.next
                    tempA = headA
                    tempB = headB
                else:
                    tempA = tempA.next
                    tempB = tempB.next
        return tempA


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        tempA = headA
        tempB = headB
        while tempA != tempB:
            tempA = tempA.next if tempA else headB
            tempB = tempB.next if tempB else headA
        return tempA


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        lengA = 0
        tempA = headA
        while tempA:
            lengA += 1
            tempA = tempA.next
        lengB = 0
        tempB = headB
        while tempB:
            lengB += 1
            tempB = tempB.next
        if lengA > lengB:
            for i in range(lengA - lengB):
                headA = headA.next
        else:
            for i in range(lengB - lengA):
                headB = headB.next
        while headA != headB:
            headA = headA.next
            headB = headB.next
            if headA == None or headB == None:
                return None
            if headA == headB:
                return headA
        return None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        arr = []
        tempA = headA
        while tempA:
            arr.append(tempA)
            tempA = tempA.next
        tempB = headB
        while tempB:
            if tempB in arr:
                return tempB
            tempB = tempB.next
        return None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        while headB:
            tempA = headA
            while tempA:
                if tempA == headB:
                    return tempA
                tempA = tempA.next
            headB = headB.next
        return None
