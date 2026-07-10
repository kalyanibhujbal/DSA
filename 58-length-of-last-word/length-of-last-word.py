class Solution():
    def lengthOfLastWord(self,s):
        length=0
        i=len(s)-1
        
        while i>=0 and s[i]==" ":
            i -=1
        while i>=0 and s[i] !=" ":
            length +=1
            i -=1
        
        return length

#Approach -
#length -Stores the length of the last word.
#i- starts from last charcter
#Skip trailing spaces ie. if there is space skip it and decrease the pointer to previous charcter.
#Count characters until another space is found.
#if not space found...ie. its a charcter ..increase length by 1 and decrease pointer to previous charcter.


#Time Complexity- O(n)
#Space Complexity- O(1)