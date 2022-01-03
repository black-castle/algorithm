class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        numArr1 = [0] * 128
        numArr2 = [0] * 128
        
        last = 1
        for i in range(len(s)):
            index1 = ord(s[i])
            index2 = ord(t[i])

            value1 = numArr1[index1]
            value2 = numArr2[index2]

            if value1 != 0 and value2 != 0:
                if value1 != value2:
                    return False
            elif value1 == 0 and value2 == 0:
                numArr1[index1] = last
                numArr2[index2] = last
                last += 1
            else:
                return False

        return True;

if __name__ == "__main__":
    sol = Solution()
    print (sol.isIsomorphic('abb', 'bbc'))
