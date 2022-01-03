from typing import List

class Solution:
    def isExist(self, nums1: List[int], nums2: List[int], size: int) -> bool:
        checkSet = set()
        token = ''.join([chr(x) for x in nums1[:size]])
        checkSet.add(hash(token))
        for i in range(size, len(nums1)):
            token = token[1:] + chr(nums1[i])
            checkSet.add(hash(token))
        
        query = ''.join([chr(x) for x in nums2[:size]])
        if hash(query) in checkSet:
            return True
        for i in range(size, len(nums2)):
            query = query[1:] + chr(nums2[i])
            if hash(query) in checkSet:
                return True

        return False

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        left, right = 1, min(len(nums1), len(nums2))
        while left <= right :
            mid = left + ((right - left) >> 1)
            if self.isExist(nums1, nums2, mid):
                res = mid
                left = mid + 1
            else:
                right = mid -1

        return res


if __name__ == "__main__":
    sol = Solution()
    print (sol.findLength([1,2,3,2,1], [3,2,1,4,7]))