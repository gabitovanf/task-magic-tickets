import sys

sys.path.append('./tester')

from TestingInstanceInterface import TestingInstanceInterface

class SolverTestingAdapter(TestingInstanceInterface):
    def __init__(self, instanceOrClass):
        self.instanceOrClass = instanceOrClass

    def compute(self, *input) -> str:
        #super(SolverTestingAdapter, self).compute(*input)

        return 'invalide something'

    def instanceClassName(self) -> str:
        return self.instanceOrClass.__class__.__name__

        