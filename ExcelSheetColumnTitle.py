class Solution(object):
    dict1 = {i: chr(i + 96) for i in range(1, 27)}
    dict1[0] = 'z'

    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """

        string1 = ""

        if columnNumber <= 26:
            string1 = self.dict1[int(columnNumber)] + string1
            return string1.upper()

        if columnNumber > 26:
            string1 = self.generateColumnTitle(columnNumber,string1)
            return string1.upper()

    def generateColumnTitle(self, columnNumber, title=''):
        # it considers that column number is greater than 26

        dividend = columnNumber / 26
        reminder = columnNumber % 26

        # remaining reminder is the character value from right. Read title from right to left
        title = str(self.dict1[reminder]) + title

        if dividend > 26 and reminder != 0:
            # when dividend is not exactly divisible
            self.generateColumnTitle(dividend, title)
        elif dividend > 26 and reminder == 0:
            # when dividend is exactly divisible; and reminder is zero it means you have reached to letter Z
            title = str(self.dict1[26])+title
            return title
        elif 1 <= dividend <= 26 and reminder != 0:
            # when dividend is less than 26 and reminder is not zero it means you can directly add dividend value.
            # since you already added reminder earlier. and you can't divide the number further
            title = str(self.dict1[dividend]) + title
            return title
        elif 2 <= dividend <= 26 and reminder == 0:
            # when divided is less than 26 and reminder is zero
            title = str(self.dict1[dividend-1]) + title
            return title
        else:
            return title

        return self.generateColumnTitle(dividend,title)

res = Solution().convertToTitle(702)
print res

# Approach

#27 ---> div+rem
#501 ---> div+rem+rem+rem
#until div comes in range of 1-26
