from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = list()
        intervals.sort()
        i = 0
        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]
            i = i + 1
            while i < len(intervals):
                if intervals[i][0] <= end:
                    end = max(end, intervals[i][1])
                    i = i + 1
                else:
                    break
            res.append(list([start, end]))
        return res
    
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))