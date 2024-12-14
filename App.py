import sys

sys.path.append('./tester')
sys.path.append('./solver')

from Tester import Tester
from LookOverSolver import LookOverSolver
from SumCountMatrix import SumCountMatrix
from SumMatricesSolver import SumMatricesSolver
from SolverTestingAdapter import SolverTestingAdapter


reportTrueDetails = """
    ----
    Количество разрядов N: {input}
    Количество счастливых 2N-значных билетов: {computed}
    ----
"""

reportFalseDetails = """
    ----
    Количество разрядов N: {input}

    Количество счастливых 2N-значных билетов
    - ожидаемое: {expected}
    - расчетное: {computed}
    ----
"""

# faster
tester0 = Tester(SolverTestingAdapter(SumMatricesSolver()))

#mode:
#    1 - complete looking over the combinations
#    2 - looking over except the last iteration substituted by remainder checking
tester1 = Tester(SolverTestingAdapter(LookOverSolver(mode = 1)))
tester2 = Tester(SolverTestingAdapter(LookOverSolver(mode = 2)))

tester0.setupReportStrings(reportTrueDetails = reportTrueDetails, reportFalseDetails = reportFalseDetails)
tester1.setupReportStrings(reportTrueDetails = reportTrueDetails, reportFalseDetails = reportFalseDetails)
tester2.setupReportStrings(reportTrueDetails = reportTrueDetails, reportFalseDetails = reportFalseDetails)

# tester0.testdir('./tests/1.Tickets', './report/1.Tickets.report.SumMatricesSolver.01.txt')
tester1.testdir('./tests/1.Tickets', './report/1.Tickets.report.LookOverSolver.m1.01.txt')
# tester2.testdir('./tests/1.Tickets', './report/1.Tickets.report.LookOverSolver.m2.02.txt')
# tester0.testdir('./tests/one', './TEMP.txt')

