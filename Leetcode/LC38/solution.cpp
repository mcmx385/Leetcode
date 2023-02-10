class Solution
{
public:
    string countAndSay(int n)
    {
        if (n == 1)
            return "1";

        string result = "";
        string res = countAndSay(n - 1);
        int len = res.length();

        int count = 1;
        char prev = res.at(0);
        char curr = res.at(0);

        for (int i = 1; i < len; ++i)
        {
            curr = res.at(i);
            if (prev != curr)
            {
                result += to_string(count);
                result += prev;
                prev = curr;
                count = 0;
            }
            ++count;
        }

        result += to_string(count);
        result += curr;

        return result;
    }
};