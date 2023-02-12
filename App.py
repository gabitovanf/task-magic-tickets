import sys

sys.path.append('./tester')
sys.path.append('./solver')

from Tester import Tester
from LookOverSolver import LookOverSolver
from SolverTestingAdapter import SolverTestingAdapter

#mode:
#    1 - complete looking over the combinations
#    2 - looking over except the last iteration substituted by remainder checking
tester = Tester(SolverTestingAdapter(LookOverSolver(mode = 2)))

# tester.testdir('./tests/one', './report/one.report.02.txt')
tester.testdir('./tests/1.Tickets', './report/1.Tickets.report.02.txt')
