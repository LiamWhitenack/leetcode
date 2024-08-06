from typing import List, Tuple


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        steps_starts = {0: 0}
        steps_reach = {0: 0}
        target = len(nums) - 1

        if len(nums) == 0:
            return True
        if len(nums) == 1:
            return True

        count_steps = 0
        while steps_starts:
            start = steps_starts.get(count_steps)
            if start is None:
                return False

            steps_reach[count_steps + 1] = 0

            start_value = nums[start:][0]
            for i in range(start_value, 0, -1):
                if i + start >= target:
                    return True
                lands_on_value = nums[i + start]
                reach = i + start + lands_on_value
                if start + i >= target:
                    return True

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
        TestCase(input=[2, 3, 1, 1, 4], output=True),
        TestCase(input=[3, 2, 1, 0, 4], output=False),
    ]

    for test_case in test_cases:
        if test_case.output != (output := Solution().canJump(test_case.input)):
            print(test_case, output)
