class Solution
{
public:
    bool isValid(string s)
    {
        stack<char> stk;
        char top;
        for (char c : s)
        {
            if (c == '{' || c == '[' || c == '(')
            {
                stk.push(c);
                continue;
            }
            else if (c == '}' || c == ']' || c == ')')
            {
                if (stk.empty())
                {
                    return false;
                }
                top = stk.top();
                if (top == '{' && c == '}' ||
                    top == '(' && c == ')' ||
                    top == '[' && c == ']')
                {
                    stk.pop();
                    continue;
                }
            }
            return false;
        }
        return stk.empty();
    }
};