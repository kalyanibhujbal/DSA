class Solution():
    def longestCommonPrefix(self, strs):

        prefix=strs[0]

        for word in strs[1:]:

            while not word.startswith(prefix):
                prefix=prefix[:-1]

                if prefix =="":
                    return ""
        return prefix

#Approach-
#Take the first word as the initial prefix.Compare it with every remaining word.
#If the current word does not start with the prefix,keep reducing the prefix by Removing the last character.
#if No common prefix exists. return empty
#Return the final common prefix.

#Time Complexity- O(n × m)
#n = number of strings
#m = length of shortest string

#Space Complexity- O(1)