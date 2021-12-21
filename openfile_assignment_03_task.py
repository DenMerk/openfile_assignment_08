import os


def file_list_generator():
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
    return file_list


def file_writer():
    with open('new.txt', 'x') as new_file:
        data_source = file_list_generator()
        for counter in range(3):
            for line in data_source[counter]:
                line += '\n'
                new_file.write(line)


if __name__ == '__main__':
    file_writer()
