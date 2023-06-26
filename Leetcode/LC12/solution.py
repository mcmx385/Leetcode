import math


class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        dig = int(num / 1000)
        res += "M" * dig
        dig = int(num % 1000 / 100)
        if dig == 9:
            res += "CM"
        elif dig > 5:
            res += "D" + "C" * (dig - 5)
        elif dig == 5:
            res += "D"
        elif dig == 4:
            res += "CD"
        else:
            res += "C" * dig
        dig = int(num % 100 / 10)
        if dig == 9:
            res += "XC"
        elif dig > 5:
            res += "L" + "X" * (dig - 5)
        elif dig == 5:
            res += "L"
        elif dig == 4:
            res += "XL"
        else:
            res += "X" * dig
        dig = int(num % 10)
        if dig == 9:
            res += "IX"
        elif dig > 5:
            res += "V" + "I" * (dig - 5)
        elif dig == 5:
            res += "V"
        elif dig == 4:
            res += "IV"
        else:
            res += "I" * dig
        return res


class Solution:
    def intToRoman(self, num: int) -> str:
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hrns = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        ths = ["", "M", "MM", "MMM"]
        return (
            ths[int(num / 1000)]
            + hrns[int(num % 1000 / 100)]
            + tens[int(num % 100 / 10)]
            + ones[int(num % 10)]
        )


class Solution:
    def intToRoman(self, num: int) -> str:
        num_map = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        res = ""
        for key in num_map.keys():
            while num >= key:
                res += num_map[key]
                num -= key
        return res


class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
        res = ""
        for a, b in dic.items():
            if num == 0:
                break
            if num >= a:
                res += b * (num // a)
                num %= a
            var = 10 ** (math.ceil(math.log10(a)) - 1)
            if num >= a - var:
                res += dic[var] + b
                num -= a - var
        return res


class Solution:
    def intToRoman(self, num: int) -> str:
        i = 1
        dic = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        res = ""
        while num != 0:
            dig = num % pow(10, i) // pow(10, i - 1)
            if dig == 5:
                res = dic[dig * pow(10, i - 1)] + res
            elif dig == 1:
                res = dic[dig * pow(10, i - 1)] + res
            elif dig == 4:
                res = dic[1 * pow(10, i - 1)] + dic[5 * pow(10, i - 1)] + res
            elif dig == 9:
                res = dic[1 * pow(10, i - 1)] + dic[1 * pow(10, i)] + res
            elif dig < 4:
                res = dic[pow(10, i - 1)] * dig + res
            elif dig > 5 and dig < 9:
                dig -= 5
                res = dic[5 * pow(10, i - 1)] + dic[pow(10, i - 1)] * dig + res
            num = num // pow(10, i)
            num *= pow(10, i)
            i += 1
        return res


class Solution:
    def intToRoman(num: int):
        roman = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        res = ""

        for base, symbol in roman.items():
            res += symbol * (num // base)
            num %= base
        else:
            return res
