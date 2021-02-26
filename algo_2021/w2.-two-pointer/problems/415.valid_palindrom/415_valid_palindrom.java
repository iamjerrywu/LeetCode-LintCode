public class Solution {
    /**
     * @param s: A string
     * @return: Whether the string is a valid palindrome
     */
    public boolean isPalindrome(String s) {
        // write your code here
        
        // two pointers
        int left = 0, right = s.length() - 1;
        while (left < right) {
            
            // if non-alphanumeric characters, keep traversing
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }
            while(left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }
            // if not the same, break earlier
            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
                return false;
            }
             // keep traversing
            left++;
            right--;
            }
         return true;
    }
}