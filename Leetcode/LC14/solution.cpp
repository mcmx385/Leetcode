class Solution
{
public:
    string longestCommonPrefix(vector<string> &strs)
    {
        string result = strs[0], temp;
        for (string str : strs)
            if (result != str)
            {
                int len = result.length() > str.length() ? str.length() : result.length();
                temp = "";
                for (int i = 0; i < len; ++i)
                    if (result[i] == str[i])
                        temp.push_back(result[i]);
                    else
                        break;
                result = temp;
            }
        return result;
    }
};