class Solution():
    def plusOne(self,digits):
        n=len(digits)

        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i]=digits[i] +1
                return digits
            
            digits[i]=0

        return[1]+digits

#Approach-
#Traverse from the last digit to the first.
#If digit is less than 9, add 1 and return.
#If digit is 9, make it 0 and carry 1 to the previous digit.
#If every digit is 9, add 1 at the beginning.

#Time Complexity- O(n)
#Space Complexity- O(1)