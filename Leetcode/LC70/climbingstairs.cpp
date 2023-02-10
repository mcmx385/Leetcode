#include <iostream>
using namespace std;
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
int climbStairs2(int n)
{
    if (n < 2)
        return 1;
    return climbStairs2(n - 1) + climbStairs2(n - 2);
}
int main()
{
    cout << climbStairs(5) << endl;
    cout << climbStairs2(5) << endl;
}