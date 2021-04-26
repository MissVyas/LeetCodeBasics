class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if haystack == needle and haystack=="":
            return 0
        elif haystack == needle:
            return 0
        elif haystack.__contains__(needle):
            return haystack.index(needle)
        else:
            return -1
