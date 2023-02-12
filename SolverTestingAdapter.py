import sys

sys.path.append('./tester')

from TestingInstanceInterface import TestingInstanceInterface

class SolverTestingAdapter(TestingInstanceInterface):
    def __init__(self, instanceOrClass):
        self.instanceOrClass = instanceOrClass

    def compute(self, *input) -> str:
        try:
            firstInputVal = input[0]
            firstInputVal = int(firstInputVal)
            computed = self.instanceOrClass.compute(firstInputVal)
        except ValueError as e:
            computed = 'Invalid input data'
            print(e)

        except AttributeError as e:
            computed = 'Instance or class passed is invalid: it must contain a method .compute(inputValue:int)'
            print(e)
            
        except Exception as e:
            computed = 'Unknown exception occured'
            print(e)

        return str(computed)

    def instanceClassName(self) -> str:
        return self.instanceOrClass.__class__.__name__

        