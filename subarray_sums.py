from typing import List, Tuple


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        left -= 1
        right -= 1
        sublists = []

        for start in range(n):
            for end in range(start + 1, n + 1):
                sublists.append(nums[start:end])

        return sum(sorted([sum(sublist) for sublist in sublists])[left : right + 1]) % (
            (10**9) + 7
        )


class TestCase:
    def __init__(
        self, nums: List[int], n: int, left: int, right: int, output: int
    ) -> None:
        self.nums = nums
        self.n = n
        self.left = left
        self.right = right
        self.output = output

    def __repr__(self) -> str:
        return str(self.__dict__)


if __name__ == "__main__":
    test_cases = [
        TestCase([1, 2, 3, 4], 4, 1, 5, 13),
        TestCase([1, 2, 3, 4], 4, 3, 4, 6),
        TestCase([1, 2, 3, 4], 4, 1, 10, 50),
    ]

    for test_case in test_cases:
        if test_case.output != (
            output := Solution().rangeSum(
                test_case.nums, test_case.n, test_case.left, test_case.right
            )
        ):
            print(test_case, output)
