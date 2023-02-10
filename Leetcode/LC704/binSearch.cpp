#include <iostream>
#include <vector>

using namespace std;

int search(vector<int> &nums, int target)
{
    int high = nums.size() - 1;
    int low = 0;
    int mid;
    while (low <= high)
    {
        mid = low + (high - low) / 2;
        if (nums[mid] == target)
            return mid;
        else if (nums[mid] < target)
            low = mid + 1;
        else if (nums[mid] > target)
            high = mid - 1;
    }
    return -1;
}
int main()
{
    vector<int> vec = {-1, 0, 3, 5, 9, 12};
    int result = search(vec, 3);
    cout << result << endl;
}