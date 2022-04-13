"""write your code in following methods"""
file_path = './tasks.txt'


def add(task):
    with open(file_path, 'a') as file:
        file.writelines(f'todo:{task}\n')


def delete(task):
    line_number = 0
    with open(file_path, 'r') as file:
        lines_list = file.readlines()
        for line in file:
            if task in line:
                break
            line_number += 1
    del lines_list[line_number]
    with open(file_path, 'w+') as file:
        file.writelines(lines_list)


def complete(task):
    line_number = 0
    with open(file_path, 'r') as file:
        lines_list = file.readlines()
        for line in file:
            if task in line:
                break
            line_number += 1
    lines_list[line_number] = f'completed:{task}'
    with open(file_path, 'w+') as file:
        file.writelines(lines_list)


def find(status):
    with open(file_path, 'r') as file:
        for line in file:
            if status in line:
                print(line)


def to_do():
    while True:
        command = input().split(' "')
        if command[0] == 'todo -a':
            for i in range(1, len(command)):
                add(command[i][0:len(command[i]) - 1])

        elif command[0] == 'todo -d':
            delete(command[1][0:len(command[1]) - 1])

        elif command[0] == 'todo -c':
            for i in range(1, len(command) - 1):
                complete(command[i][0:len(command[i]) - 1])

        elif command[0] == 'todo -f':
            if command[1] == 'todo':
                find('todo')
            elif command[1] == 'completed':
                find('completed')
        elif command[0] == 'todo -all':
            with open(file_path, 'r') as file:
                print(file)
        elif command[0] == 'todo -quit':
            return
