from typing import List, Literal, Tuple


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        self.my_grid: List[List[int]] = [[] for _ in grid] + [[] for _ in grid] + [[] for _ in grid]  # type: ignore[assignment]

        for i, row in enumerate(grid):
            cell: Literal["/", "\\", " "]
            for j, cell in enumerate(row):  # type: ignore[assignment]
                if cell == "/":
                    self.my_grid[i * 3][j * 3 + 2] = -1
                    self.my_grid[i * 3 + 1][j * 3 + 1] = -1
                    self.my_grid[i * 3 + 2][j * 3 + 0] = -1
                if cell == "\\":
                    self.my_grid[i * 3][j * 3 + 0] = -1
                    self.my_grid[i * 3 + 1][j * 3 + 1] = -1
                    self.my_grid[i * 3 + 2][j * 3 + 2] = -1

        max_color = 3
        n = len(grid)
        # apply flood fill with m as color till entire grid is not colored
        for i in range(n * 3):
            for j in range(n * 3):
                if self.my_grid[i][j] == 0:
                    max_color += 1
                    self.floodfill(self.my_grid, i, j, max_color)

        return max_color

    def floodfill(self, grid, r, c, color):
        # Check for out-of-bounds or already colored cells
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != 0:
            return

        # Color the cell
        grid[r][c] = color

        # Flood fill in all four directions
        self.floodfill(grid, r - 1, c, color)
        self.floodfill(grid, r + 1, c, color)
        self.floodfill(grid, r, c - 1, color)
        self.floodfill(grid, r, c + 1, color)


def num_sections(grid: List[List[Literal[0, 1]]]) -> int:
    count = 0

    zero_positions = []

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 0:
                zero_positions.append((i, j))

    while zero_positions:
        zero_position = zero_positions[0]
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        neighbors = [
            add_tuples(zero_position, move)
            for move in moves
            if add_tuples(zero_position, move) in zero_positions
        ]
        if len(neighbors) == 0:
            zero_positions.remove(zero_position)
            count += 1
            continue
        seen = {neighbors[-1]}
        while neighbors:
            neighbor = neighbors.pop()
            for move in moves:
                neighbor_position = add_tuples(move, neighbor)
                if (
                    neighbor_position in zero_positions
                    and neighbor_position not in seen
                ):
                    seen.add(neighbor_position)
                    neighbors.append(neighbor_position)
        for position in seen:
            zero_positions.remove(position)
        count += 1

    return count


def add_tuples(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
    return (a[0] + b[0], a[1] + b[1])


print(Solution().regionsBySlashes(["//", "/ "]))
