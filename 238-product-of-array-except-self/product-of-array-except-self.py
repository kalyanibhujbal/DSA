class Solution:
    def productExceptSelf(self,nums):
        n=len(nums)

        answer= [1] * n

        prefix=1
        for i in range(n):
            answer[i]=prefix
            prefix *= nums[i]

        suffix=1
        for i in range(n-1, -1, -1):
            answer[i]*= suffix
            suffix *= nums[i]

        return answer
        
#Approach -
#For every index, Answer = Left Product × Right Product
#Instead of calculating repeatedly, store prefix products first, then multiply with suffix products.


#Time Complexity- O(n)  - two traversals.
#Space Complexity- O(1)