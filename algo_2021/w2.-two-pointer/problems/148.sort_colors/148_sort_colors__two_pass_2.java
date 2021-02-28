public class Solution {
    /**
     * @param nums: A list of integer which is 0, 1 or 2 
     * @return: nothing
     */
    public void sortColors(int[] nums) {
        // write your code here
        partitionArray(nums, 1);
        partitionArray(nums, 2);
    }
    
    private void partitionArray(int[] nums, int k) {
        int lastSmallPointer = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] < k) {
                lastSmallPointer++;
                int tmp = nums[lastSmallPointer];
                nums[lastSmallPointer] = nums[i];
                nums[i] = tmp;
            }
        }
    }
}