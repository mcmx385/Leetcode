class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        i = 0
        while l1 != None or l2 != None:
            if l1 != None:
                num1 += l1.val * (10**i)
                l1 = l1.next
            if l2 != None:
                num2 += l2.val * (10**i)
                l2 = l2.next
            i += 1
        num3 = num1 + num2
        l3 = ListNode(num3 % 10)
        tmp = l3
        num3 //= 10
        while num3 != 0:
            tmp.next = ListNode(num3 % 10)
            num3 = num3 // 10
            tmp = tmp.next
        return l3


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        l3 = ListNode(0)
        tmp = l3
        carry = 0
        while l1 != None or l2 != None:
            total = carry
            if l1 != None:
                total += l1.val
                l1 = l1.next
            if l2 != None:
                total += l2.val
                l2 = l2.next
            carry = total // 10
            tmp.next = ListNode(total % 10)
            tmp = tmp.next
        if carry != 0:
            tmp.next = ListNode(carry)
        return l3.next


class Solution:
    l3 = ListNode(0)
    tmp = l3
    carry = 0

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        total = self.carry
        if l1 != None:
            total += l1.val
        if l2 != None:
            total += l2.val
        if total == 0 and l1 == None and l2 == None:
            return self.l3.next

        self.carry = total // 10
        self.tmp.next = ListNode(total % 10)
        self.tmp = self.tmp.next

        if l1 != None and l2 != None:
            self.addTwoNumbers(l1.next, l2.next)
        elif l1 != None:
            self.addTwoNumbers(l1.next, None)
        elif l2 != None:
            self.addTwoNumbers(None, l2.next)
        elif self.carry > 0:
            self.tmp.next = ListNode(self.carry)
            self.tmp = self.tmp.next

        return self.l3.next
