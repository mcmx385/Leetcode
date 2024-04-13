class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aa = 0
        for c in a:
            aa = aa * 2 + int(c)
        bb = 0
        for c in b:
            bb = bb * 2 + int(c)
        c = aa + bb
        if c == 0:
            return "0"
        s = ""
        while c > 0:
            s += str(c % 2)
            c //= 2
        s = s[::-1]
        return s


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        s = ""
        while i >= 0 or j >= 0:
            sum = carry
            sum += int(a[i]) if i >= 0 else 0
            sum += int(b[j]) if j >= 0 else 0
            s += str(sum % 2)
            carry = sum // 2
            i = i - 1 if i >= 0 else i
            j = j - 1 if j >= 0 else j
        if carry != 0:
            s += str(carry)
        return s[::-1]


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        s = ""
        a = list(a)
        b = list(b)
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            s += str(carry % 2)
            carry = carry // 2
        return s[::-1]


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        print(bin(int(a, 2) + int(b, 2)))
        return bin(int(a, 2) + int(b, 2))[2:]


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if "" in (a, b):
            return a or b
        if a[-1] == "1" and b[-1] == "1":
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), "1") + "0"
        if a[-1] == "0" and b[-1] == "0":
            return self.addBinary(a[:-1], b[:-1]) + "0"
        return self.addBinary(a[:-1], b[:-1]) + "1"


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if "" in (a, b):
            return a or b
        a_2 = int(a, 2)
        b_2 = int(b, 2)
        while carry != 0:
            carry = (a_2 & b_2) << 1
            a_2 = a_2 ^ b_2
            b_2 = carry
        return bin(a_2)[2:]


if __name__ == "__main__":
    s = Solution()
    print(s.addBinary("11", "1"))
    print(s.addBinary("1010", "1011"))
