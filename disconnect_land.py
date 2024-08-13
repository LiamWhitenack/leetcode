from typing import List, Literal, Set, Tuple


class Solution:
    def minDays(self, grid: List[List[int]]) -> Literal[0, 1, 2]:

        bridges = {
            (i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell
        }
        if not self.one_island(bridges.copy()):
            return 0
        num_land = sum([sum(row) for row in grid])
        if num_land <= 2:
            return num_land  # type: ignore[return-value]

        for bridge in bridges:
            # grid_copy[bridge[0]][bridge[1]] = 0
            if not self.one_island(bridges.symmetric_difference({bridge})):
                return 1

        return 2

    def one_island(self, land_positions: Set[Tuple[int, int]]) -> bool:
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


print(
    Solution().minDays(
        [[1, 1, 0, 1, 1], [1, 1, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 0, 1, 1]]
    )
)
