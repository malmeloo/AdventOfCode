import aoc

input_data = aoc.get_input()
num_grid = [[int(num) for num in row] for row in input_data]

large_grid = [[0] * len(num_grid[0]) * 5 for _ in range(len(num_grid) * 5)]

for _x in range(len(num_grid[0]) * 5):
    for _y in range(len(num_grid) * 5):
        y_val = _y % len(num_grid)
        x_val = _x % len(num_grid)
        new_val = (num_grid[y_val][x_val] + _x // len(num_grid[0]) + _y // len(num_grid)) % 9
        if new_val == 0:
            new_val = 9

        large_grid[_y][_x] = new_val


def _neighbors(cell: tuple, grid):
    neigh = set()
    if cell[0] > 0:
        neigh.add((cell[0] - 1, cell[1]))
    if cell[0] < len(grid[0]) - 1:
        neigh.add((cell[0] + 1, cell[1]))
    if cell[1] > 0:
        neigh.add((cell[0], cell[1] - 1))
    if cell[1] < len(grid) - 1:
        neigh.add((cell[0], cell[1] + 1))

    return neigh


def _smallest_node(tent_dist, known_nodes):
    smallest_dist = 9999999
    smallest = None
    for node in known_nodes:
        if tent_dist[node] < smallest_dist:
            smallest_dist = tent_dist[node]
            smallest = node

    return smallest


def find_risk(grid):
    dest_node = (len(grid[0]) - 1, len(grid) - 1)
    known_nodes = {(0, 0)}

    unvisited = set((x, y) for x in range(len(grid[0])) for y in range(len(grid)))
    tent_dist = {node: 9999999 for node in unvisited}
    tent_dist[(0, 0)] = 0

    cur_node = (0, 0)
    while True:
        if cur_node == dest_node:
            return tent_dist[cur_node]

        for neighbor in _neighbors(cur_node, grid):
            new_dist = tent_dist[cur_node] + grid[neighbor[1]][neighbor[0]]
            if new_dist < tent_dist[neighbor]:
                tent_dist[neighbor] = new_dist
                known_nodes.add(neighbor)

        known_nodes.remove(cur_node)

        cur_node = _smallest_node(tent_dist, known_nodes)


aoc.run(lambda: find_risk(num_grid))
aoc.run(lambda: find_risk(large_grid))
