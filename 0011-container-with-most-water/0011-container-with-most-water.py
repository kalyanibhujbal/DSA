class Solution():
    def maxArea(self,height):
        left=0
        right=len(height)-1
        
        maximum=0
        while left < right:
            area= (right-left) * min(height[left], height[right])
            maximum=max(maximum, area)
            
            if height[left]< height[right]:
                left+=1
            else:
                right-=1
        return maximum 
    

#Approach
#One pointer at the beginning.One pointer at the end.
#Area = width × smaller height. Width=right-left. Height=minimum of both heights
#Keep the maximum area.
#Move the pointer having the smaller height.