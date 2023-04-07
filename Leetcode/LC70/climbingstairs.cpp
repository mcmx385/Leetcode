#include <iostream>
using namespace std;

class Solution
{
public:
    int climbStairs(int n)
    {
        if (n < 2)
            return 1;
        return climbStairs(n - 1) + climbStairs(n - 2);
    }
};

class Solution
{
public:
    int result[46];
    int climbStairs(int n)
    {
        if (n < 2)
            return 1;
        if (result[n] != 0)
            return result[n];
        int num = climbStairs(n - 1) + climbStairs(n - 2);
        result[n] = num;
        return num;
    }
};