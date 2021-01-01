#Given two strings s and t , write a function to determine if t is an anagram of s.

#Solution 1 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Initialize a list of length 26 filled with 0s
        #let a map to 0, b map to 1... z map to 25
        charList = [0]*26
        
        #if the two strings differ in length, return false
        if len(s) != len(t):
            return False
        
        #for each letter in the string
        for letterIndex in range(len(s)):
            #add one to the corresponding letter index if it is in string s
            charList[ord(s[letterIndex])-97] = charList[ord(s[letterIndex])-97] + 1
            
            #subtract one to the corresponding letter index if it is in string t
            charList[ord(t[letterIndex])-97] = charList[ord(t[letterIndex])-97] - 1
        
        #if the letter frequencies do not differ, return True
        if charList == [0]*26:
            return True
        else:
            False

#Solution 2

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Initialize a list of length 26 filled with 0s
        #let charList[i] store the frequency of a unique letter from a to z
        #index 0 to 25
        
        charList = [0]*26
        
        #if the two strings differ in length, return false
        if len(s) != len(t):
            return False
        
        #for each letter in the string s
        for letterIndex in range(len(s)):
            charList[ord(s[letterIndex])-97] = charList[ord(s[letterIndex])-97] + 1
            
        for letterIndex in range(len(t)):
            charList[ord(t[letterIndex])-97] = charList[ord(t[letterIndex])-97] - 1
            if charList[ord(t[letterIndex])-97] < 0:
                return False
        return True
            
        
            
