#include <vector>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int coinChange(vector<int> &coins, int amount)
{
    if (amount <= 0)
        return 0;
    sort(coins.begin(), coins.end());
    int dp[amount + 1];
    dp[0] = 0;
    for (int i = 1; i < amount + 1; ++i)
    {
        dp[i] = INT_MAX;
        for (int coin : coins)
        {
            if (i - coin < 0)
                break;
            if (dp[i - coin] != INT_MAX)
                dp[i] = min(dp[i], 1 + dp[i - coin]);
        }
    }
    if (dp[amount] == INT_MAX)
        return -1;
    return dp[amount];
}
int main()
{
    return 0;
}