class Solution
{
public:
    int myAtoi(string s)
    {
        long long int result = 0;
        bool negative = false;
        int i = 0;
        while (s[i] == ' ')
            ++i;
        if (s[i] == '-')
        {
            negative = true;
            ++i;
        }
        else if (s[i] == '+')
            ++i;
        for (; i < s.length(); ++i)
        {
            int num = s[i] - '0';
            if (num > 9 or num < 0)
                break;
            result = result * 10 + num;
            if (negative && -result <= INT_MIN)
                return INT_MIN;
            if (!negative && result >= INT_MAX)
                return INT_MAX;
        }
        return negative ? -result : result;
    }
};