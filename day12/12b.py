with open('day12.in') as f:
    lines = f.read().splitlines()

pos = [0, 0]
wp = [10, 1]
dirs = { "N": [0, 1], "S": [0, -1], "E": [1, 0], "W": [-1, 0] }

for line in lines:
    instr = line[0]
    val = int(line[1:])

    if instr in ["L", "R"]:
        # Rotate waypoint
        val = val // 90
        if instr == "L":
            for i in range(val):
                x = -wp[1]
                y = wp[0]
                wp = [x, y]
        else:
            for _ in range(val):
                x = wp[1]
                y = -wp[0]
                wp = [x, y]
    elif instr == "F":
        pos[0] += wp[0] * val
        pos[1] += wp[1] * val
    else:
        wp[0] += dirs[instr][0] * val
        wp[1] += dirs[instr][1] * val

manhattan = abs(pos[0]) + abs(pos[1])
print(f"Day 12 Part 2: { manhattan }")
