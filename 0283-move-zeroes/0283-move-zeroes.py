class Solution():
    def moveZeroes(self, nums):
       
        j=0

        for i in range(len(nums)):
            if nums[i] != 0 :
                nums[i], nums[j] = nums[j], nums[i]
                j +=1

        return nums

#Approach- 
#Keep one pointer (j) Points to the position where the next non-zero element should be placed.Traverse array using i.
#Check if current number is non-zero. Swap current non-zero element with position j.
#Move pointer to the next available position and then Return modified array.

#Time Complexity- O(n)
#Space Complexity - O(1)