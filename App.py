import sys

sys.path.append('./tester')
sys.path.append('./solver')

from Tester import Tester
from SolverInterface import SolverInterface
from SolverTestingAdapter import SolverTestingAdapter

tester = Tester(SolverTestingAdapter(SolverInterface()))

tester.testdir('./tests/1.Tickets')
