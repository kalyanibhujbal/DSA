class Solution():
    def isPalindrome(self,s):
        left=0
        right=len(s)-1

        while left < right:

            while left < right and not s[left].isalnum():
                left +=1
            while left < right and not s[right].isalnum():
                right -=1

            if s[left].lower() != s[right].lower():
                return False
            
            left +=1
            right -=1

        return True

#Approach -
#Left pointer starts from the beginning.Right pointer starts from the end.Continue until both pointers meet.
#Skip spaces and special characters from the left and right
#Compare both characters after converting them to lowercase.
#Move both pointers toward the center.If every comparison matches, the string is a palindrome.

#Time Complexity- O(n)
#Space Complexity- O(1)