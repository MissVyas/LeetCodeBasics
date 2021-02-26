import re
class Solution:
    def isPalindrome(self, s: str) -> bool:

        #Converting string to lower case
        s = s.lower()

        #Checking if string is alphanumeric
        if s.isalnum():    
            rev = s[::-1]
        else:
            #Else converting it to alphanumeric and then reversing it
            # \W stands for AZ09az
            # _ for underscore
            # + is one or more occurences
            # [] a set of characters
            # re.sub('texttofindwithpattern','replacewithwhat',your_string)
            s = re.sub(r'[\W_]+', '', s)
            rev = s[::-1]

        #Comparing the reversed strings    
        if rev == s:
            return True
        else:
            return False
        
pal = Solution().isPalindrome("Hello")
print pal
pal2 = Solution().isPalindrome("121")
print pal2
