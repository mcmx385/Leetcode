class Solution {

  public int maxSubArray(int[] nums) {
    int maxVal = nums[0];
    int currVal;
    for (int i = 0; i < nums.length; ++i) {
      currVal = 0;
      for (int j = i; j < nums.length; ++j) {
        currVal += nums[j];
        maxVal = (currVal > maxVal) ? currVal : maxVal;
        currVal = (currVal < 0) ? 0 : currVal;
      }
    }
    return maxVal;
  }
}

class Solution {

  public int maxSubArray(int[] nums) {
    int maxVal = nums[0];
    int currVal = 0;
    for (int i = 0; i < nums.length; ++i) {
      currVal += nums[i];
      maxVal = (currVal > maxVal) ? currVal : maxVal;
      currVal = (currVal < 0) ? 0 : currVal;
    }
    return maxVal;
  }
}