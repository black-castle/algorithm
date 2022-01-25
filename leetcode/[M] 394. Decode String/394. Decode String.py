class Solution:
    def decodeString(self, s: str) -> str:
        if s.isalpha():
            return s
        
        res = ""
        index = 0
        while index < len(s) :
            if s[index].isdigit():
                start = s.find('[', index)
                cnt = s[index:start]
                index = start

                bracket = 0
                while index < len(s):
                    if s[index] == '[':
                        bracket = bracket + 1
                    elif s[index] == ']':
                        bracket = bracket - 1
                        if bracket == 0: break
                    index = index + 1
                res = res + int(cnt) * self.decodeString(s[start +1: index])
            else:
                res = res + s[index]
            index = index + 1
        return res
    
if __name__ == "__main__":
    sol = Solution()
    # print(sol.decodeString("3[a]2[bc]"))
    print(sol.decodeString("3[a2[c]]"))
    print(sol.decodeString("2[abc]3[cd]ef"))