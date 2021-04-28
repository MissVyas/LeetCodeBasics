import collections
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        dic1 = collections.Counter(deck)
        print dic1
        n = len(deck)
        for num in xrange(2,n+1):
            if n % num == 0:
                if all(v % num == 0 for v in dic1.values()):
                    return True
        return False

res = Solution().hasGroupsSizeX([1,1,2,2,2,2])
print res

######
#
#[1,1,1,2,2,2,3,3]
#[1]
#[1,1]
#[1,1,2,2,2,2]
######