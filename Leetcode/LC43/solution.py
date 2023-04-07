class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1)*int(num2))


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        base = 0
        for num in num2[::-1]:
            res += int(num1)*int(num)*pow(10, base)
            base += 1
        return str(res)


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0]*(len(num1)+len(num2))
        for i, num in enumerate(num2[::-1]):
            for j, tar in enumerate(num1[::-1]):
                res[i+j] += int(num)*int(tar)
                res[i+j+1] += res[i+j]//10
                res[i+j] %= 10
        res = res[::-1]
        while len(res) > 1 and res[0] == 0:
            res.pop(0)
        return ''.join(map(str, res))
