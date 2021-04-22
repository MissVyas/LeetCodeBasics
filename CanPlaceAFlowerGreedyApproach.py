class Solution():
    def  canPlaceFlowers(self,flowerbed, n):
        """

        :param flowerbed: List[int]
        :param n: int
        :return: Boolean
        """

        count = 0
        i=0
        while i < len(flowerbed):
            is_flower = flowerbed[i]
            if not is_flower: #Empty Plot
                cond = is_flower
                if i>0:
                    cond = cond or flowerbed[i-1]
                if i < len(flowerbed) - 1 :
                    cond = cond or flowerbed[i+1]
                if not cond:
                    count += 1
                    i += 2
                else:
                    i += 1
            else:
                i += 1

        return count >= n

res = Solution().canPlaceFlowers([1,0,0,1,0,0,0,1,0,0],2)
print res