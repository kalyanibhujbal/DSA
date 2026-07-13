class Solution():
    def isHappy(self,n):
        seen=set()
        
        while n!=1:

            if n in seen:
                return False

            seen.add(n)

            total=0
            while n>0:
                digit= n % 10
                total += digit * digit
                n= n // 10

            n=total

        return True

#Approach-
#Create an empty set.Continue until we reach 1.If the number repeats, a loop exists → return False.Store the current number.
#Stores the sum of squares.Get the last digit by modulus operator .Add its square in total  then Remove the last digit by divide.Repeat the process with the new number and Keep calculating the sum of squares of digits.
#If the number becomes 1 → return True.


#Time Complexity- O(log n)
#Space Complexity- O(log n)