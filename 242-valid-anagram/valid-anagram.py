class Solution(object):
    def isAnagram(self, s, t):
        
        if len(s) != len(t):
            return False

        count={}

        for ch in s:
            count[ch]=count.get(ch,0) + 1

        for ch in t:
            if ch not in count:
                return False
        
            count[ch]=count[ch]-1

            if count[ch] < 0:
                return False

        return True        
    
#Approach -
#If lengths are different, return False.
#Count the frequency of each character in the first string.
#Decrease the count using the second string.
#If any count becomes negative, they are not anagrams.
#If all counts become zero, return True.

#Time complexity -O(n)
#Space complexity -O(n)