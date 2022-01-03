from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        smallest = [-1] * len(nums)
        maxi = 0;
        for n in nums:
            left = 0
            right = maxi
            while left < right:
                mid = left + ( (right - left) >> 1)
                if smallest[mid] < n:
                    left = mid + 1
                else:
                    right = mid
            
            smallest[left] = n

            if left == maxi:
                maxi += 1;

        return maxi


if __name__ == "__main__":
    sol = Solution()
    print (sol.lengthOfLIS([10,9,2,5,3,7,101,18]))
        