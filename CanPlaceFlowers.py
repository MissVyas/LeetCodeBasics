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
            #print "i="+str(i)
            if i == 0:
                #print "At the start of plot"
                nextplot = flowerbed[i+1]
                currentplot = flowerbed[i]
                #print "nextplot: " + str(nextplot)
                #print "currentplot: " + str(currentplot)
                if (currentplot == nextplot) and currentplot == 0:
                    count += 1
                    flowerbed[i] = 1
                    #print flowerbed
            elif i == (plots-1):
                #print "At the end of plot"
                prevplot = flowerbed[i-1]
                currentplot = flowerbed[i]
                #print "prevplot: " + str(prevplot)
                #print "currentplot: " + str(currentplot)
                if (currentplot == prevplot) and currentplot == 0:
                    count += 1
                    flowerbed[i] = 1
                    #print flowerbed
            else:
                nextplot = flowerbed[i+1]
                prevplot = flowerbed[i-1]
                currentplot = flowerbed[i]

                if currentplot == 0:
                    #print "nextplot: "+str(nextplot)
                    #print "prevplot: "+str(prevplot)
                    #print "currentplot: "+str(currentplot)
                    if nextplot == 0 and prevplot == 0:
                        count += 1
                        flowerbed[i] = 1
                        #print flowerbed
            i += 1

        ##print list1
        ##print flowerbed

        if count >= n:
            return True
        else:
            return False
res = Solution().canPlaceFlowers([1],0)
print res
