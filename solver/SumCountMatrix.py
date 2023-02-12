from math import ceil, floor
import copy

class SumCountMatrix:

    ZERO_ZERO = [1]

    def __init__(self, sumCountList:list = []):
        self.sumCountList =sumCountList

    def empty(self):
        return len(self.sumCountList.keys()) < 1

    def fromList(self, inputList:list, numSumValuesToExtend:int = 0):

        inputLength = len(inputList)
        inputMaxSum = inputLength - 1

        totalSum = inputMaxSum + numSumValuesToExtend # is the last index also
        centerIndex = floor(totalSum / 2)

        newDict = {}
        newList = [0] * (totalSum + 1)

        count = 0

        for i in range(centerIndex + 1):
            if (i < inputLength):
                count += inputList[i]

            subI = i - numSumValuesToExtend - 1
            if (subI > -1 and subI < inputLength):
                count -= inputList[subI]

            newList[i] = count
            newList[totalSum - i] = count
        
        print(newList)

        self.sumCountList = newList

        return self

    def fromZero(self):
        self.sumCountList = copy.copy(SumCountMatrix.ZERO_ZERO)

        return self

    def list(self) -> list:
        return self.sumCountList

    def extendWith(self, numSumValuesToExtend:int = 9):
        return self.fromList(self.sumCountList, numSumValuesToExtend)


    def getSquareValue(self):
        """
        Returns a sum of square of each element in list
        """
        inList = self.sumCountList

        inputLength = len(inList)
        centerIndex = ceil(inputLength / 2) - 1
        isCenterEven = inputLength % 2 == 0

        sum = 0
        curIndex = centerIndex
        curVal = inList[centerIndex]

        if (isCenterEven):
            sum += 2 * (curVal ** 2)
        else:
            sum += curVal ** 2

        while curIndex > 0:
            curIndex -= 1
            curVal = inList[curIndex]
            sum += 2 * (curVal ** 2)

        return sum




