class Solution:
    def relativeSortArray(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()
        dict1 = {}

        for ele in A:
            if ele not in dict1:
                dict1[ele] = 1
            else:
                dict1[ele] += 1

        temp = []
        for ele in B:
            if ele in dict1.keys():
                temp.extend([ele for i in range(dict1[ele])])
                del dict1[ele]

        arr = []
        for key in dict1:
            for j in range(dict1[key]):
                arr.append(key)
        arr.sort()
        temp.extend(arr)
        return temp