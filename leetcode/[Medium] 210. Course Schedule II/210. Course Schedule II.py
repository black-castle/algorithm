from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        incoming = [0] * numCourses
        outgoing = [ [] for key in range(numCourses)]
        
        for pre in prerequisites:
            incoming[pre[0]] = incoming[pre[0]] + 1
            outgoing[pre[1]].append(pre[0])
        
        res = []    
        queue = [i for i, n in enumerate(incoming) if n == 0]
        while len(queue) > 0:
            here = queue.pop(0)
            res.append(here)
            for next in outgoing[here]:
                incoming[next] = incoming[next] - 1
                if incoming[next] == 0: queue.append(next)
                
        for n in incoming:
            if n > 0: return []   
            
        return res
        
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.findOrder(2, [[1,0]]))
    print(sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
    print(sol.findOrder(3, [[1,0],[1,2],[0,1]]))