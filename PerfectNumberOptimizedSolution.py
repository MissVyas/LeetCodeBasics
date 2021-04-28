class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        list1 = []
        if num == 1:
            return False

        sum1 = 0
        i = 1

        while i*i <= num:
            if num % i == 0:
                sum1 += i
                if i * i != num:
                    sum1 += num / i
            i += 1

        return sum1 - num == num

res = Solution().checkPerfectNumber(10)
print res
