class Solution:
    def containsDuplicate(self, nums) -> bool:
        duplicate =len(nums)
        unique = len(set(nums))

        if(duplicate == unique):
            return False
        else:
            return True
        
object = Solution()
print(object.containsDuplicate([2,3,1]))