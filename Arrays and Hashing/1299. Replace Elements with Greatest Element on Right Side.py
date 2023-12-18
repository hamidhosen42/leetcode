from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max_right = -1

        for i in range(n - 1, -1, -1):
            current_value = arr[i]
            arr[i] = max_right
            max_right = max(max_right, current_value)

        return arr

# Example usage:
obj = Solution()
print(obj.replaceElements([17, 18, 5, 4, 6, 1]))  # Output: [18, 6, 6, 6, 1, -1]
