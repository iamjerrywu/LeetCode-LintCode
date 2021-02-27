public class Solution {
    /**
     * @param nums: A list of integer which is 0, 1 or 2 
     * @return: nothing
     */
    public void sortColors(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0) {
            return;
        }
        
        int[] colorCnts = new int[3];
        for (int i = 0; i < nums.length; i++) {
            colorCnts[nums[i]]+=1;
        }
        
        int index = 0;
        for (int i = 0; i < colorCnts.length; i++) {
            int cnt = colorCnts[i];
            while(cnt > 0) {
                nums[index] = i;
                cnt--;
                index++;
            }
        }
    }
}