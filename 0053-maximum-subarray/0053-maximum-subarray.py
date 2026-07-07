class Solution:
    def maxSubArray(self, nums):
        current_sum=nums[0]
        max_sum=nums[0]

        for i in range (1, len(nums)):
            current_sum= max(nums[i], current_sum + nums[i])

            max_sum= max(max_sum , current_sum)

        return max_sum

#Approach - (Kadane's Algorithm)
#Stores current sum and maximum sum found. At every element, either start new subarray or continue previous subarray
#Return maximum subarray sum.

#Time Complexity- O(n)
#Space Complexity- O(1)