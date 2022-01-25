class Solution:
    MAXI = (1 << 31) - 1
    MINI = -MAXI - 1
    
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0: return 0
        
        sign, index = 1, 0
        if s[0] == '-' or s[0] == '+':
            sign = -1 if s[0] == '-' else 1
            index = 1
        
        num = ""
        while index < len(s):
            if '0' <= s[index] and s[index] <= '9':
                num += s[index]
            else:
                break
            index += 1
            
        if len(num) == 0:   return 0
        res = int(num) * sign
        if res > self.MAXI:     return self.MAXI
        elif res < self.MINI:   return self.MINI
        return res