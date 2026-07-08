class Solution():
    def rotate(self,nums,k):
         n=len(nums)
         k=k % n

         nums.reverse()
         nums[:k]=reversed(nums[:k])
         nums[k:]=reversed(nums[k:])
        
#Approach- 
#k = number of steps /move every element k positions to the right
#Reverse the whole array.
#Reverse the first k elements.
#Reverse the remaining elements.

#Time Complexity- O(n)
#Space Complexity- O(1)

