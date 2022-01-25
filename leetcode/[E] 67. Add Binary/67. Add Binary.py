class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res, add = "", 0;
        a, b = a[::-1], b[::-1]
        for i in range(max(len(a), len(b))):
            sum = add
            if i < len(a):
                sum += 0 if a[i] == '0' else 1
            if i < len(b):
                sum += 0 if b[i] == '0' else 1
            
            res = ('0' if sum % 2 == 0 else '1') + res
            add = sum // 2;
            
        return '1' + res if add > 0 else res