import os
from TestingInstanceInterface import TestingInstanceInterface

class Tester:
    __reportHeader =  """
    ОТЧЁТ О ТЕСТИРОВАНИИ {className}
    Директория тестовых данных: 
    {dirpath}

    --------------

    """

    __reportItem = """
    {iterationName} - {result} - {seconds}сек

    """

    __reportTrueDetails = """
    ----
    Input: {input}
    ----
    """

    __reportFalseDetails = """
    ----
    Input: {input}
    Expected: {expected}
    Computed: {computed}
    ----
    """

    def __init__(self, instance: TestingInstanceInterface):
        self.instance = instance
        self.lastreport = ''

    def testdir(self, dirpath:str):
        # Store current location
        curdir = os.getcwd()

        os.chdir(dirpath)
        self.__startNewReport(os.getcwd())

        for filenamesDict in Tester.__getFilenamesDict(os.listdir()):
            iterationName = filenamesDict['in'][0:-3]
            fileContentDict = Tester.__readFiles(filenamesDict)

            # Continue if in- or out- has not been found 
            # or any other exeption raised
            if (fileContentDict == None): continue

            # Compute and compare result with out-file's content
            testResult = self.instance.validate(output = fileContentDict['out'], *fileContentDict['in'])

            self.__appendReportItem(iterationName, testResult)


        print(self.lastreport)

        # Set cwd back to current
        os.chdir(curdir)


    @staticmethod
    def __getFilenamesDict(dirAndFiles:list) -> list:
        filenameList = sorted(filter(lambda filename: filename.endswith('.in'), dirAndFiles))

        return list(map(lambda filename: { "in": filename, "out": filename[0:-3] + '.out' }, filenameList))

    @staticmethod
    def __readFiles(filenamesDict:dict) -> dict:
        fileContentDict = {}

        for (key, filename) in filenamesDict.items():
            try:
                with open(filename, 'r') as f:
                    if (key == 'out'):
                        content = f.readline()
                        content = content.strip()
                    else:
                        content = f.readlines()

                    fileContentDict[key] = content
            except Exception as e:
                fileContentDict = None
                print(e)
                break


        return fileContentDict

    def __startNewReport(self, dirpath:str):
        className = self.instance.instanceClassName()
        self.lastreport = Tester.__reportHeader.format(className=className, dirpath=dirpath)

    def __appendReportItem(self, iterationName, testResult):
        self.lastreport += (Tester.__reportItem
                .format(iterationName = iterationName, result = testResult['valid'], seconds = testResult['seconds']))

        if (testResult['valid'] == True):
            self.lastreport += (Tester.__reportTrueDetails
                .format(**testResult))
        else:
            self.lastreport += (Tester.__reportFalseDetails
                .format(**testResult))


