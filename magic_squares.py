from typing import List, Literal


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0
        for row_start in range(len(grid) - 2):
            for column_start in range(len(grid[0]) - 2):
                row_end = row_start + 3
                column_end = column_start + 3

                count += is_magic(
                    [
                        get_column(grid[row_start:row_end], k)
                        for k in range(column_start, column_end)
                    ]
                )

        return count


def get_column(grid: List[List[int]], i: int) -> List[int]:
    return [grid[0][i], grid[1][i], grid[2][i]]


def is_magic(grid: List[List[int]]) -> Literal[0, 1]:
    magic_sum = grid[0][0] + grid[1][1] + grid[2][2]
    if grid[2][0] + grid[1][1] + grid[0][2] != magic_sum:
        return 0
    for i in range(3):
        column = get_column(grid, i)
        row = grid[i]
        for e in column:
            if e > 9:
                return 0
        for e in row:
            if e > 9:
                return 0
        if sum(row) != magic_sum:
            return 0
        if sum(column) != magic_sum:
            return 0
    return 1


print(Solution().numMagicSquaresInside([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]))
