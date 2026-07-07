class Solution:
    def containsDuplicate(self, nums):
        seen=set()
        
        for num in nums:
            if num in seen:
                return True
            
            seen.add(num)

        return False 

#Approach-
#traverse the array.If the element already exists in the set, return True .Otherwise, add it to the set.

#Time Complexity - O(n)
#Each lookup and insertion in a hash set is O(1) on average.

#Space Complexity- O(n)
#In the worst case scenario if all elements are unique, the set stores all n elements.