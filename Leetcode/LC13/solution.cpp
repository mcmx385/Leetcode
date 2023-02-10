#include <iostream>
#include <string>
#include <map>

using namespace std;

class Solution
{
public:
    int romanToInt(string s)
    {
        map<char, int> key;
        key['I'] = 1;
        key['V'] = 5;
        key['X'] = 10;
        key['L'] = 50;
        key['C'] = 100;
        key['D'] = 500;
        key['M'] = 1000;

        int result = 0;
        int prev = 0;
        for (int i = s.length() - 1; i >= 0; --i)
        {
            int curr = key[s[i]];
            result = curr >= prev ? result + curr : result - curr;
            prev = curr;
        }
        return result;
    }
};