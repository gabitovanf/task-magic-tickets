import sys

sys.path.append('./tester')

from Tester import Tester
from SolverTestingAdapter import SolverTestingAdapter

tester = Tester(SolverTestingAdapter([0]))

tester.testdir('./tests/1.Tickets')
