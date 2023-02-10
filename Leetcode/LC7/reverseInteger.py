def reverseInteger(num):
    res = 0
    signed = num < 0  # extract -ve sign from num
    while num != 0:
        rem = num % 10
        res += rem
        res *= 10
        num /= 10
    res = -res if signed else res  # add -ve sign if extracted
