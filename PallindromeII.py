class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        slen = len(s)
        i = 0

        if s == s[::-1]:
            return True
        else:
            while i < slen:
                test = list(s)
                test.pop(i)
                str_new = ""
                str_new = str_new.join(test)
                if str_new == str_new[::-1]:
                    return True
                else:
                    i = i + 1
                    continue
            return False

res = Solution().validPalindrome("cbbcc")
print res
