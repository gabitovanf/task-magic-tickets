from SolverInterface import SolverInterface

class LookOverSolver(SolverInterface):
    
    @staticmethod 
    def solve(numDigits:int, mode:int = 1) -> int:
        if (mode == 1):
            return LookOverSolver._solve(numDigits)
        return LookOverSolver._checkingRemainderIncrement(numDigits, numDigits)

    @staticmethod
    def _solve(remainingDigits:int, sumA:int = 0, sumB:int = 0) -> int:
        if (remainingDigits <= 0):
            if (sumA == sumB): 
                return 1
            return 0

        count = 0

        for a in range(10):
            for b in range(10):
                increment = LookOverSolver._solve(remainingDigits - 1, sumA + a, sumB + b)
                count += increment

        return count

    @staticmethod
    def _checkingRemainderIncrement(numDigits:int, iteration:int, sumA:int = 0) -> int:
        if (iteration <= 0):
            return LookOverSolver._checkingRemainderDecrement(numDigits, sumA)

        count = 0

        for a in range(10):
            increment = LookOverSolver._checkingRemainderIncrement(numDigits, iteration - 1, sumA + a)
            count += increment

        return count

    @staticmethod
    def _checkingRemainderDecrement(iteration:int, remainder:int = 0) -> int:
        if (iteration <= 1):
            if (remainder > -1 and remainder < 10):
                return 1

            return 0

        count = 0

        for b in range(10):
            increment = LookOverSolver._checkingRemainderDecrement(iteration - 1, remainder - b)
            count += increment

        return count

    def __init__(self, mode:int = 1):
        """
        mode:
            1 - complete looking over the combinations
            2 - looking over except the last iteration substituted by remainder checking
        """
        self.mode = mode


    def compute(self, numDigits:int) -> int:
        return LookOverSolver.solve(numDigits, self.mode)

        
