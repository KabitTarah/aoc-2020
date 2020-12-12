with open('day12.in') as f:
    lines = f.read().splitlines()

pos = [0, 0]
dirs = { "N": [0, 1], "S": [0, -1], "E": [1, 0], "W": [-1, 0] }
direction = "E"
right = { "E": "S", "S": "W", "W": "N", "N": "E" }
left = { "E": "N", "N": "W", "W": "S", "S": "E" }


for line in lines:
    instr = line[0]
    val = int(line[1:])

    if instr in ["L", "R"]:
        val = val // 90
        if instr == "L":
            for _ in range(val):
                direction = left[direction]
        else:
            for _ in range(val):
                direction = right[direction]
    elif instr == "F":
        pos[0] += dirs[direction][0] * val
        pos[1] += dirs[direction][1] * val
    else:
        pos[0] += dirs[instr][0] * val
        pos[1] += dirs[instr][1] * val

manhattan = abs(pos[0]) + abs(pos[1])
print(f"Day 12 Part 1: { manhattan }")
