from itertools import permutations
from math import factorial


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rights = m - 1
        downs = n - 1

        return len(
            set(
                list(
                    permutations(
                        [True for _ in range(rights)] + [False for _ in range(downs)]
                    )
                )
            )
        )


class TestCase:
    def __init__(self, m: int, n: int, output: int) -> None:
        self.input = m, n
        self.output = output

    def __repr__(self) -> str:
        return str(self.__dict__)


if __name__ == "__main__":
    test_cases = [
        TestCase(
            m=i,
            n=j,
            output=int(factorial(i + j - 2) / (factorial(i - 1) * factorial(j - 1))),
        )
        for i in range(1, 7)
        for j in range(1, 7)
    ]

    for test_case in test_cases:
        if test_case.output != (output := Solution().uniquePaths(*test_case.input)):
            print(test_case, output)
