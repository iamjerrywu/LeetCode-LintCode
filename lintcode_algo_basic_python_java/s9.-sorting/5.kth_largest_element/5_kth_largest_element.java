public class Solution {
    /**
     * @param n: An integer
     * @param nums: An array
     * @return: the Kth largest element
     */
    public int kthLargestElement(int n, int[] nums) {
        // write your code here
        if (nums == null || nums.length ==0) {
            return -1;
        }

        return quickSelect(nums, 0, nums.length - 1, n);
    }

    private int quickSelect(int[] nums, int start, int end, int n) {
        if (start >= end) {
            return nums[start];
        }
        
        int mid = start + (end - start)/2;
        int pivot = nums[mid];
        int left = start, right = end;
        
        while (left <= right) {
            // keep traversing
            while (left <= right && nums[left] > pivot) {
                left++;
            }
            while (left <= right && nums[right] < pivot) {
                right--;
            }
            if (left <= right) {
                // swap value
                int tmp = nums[left];
                nums[left] = nums[right];
                nums[right] = tmp;
                left++;
                right--;
            }
        }
        // locate kth element
        if (start + n - 1 <= right) {
            return quickSelect(nums, start, right, n);
        } 
        if (start + n - 1 >= left) {
            return quickSelect(nums, left, end, n - (left - start));
        }
        return nums[right + 1];

    }        
}