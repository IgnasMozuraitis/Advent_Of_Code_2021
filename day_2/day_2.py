with open("input.txt", "r") as dataset:
    data = []
    for line in dataset:
        direction, amount = line.split()
        amount = int(amount)
        data.append((direction, amount))

horisontal = 0
depth = 0

for direction, amount in data:
    if direction == "forward":
        horisontal += amount
    elif direction == "down":
        depth += amount
    elif direction == "up":
        depth -= amount

result = horisontal * depth

print(result)


horisontal = 0
depth = 0
aim = 0

for direction, amount in data:
    if direction == "forward":
        horisontal += amount
        depth += aim * amount
    elif direction == "down":
        aim += amount
    elif direction == "up":
        aim -= amount

result = horisontal * depth

print(result)