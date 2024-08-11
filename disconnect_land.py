from typing import List, Literal, Tuple


class Solution:
    def minDays(self, grid: List[List[int]]) -> Literal[0, 1, 2]:
        if not self.one_island(grid):
            return 0
        num_land = sum([sum(row) for row in grid])
        if num_land <= 2:
            return num_land  # type: ignore[return-value]

        bridges = set()
        min_neighbors: Literal[0, 1, 2] = 2
        land_positions = {
            (i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell
        }
        for land_position in land_positions:
            i, j = land_position
            neighbor_directions = set()
            for direction, neighbor in enumerate(
                (
                    (i - 1, j),
                    (i + 1, j),
                    (i, j + 1),
                    (i, j - 1),
                )
            ):
                if neighbor in land_positions:
                    neighbor_directions.add(direction)
            if neighbor_directions == {2, 3} or neighbor_directions == {0, 1}:
                bridges.add(land_position)
            min_neighbors = min([min_neighbors, len(neighbor_directions)])  # type: ignore[list-item]

        for bridge in bridges:
            grid_copy = [
                [
                    cell if (i, j) != (bridge[0], bridge[1]) else 0
                    for j, cell in enumerate(row)
                ]
                for i, row in enumerate(grid)
            ]
            # grid_copy[bridge[0]][bridge[1]] = 0
            if not self.one_island(grid_copy):
                return 1

        return min_neighbors

    def one_island(self, grid: List[List[int]]) -> bool:
        land_positions = {
            (i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell
        }
        if not land_positions:
            return False
        search_spots = {land_positions.pop()}
        while True:
            land_position = search_spots.pop()
            i, j = land_position
            for neighbor in neighbors(i, j):
                if neighbor in land_positions:
                    search_spots.add(neighbor)
                    land_positions.remove(neighbor)
            if not search_spots:
                break

        return len(land_positions) == 0


def neighbors(i: int, j: int) -> List[Tuple[int, int]]:
    return [
        (i - 1, j),
        (i + 1, j),
        (i, j + 1),
        (i, j - 1),
    ]


print(Solution().minDays([[0, 0]]))
