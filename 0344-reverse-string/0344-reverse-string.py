class Solution():
    def reverseString(self, s):

        left = 0
        right = len(s) - 1

        while left < right:

            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

#Approach-
#Left pointer starts from the beginning.Right pointer starts from the last character.
#Continue until both pointers meet.Swap the characters.
#Move left pointer one step forward.
#Move right pointer one step backward.

#Time complexity- O(n)
#space complexity - O(1)