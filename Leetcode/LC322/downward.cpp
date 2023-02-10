#include <vector>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int coinChange(vector<int> &coins, int amount)
{
    if (amount <= 0)
        return 0;
    int output = 0;
    sort(coins.begin(), coins.end());
    for (int i = coins.size() - 1; i >= 0 && amount > 0; --i)
    {
        cout << amount << " " << coins[i] << " " << amount / coins[i] << " " << amount % coins[i] << endl;
        output += amount / coins[i];
        amount = amount % coins[i];
    }
    if (amount > 0)
        return -1;
    return output;
}

int main()
{
    return 0;
}