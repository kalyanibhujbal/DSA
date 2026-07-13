class Solution():
    def canConstruct(self, ransomNote, magazine):
        count={}

        for ch in magazine:
            count[ch]=count.get(ch,0)+1

        for ch in ransomNote:
            if ch not in magazine or count[ch]==0:
                return False
            
            count[ch]-=1
        
        return True

#Approach-
#Create an empty dictionary.Visit every character of magazine.Store frequency.
#Visit every character of ransomNote.If a character is missing or its count becomes 0, return False.
#Otherwise decrease its count.
#If all characters are found, return True.
      
#Time Complexity- O(n + m)
#n = length of ransomNote
#m = length of magazine
#Space Complexity- O(1)