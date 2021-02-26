class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if (x >= -2,147,483,648 and x <= 2,147,483,647):
            if x < 0:
                x = abs(x)
                x_str = str(x)
                rev_x_str = x_str[::-1]
                neg_str = '-'+rev_x_str
                rev_x = int(neg_str)
            elif x > 0: 
                x_str = str(x)
                rev_x_str = x_str[::-1]
                rev_x_str = rev_x_str.lstrip('0')
                rev_x = int(rev_x_str)
            else:
                rev_x=0
            if (rev_x >= -2147483648 and rev_x <= 2147483647):
                return rev_x
            else:
                return 0
        else:
            return 0

res = Solution().reverse(1534236469)
print res
