from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        res = list()
        arr.sort()
        mini = 987654321
        for i in range(1, len(arr)):
            gap = arr[i] - arr[i-1]
            if gap < mini:
                mini = gap
                res.clear()
                res.append(list([arr[i-1], arr[i]]))
            elif gap == mini:
                res.append(list([arr[i-1], arr[i]]))
                
        return res
        
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumAbsDifference([1,3,6,10,15]))