import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        print "Your number: "+str(n)
        numbers = {}
        print "Outer loop: "+str(range(2, int(math.sqrt(n))+1))
        for p in range(2, int(math.sqrt(n))+1):
            print "My Dict: "+str(numbers)
            if p not in numbers:
                print "Considering number in range: "+str(p)
                print "Inner Loop: "+str(range(p*p, n,p))
                # Understand range here
                # range(no. to start, till the number, iterate value(either you want to iterate by two or three or any number))
                for multiple in range(p*p, n,p):
                    print "Multiple: "+str(multiple)
                    numbers[multiple] = 1

        print numbers
        # Exclude "1" and the number "n" itself
        return n - len(numbers) - 2
res = Solution().countPrimes(30)
print res
