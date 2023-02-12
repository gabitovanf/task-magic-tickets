import time

class TestingInstanceInterface:
    def compute(self, *input) -> str:
        print(input, type(input))
        pass

    def validate(self, *input, output:str = '') -> dict:
        starttime = time.time()
        computed = self.compute(*input)

        return { "valid": computed == output, "computed": computed, "expected": output, "seconds": time.time() - starttime, "input": list(input) }

    def instanceClassName(self) -> str:
        pass

