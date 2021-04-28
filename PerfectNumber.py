class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        list1 = []
        if num == 1:
            return False

        for i in range(1,num/2+1):
            if num%i == 0:
                list1.append(i)
        print list1
        return num == sum(list1)

res = Solution().checkPerfectNumber(28)
print res
