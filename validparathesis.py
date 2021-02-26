class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        flag = 0
        list1 = ['{}','()','[]']
        s1 = s
        while True:
            for ele in list1:
                print ele
                print s
                if str(ele) in s:
                    s = s.replace(ele,"")
                    flag = 1
            if s == "" and flag == 1: 
                break;
            if flag == 0:
                print "String is not a valid paranthesis: "+str(s1)
                break;

        if flag == 0:
            return False
        else:
            return True
                    
                
                
res = Solution().isValid("()")
print res
