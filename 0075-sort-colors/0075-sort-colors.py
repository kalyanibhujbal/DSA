class Solution():
    def sortColors(self, nums):
        low=0
        mid=0
        high=len(nums)-1
        
        while mid <= high:
            if nums[mid]==0:
                nums[low], nums[mid]=nums[mid], nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid], nums[high]=nums[high], nums[mid]
                high-=1
    
#Approach-
# low-> next position for 0
# mid-> current element
# high -> next position for 2
#if mid=0 swap it with low and move both pointers,elif mid=1 nothing to do , move mid pointer, else mid=2 then swap it with high

#Time complexity - O(n)
#Space complexity - O(1)