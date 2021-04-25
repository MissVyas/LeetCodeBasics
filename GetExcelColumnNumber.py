class Solution(object):
    dict1 = {chr(i + 96):i for i in range(1, 27)}

    def convertToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        columnTitle = columnTitle.lower()
        len1 = len(columnTitle)
        i = len1 - 1
        columnNumber = 0
        for char1 in columnTitle:
            val = self.dict1[char1]
            columnNumber = (val * (26 ** i)) + columnNumber
            i = i - 1

        return columnNumber

res = Solution().convertToNumber('FXSHRXW')
print res

# Approach

#27 ---> div+rem
#501 ---> div+rem+rem+rem
#until div comes in range of 1-26
