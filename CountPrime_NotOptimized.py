class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 and n == 1:
            return 0

        list1 = range(2, n + 1)
        for i in list1:
            #print i
            if i == 0:
                continue
            for j in list1:
                #print j
                if j == i:
                    continue
                if int(j) >= int(i) and j != 0:
                    #print str(j)+"/"+str(i)
                    if int(j) % int(i) == 0 or int(j) == int(i) ** 2:
                        idx = list1.index(j)
                        list1[int(idx)] = 0

        #print list1

        count = 0
        for char1 in list1:
            if char1  != 0:
                count += 1
        return count


res = Solution().countPrimes(10)
print res
