from pyparsing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        arr1 =[]
        ln = len(arr)-1

        for i in range(ln):
            arr2 = arr1.remove(arr1[i])
            mx = max(arr)
            

        return arr2

object = Solution()
print(object.replaceElements([17,18,5,4,6,1]))