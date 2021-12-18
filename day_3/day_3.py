# first part

with open("input.txt") as file:
    data = []
    for line in file.readlines():
        data.append([int(x) for x in line.strip()])

numbers_list = [0 for n in range(0, len(data[0]))]

for line in data:
    for number in range(0, len(line)):
        numbers_list[number] += line[number]

epsilon_rate = int("".join(["1" if n < len(data) / 2 else "0" for n in numbers_list]), 2)
gamma_rate = int("".join(["0" if n < len(data) / 2 else "1" for n in numbers_list]), 2)

print(int("".join(["1" if n < len(data) / 2 else "0" for n in numbers_list])))
print(gamma_rate * epsilon_rate)


# second part

data_set = data.copy()
new_data_set = []

def taking_data(data_set):
    numbers_list = [0 for n in range(0, len(data_set[0]))]
    for line in data_set:
        for number in range(0, len(line)):
            numbers_list[number] += line[number]
    return [1 if n < len(data_set) / 2 else 0 for n in numbers_list]

counter = 0
while len(data_set) > 1:
    
    removables = taking_data(data_set)

    for line in data_set:
            if line[counter] == removables[counter]:
                new_data_set.append(line)
    data_set = new_data_set
    new_data_set = []
    counter += 1

print(int("".join(map(str, data_set[0])),2))


data_set = data.copy()
new_data_set = []
counter = 0
while len(data_set) > 1:
    
    removables = taking_data(data_set)
    
    for line in data_set:
            if line[counter] != removables[counter]:
                new_data_set.append(line)
    data_set = new_data_set
    new_data_set = []
    counter += 1

print(int("".join(map(str, data_set[0])),2))