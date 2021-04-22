class Solution():
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        # Get the number of plots
        plots = len(flowerbed)

        # If there is only one plot and 1 flower to place
        if plots == 1 and n == 1:
            if flowerbed[0] == 0:
                return True
            else:
                return False

        # If there is no flower to place for one single slot
        if n == 0 and plots == 1:
            return True

        # To  Keep a count of plot we can place
        count = 0

        # loop
        i = 0


        while i < plots:
            if i == 0:
                # At the start of plot
                nextplot = flowerbed[i+1]
                currentplot = flowerbed[i]
                if (currentplot == nextplot) and currentplot == 0:
                    count += 1
                    flowerbed[i] = 1
            elif i == (plots-1):
                #At the end of plot
                prevplot = flowerbed[i-1]
                currentplot = flowerbed[i]
                if (currentplot == prevplot) and currentplot == 0:
                    count += 1
                    flowerbed[i] = 1
            else:
                nextplot = flowerbed[i+1]
                prevplot = flowerbed[i-1]
                currentplot = flowerbed[i]

                if currentplot == 0:
                    if nextplot == 0 and prevplot == 0:
                        count += 1
                        flowerbed[i] = 1
            i += 1

        if count >= n:
            return True
        else:
            return False

res = Solution().canPlaceFlowers([1],0)
print res
