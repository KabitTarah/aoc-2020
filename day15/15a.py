game = [1,0,16,5,17,4]
#game = [1,3,2]
#game = [2,1,3]
#game = [1,2,3]

seen = {}
for i in range(len(game)):
    seen[game[i]] = i
for i in range(len(game), 30000000):
    if i % 10000 == 0: print(i)
    prev = game[i-1]
    if prev in seen.keys():
        last = seen[prev]
        next = (i - 1) - last
    else: next = 0
    game.append(next)
    seen[prev] = i - 1

print(f"Day 15 Part 1: { game[2019] }")
print(f"Day 15 Part 2: { game[29999999] }")
