class Solution():
    def removeDuplicates(self,nums):
        if len(nums)==0:
            return 0
        
        i=0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i +=1
                nums[i]=nums[j]
        return i+1
    
#Approach-
#i -> points to the last unique element
#j-> scans the array, then start chceking from second element
#If a new elment is found, move the unique pointer.place the unique element
#return the number of unique elements

#Time complexity- O(n)
#Space complexity- O(1)