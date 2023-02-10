class Solution
{
public:
    vector<int> runningSum(vector<int> &nums)
    {
        int total = nums.size();
        for (int i = 1; i < total; ++i)
            nums[i] = nums[i] + nums[i - 1];
        return nums;
    }
};