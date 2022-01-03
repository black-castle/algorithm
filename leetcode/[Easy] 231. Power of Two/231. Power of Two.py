class Solution:
    cases = set([pow(2,x) for x in range(32)])
    
    def isPowerOfTwo(self, n: int) -> bool:
        if n in Solution.cases:
            return True
        else:
            return False
    
    
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPowerOfTwo(3))