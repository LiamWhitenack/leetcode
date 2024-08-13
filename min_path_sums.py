from typing import List, Set


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        positions = {(0, 0): grid[0][0]}
        m = len(grid)
        n = len(grid[0])

        costs: Set[int] = set()

        while positions:

            (i, j), cost = list(positions.items())[0]
            del positions[(i, j)]
            if (i, j) == (m - 1, n - 1):
                costs.add(cost)
                continue

            down = (i + 1, j)
            right = (i, j + 1)

            if i < m - 1:
                if down in positions:
                    positions[down] = min([cost + grid[i + 1][j], positions[down]])
                else:
                    positions[down] = cost + grid[i + 1][j]
            if j < n - 1:
                if right in positions:
                    positions[right] = min([cost + grid[i][j + 1], positions[right]])
                else:
                    positions[right] = cost + grid[i][j + 1]

        return min(costs)


print(Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
