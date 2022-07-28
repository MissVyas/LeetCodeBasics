import itertools
class Solution(object):
    def isLongPressedName(self, name, typed):

        # lets get the group by letter for both the name and type.
        g1 = self.groupbyletters(name)
        g2 = self.groupbyletters(typed)

        len_g1 = len(g1)
        len_g2 = len(g2)

        # Validate the strings are not same eg: alexxxx and alexxaaan
        if len_g1 != len_g2:
            return False

        # Validate the values in set
        for t1, t2 in zip(g1, g2):
            print t1
            print t2


    def groupbyletters(self,string1):
        len1 = len(string1)
        i = 0
        list1 = []
        while i != len1-1:
            j = i
            count = 0
            while j <= len1:
                if j == len1 or string1[i] != string1[j]:
                    if i == len1-1:
                        list1.append((string1[i], count+1))
                    else:
                        list1.append((string1[i], count))
                    i = j
                    break
                count += 1
                j = j+1
                continue
        return list1

res = Solution().groupbyletters("alex")
print res