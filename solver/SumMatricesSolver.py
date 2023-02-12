from SolverInterface import SolverInterface
from SumCountMatrix import SumCountMatrix

class SumMatricesSolver(SolverInterface):

    @staticmethod
    def solve(numDigits:int) -> int:
        countMatrix = SumCountMatrix().fromZero()

        while numDigits > 0:
            countMatrix.extendWith(10 - 1)

            numDigits -= 1
            
        # print('LAST', countMatrix.list(), countMatrix.getSquareValue())

        return countMatrix.getSquareValue()

    def compute(self, numDigits:int) -> int:
        return SumMatricesSolver.solve(numDigits)