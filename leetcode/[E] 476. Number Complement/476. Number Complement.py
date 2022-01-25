import math

class Solution:
    p = [2**i for i in range(0,31)]
    def findComplement(self, num: int) -> int:
        mask = Solution.p[int(math.log(num * 2, 2))] - 1
        return ~num & mask
    
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.findComplement(2))
    print(sol.findComplement(5))
    print(sol.findComplement(1))