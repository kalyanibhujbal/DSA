class Solution():
    def majorityElement(self, nums):
        count={}
        for num in nums:
            count[num]=count.get(num, 0)+1

            if count[num] > len(nums) //2:
                return num

#Approach-
#Create an empty dictionary.Visit every element.Count the frequency of every element.
#If any frequency becomes greater than n // 2, return that element.

#Time Complexity- O(n)
#Space Complexity- O(n)