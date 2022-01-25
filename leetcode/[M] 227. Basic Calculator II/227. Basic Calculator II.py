from typing import List

class Solution:
    def insert(self, stack:list, num:int):
        stack.append(int(num))
        if len(stack) >= 3 and stack[-2] in ["*", "/"]:
            num2 = stack.pop(); op = stack.pop(); num1 = stack.pop()
            if op == '*':   stack.append(num1 * num2)
            else:           stack.append(num1 // num2)
        
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = []
        num = ""
        for ch in s:
            if ch in ["+", "-", "*", "/"]:
                self.insert(stack, int(num))
                stack.append(ch)
                num = ""
            else: num = num + ch
        self.insert(stack, int(num))
        res = stack[0]
        for i in range(1, len(stack), 2):
            if stack[i] == "+":   res = res + int(stack[i+1])
            else:                 res = res - int(stack[i+1])
        return res
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.calculate(" 3+5 / 2 "))