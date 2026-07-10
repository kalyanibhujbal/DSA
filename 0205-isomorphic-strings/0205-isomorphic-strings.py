class Solution():
    def isIsomorphic(self,s,t):
        map1={}
        map2={}

        for i in range(len(s)):
            
            if s[i] in map1:
                if map1[s[i]] != t[i]:
                    return False
            else:
                map1[s[i]]=t[i]

            if t[i] in map2:
                if map2[t[i]] != s[i]:
                    return False
            else:
                map2[t[i]]=s[i]

        return True

#Approach-
#Create two dictionaries.
#map1 → maps characters from s to t
#map2 → maps characters from t to s
#Visit every character.Check if the current character already has a mapping.If the existing mapping is different, return False.Create a new mapping.
#Repeat the same process in reverse using map2.
#This prevents two different characters from mapping to the same character.

#Time Complexity- O(n)
#Space Complexity- O(n)