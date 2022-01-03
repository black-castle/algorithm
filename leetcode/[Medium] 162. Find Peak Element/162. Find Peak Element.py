from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            if right - left == 1:
                return left if nums[left] > nums[right] else right

            mid = left + ((right - left) >> 1)

            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        
        return left


if __name__ == "__main__":
    sol = Solution()
    print (sol.findPeakElement([1,2,1]))
        