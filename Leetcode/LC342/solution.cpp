class Solution
{
public:
    bool isPowerOfFour(int n)
    {
        float m = (float)n;
        while (m > 1)
            m /= 4;
        if (m == 1 && (int)m == ceil(m))
            return true;
        return false;
    }
};