class Solution
{
public:
    string addSpaces(string s, vector<int> &spaces)
    {
        string result = "";
        int space_ind = 0;
        int str_ind = 0;
        for (char c : s)
        {
            if (space_ind < spaces.size() && str_ind == spaces[space_ind])
            {
                result += " ";
                space_ind++;
            }
            result += c;
            ++str_ind;
        }
        return result;
    }
};