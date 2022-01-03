class MedianFinder:
    PLUS = 100000
    MAX_LEVEL = 18
    
    def __init__(self):
        self.sum = []
        for i in range(self.MAX_LEVEL + 1):
            self.sum.append([0] * pow(2, i))
        self.update = {}
        

    def addNum(self, num: int) -> None:
        if num in self.update:
            self.update[num + self.PLUS] += 1
        else:
            self.update[num + self.PLUS] = 1        

    def updateAll(self) -> None:
        level = self.MAX_LEVEL
        while len(self.update) > 0:
            newDict = {}
            for key, value in self.update.items():
                self.sum[level][key] += value
                parent = key // 2
                if level > 0:
                    if parent in newDict:
                        newDict[parent] += value
                    else:
                        newDict[parent] = value
            level -= 1
            self.update = newDict

    def findMedian(self) -> float:
        self.updateAll()

        level, index = 0, 0
        remain = (self.sum[0][0] // 2) + 1
        while level < self.MAX_LEVEL:
            leftParent = index * 2
            left = self.sum[level + 1][leftParent]
            
            if left < remain:
                remain -= left
                index = leftParent + 1
            else:
                index = leftParent
            level += 1
        res = index - self.PLUS
            
        if self.sum[0][0] % 2 == 0:
            return res - 0.5
        else:
            return res


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()