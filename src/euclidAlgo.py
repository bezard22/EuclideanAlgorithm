class EuclideanAlgorithm:
    def __init__(self) -> None:
        self.resetSteps()
    
    def resetSteps(self) -> None:
        self.steps = []

    def gcd(self, r0: int, r1: int) -> int:
        self.resetSteps()
        while r1 > 0:
            self.steps.append((r0, r1, int(r0 / r1)))
            r1, r0 = r0 % r1, r1
        self.steps.append((r0, r1))
        return r0