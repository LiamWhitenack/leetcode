from typing import List, Tuple


class Solution:
    def jump(self, nums: List[int]) -> int:
        steps_starts = {0: 0}
        steps_reach = {0: 0}
        target = len(nums) - 1

        if len(nums) == 1:
            return 0

        count_steps = 0
        while steps_starts:
            start = steps_starts[count_steps]
            steps_reach[count_steps + 1] = 0

            start_value = nums[start:][0]
            for i in range(start_value, 0, -1):
                if i + start >= target:
                    return count_steps + 1
                lands_on_value = nums[i + start]
                reach = i + start + lands_on_value
                if start + i >= target:
                    return count_steps + 1

                if steps_reach[count_steps + 1] < reach:
                    steps_reach[count_steps + 1] = reach
                    steps_starts[count_steps + 1] = i + start

            count_steps += 1

        raise Exception()


class TestCase:
    def __init__(self, input: List[int], output: int) -> None:
        self.input = input
        self.output = output

    def __repr__(self) -> str:
        return str(self.__dict__)


if __name__ == "__main__":
    test_cases = [
        TestCase(input=[1, 1, 1, 1], output=3),
        TestCase(input=[1], output=0),
        TestCase(input=[2, 3, 1, 1, 4], output=2),
        TestCase(input=[2, 3, 0, 1, 4], output=2),
    ]

    for test_case in test_cases:
        if test_case.output != (output := Solution().jump(test_case.input)):
            print(test_case, output)
