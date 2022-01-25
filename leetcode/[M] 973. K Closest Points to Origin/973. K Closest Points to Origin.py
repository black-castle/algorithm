from typing import List

from heapq import *

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) <= k:
            return [points[i] for i in range(len(points))]
        
        heap = []
        for x,y in points:
            heappush(heap, [x ** 2 + y ** 2, [x,y]])
        return [heappop(heap)[1] for _ in range(k)]


if __name__ == "__main__":
    sol = Solution()
    print(sol.kClosest([[1,3],[-2,2],[2,-2]], k = 2))