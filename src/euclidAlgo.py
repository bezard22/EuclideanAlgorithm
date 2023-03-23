class EuclideanAlgorithm:
    def __init__(self) -> None:
        self.resetSteps()
    
    def resetSteps(self) -> None:
        self.steps = []
    
    def explanation(self) -> str:
        expStr = ""
        for step in self.steps:
            expStr += f"{step[0]} = {step[1]} * {step[2]} + {step[3]}\t"
            expStr += f"| gcd({step[0]}, {step[1]}) = gcd({step[1]}, {step[3]})\n"
        expStr += f"gcd({self.steps[0][0]}, {self.steps[0][1]}) = {self.steps[-1][1]}"
        return expStr

    def gcd(self, r0: int, r1: int) -> int:
        self.resetSteps()
        while r1 > 0:
            self.steps.append((r0, r1, int(r0 / r1), r0 % r1))
            r1, r0 = r0 % r1, r1
        return r0