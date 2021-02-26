class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        
        # two pointers
        left, right = 0, len(s) - 1
        
        while left < right:
            # if non-alphanumeric characters, keep traversing
            while left < right and not s[left].isalnum():
                left+=1
            while left < right and not s[right].isalnum():
                right-=1
            # if not the same, break earlier
            if s[left].lower() != s[right].lower():
                return False
            # keep traversing
            left+=1
            right-=1
        return True