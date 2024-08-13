from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        positions = {(0, 0): 1}
        disallowed_positions = {
            (i, j)
            for i, row in enumerate(obstacleGrid)
            for j, val in enumerate(row)
            if val > 0
        }
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        counter = 0

        if obstacleGrid[m - 1][n - 1] or obstacleGrid[0][0]:
            return 0

        while positions:

            (i, j), num_paths = list(positions.items())[0]
            del positions[(i, j)]
            if (i, j) == (m - 1, n - 1):
                counter += num_paths
                continue

            down = (i + 1, j)
            right = (i, j + 1)

            if down not in disallowed_positions and i < m - 1:
                positions[down] = num_paths + positions.get(down, 0)
            if right not in disallowed_positions and j < n - 1:
                positions[right] = num_paths + positions.get(right, 0)

        return counter


Solution().uniquePathsWithObstacles(
    [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
)
