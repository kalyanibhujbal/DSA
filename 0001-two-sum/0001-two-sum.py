class Solution:
    def twoSum(self, nums, target):
        hashmap = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hashmap:
                return[hashmap[complement], i]

            hashmap[nums[i]] = i

#Approach (Hashing)

#Instead of checking every pair (O(n²)),
#Use a dictionary (hash map). Store  number : index
#For every number,Find
#complement=target - current_numbe
#If it already exists in dictionary, Return both indices (previous and current index).
#Store current number and its index.

#Time Complexity- O(n) Loop runs once.
#Space Complexity- O(n)  Dictionary stores all elements.


