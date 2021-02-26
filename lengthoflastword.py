class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = int(len(s))
        if l > 0:
            listofs = s.split()
            if len(listofs) > 0:
                lastword = listofs[len(listofs)-1]
                length = len(lastword)
                return length
            else:
                return 0
        else:
            return 0

pal = Solution().lengthOfLastWord("Hello this is me")
print pal
val = Solution().lengthOfLastWord(" ")
print val
