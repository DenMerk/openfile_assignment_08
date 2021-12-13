import os

file_list = []

for count in range(1, 4):
    file_name = f"{count}.txt"
    path = os.path.join(os.getcwd(), file_name)
    inner_list = []  # Inner list for sorting files by their size
    with open(path, encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            inner_list.append(line)
        inner_list.insert(0, str(len(inner_list)))
        inner_list.insert(0, file_name)
    file_list.append(inner_list)

file_list = sorted(file_list, key=len)  

with open('new.txt', 'x') as new_file:
    for counter in range(3):
        for line in file_list[counter]:
            line += '\n'
            new_file.write(line)


print(file_list)
