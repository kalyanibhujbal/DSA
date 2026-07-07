class Solution:
    def twoSum(self, nums, target):
        hashmap = {}

        for i in range(len(nums)):
            remaining = target - nums[i]

            if remaining in hashmap:
                return [hashmap[remaining], i]

            hashmap[nums[i]] = i

#Approach (Hashing)

#Instead of checking every pair (O(n²)),
#Create an empty dictionary ie.hash map to store - number : index
#For every number,Find - remaining=target - current_number
#If it already exists in dictionary, Return both indices (previous and current index).
#Store current number and its index.

#Time Complexity- O(n) Loop runs once.
#Space Complexity- O(n)  Dictionary stores all elements.


