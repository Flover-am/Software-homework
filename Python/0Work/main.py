def logo_play():
    x = [0]
    y = [0]
    error = [0]
    pic = [[' ' for i in range(10)] for j in range(10)]
    brush = ' '
    pen_drawing = True

    Error = 0

    while 1:
        command = input().split()
        if command[0] == 'end':
            break
        elif command[0] == 'pen_up':
            pen_drawing = False
        elif command[0] == 'pen_down':
            pen_drawing = True
        elif command[0] == 'move':
            if len(command) == 4:
                brush = command[3]
            move(command[1], int(command[2]), pen_drawing, brush, False, x, y, pic, error)
        elif command[0] == 'cross':
            x_formal = x[0]
            y_formal = y[0]

            if len(command) == 3:
                brush = command[2]
            teps = int(command[1])

            if ((x[0] - teps) < 0) | ((x[0] + teps) > 9) | ((y[0] - teps) < 0) | ((y[0] + teps) > 9):
                Error = 1
                break

            pen_drawing = False
            move('L', teps, pen_drawing, brush, True, x, y, pic, error)
            pen_drawing = True
            move('R', 2 * teps, pen_drawing, brush, True, x, y, pic, error)

            pen_drawing = False
            move('L', teps, pen_drawing, brush, True, x, y, pic, error)
            move('U', teps, pen_drawing, brush, True, x, y, pic, error)

            pen_drawing = True
            move('D', 2 * teps, pen_drawing, brush, True, x, y, pic, error)
            pen_drawing = False
            move('U', teps, pen_drawing, brush, True, x, y, pic, error)
            pen_drawing = True

            x[0] = x_formal
            y[0] = y_formal

        elif command[0] == 'rect_f':
            x_formal = x[0]
            y_formal = y[0]

            if len(command) == 4:
                brush = command[3]
            line = int(command[1]) - 1
            column = int(command[2]) - 1
            if (x[0] + line) > 9 | (y[0] + column) > 9:
                Error = 1

                break

            for i in range(column + 1):
                move('R', line, pen_drawing, brush, True, x, y, pic, error)
                y[0] += 1
                x[0] = x_formal

            x[0] = x_formal
            y[0] = y_formal

        elif command[0] == 'rect':
            x_formal = x[0]
            y_formal = y[0]

            if len(command) > 3:
                brush = command[3]
            line = int(command[1]) - 1
            column = int(command[2]) - 1

            if ((x[0] + line) > 9) | ((y[0] + column) > 9):
                Error = 1
                break

            move('R', line, pen_drawing, brush, True, x, y, pic, error)
            move('D', column, pen_drawing, brush, True, x, y, pic, error)
            move('L', line, pen_drawing, brush, True, x, y, pic, error)
            move('U', column, pen_drawing, brush, True, x, y, pic, error)

    if not Error:
        for i in range(10):
            for j in range(10):
                print(pic[i][j], end='')
            if i < 10:
                print()
    else:
        print('Error!')


def move(direction, tep, pen_drawing, brush, if_bush_self, x, y, pic, error):
    if if_bush_self & pen_drawing:
        pic[y[0]][x[0]] = brush

    if direction == 'L':
        if pen_drawing:
            for place in range(x[0] - tep, x[0]):
                pic[y[0]][place] = brush
        x[0] -= tep
    elif direction == 'R':
        if pen_drawing:
            for place in range(x[0] + 1, x[0] + 1 + tep):
                pic[y[0]][place] = brush
        x[0] += tep
    elif direction == 'U':
        if pen_drawing:
            for place in range(y[0] - tep, y[0]):
                pic[place][x[0]] = brush
        y[0] -= tep
    elif direction == 'D':
        if pen_drawing:
            for place in range(y[0] + 1, y[0] + 1 + tep):
                pic[place][x[0]] = brush
        y[0] += tep


if __name__ == '__main__':
    logo_play()
