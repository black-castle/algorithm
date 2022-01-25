import heapq

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ch2rank = {}
        rank2ch = {}

        rank = 1
        for c in order:
            ch2rank[c] = rank
            rank2ch[rank] = c
            rank += 1
        
        heap = []
        for ch in s:
            if ch not in ch2rank:
                ch2rank[ch] = rank
                rank2ch[rank] = ch
                rank += 1
            heapq.heappush(heap, ch2rank[ch])

        res = ''
        while heap:
            res += rank2ch[heapq.heappop(heap)]
        return res

if __name__ == "__main__":
    sol = Solution()
    print (sol.customSortString("cba", "abcd"))
            