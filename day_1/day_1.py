with open("input.txt", "r") as dataset:
    data = [int(data) for data in dataset]

increased_counter = 0

previous = data[0]

for value in data[1:]:
    if value > previous:
        increased_counter += 1
    previous = value

print(increased_counter)


increased_counter = 0

a = data[0]
b = data[1]
c = data[2]

previous = sum([a, b, c])

for value in data[3:]:
    current = sum([b, c, value])
    if current > previous:
        increased_counter += 1
    a = b
    b = c
    c = value
    previous = current
    

print(increased_counter)