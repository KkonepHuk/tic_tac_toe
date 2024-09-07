#объявление необходимых переменных
turn1 = ''
flag = True
counter = 0
game_board = list(range(1, 10))


#главный цикл
def main():
    global counter
    global flag

    create_board(game_board)
    while flag:
        move(game_board)
        result()


#отрисовка поля
def create_board(game_board):
    print('', game_board[0], '|', game_board[1], '|', game_board[2])
    print('---|---|---')
    print('', game_board[3], '|', game_board[4], '|', game_board[5])
    print('---|---|---')
    print('', game_board[6], '|', game_board[7], '|', game_board[8])


#выполнение хода
def move(game_board):
    global turn1

    while True:
        try:
            if turn1 == 'X':
                turn1, turn2 = 'O', 'X'
                m1, m2 = 'Введите номер клетки, на которую хотите совершить ход O: ', 'Введите номер клетки, на которую хотите совершить ход X: '
            else:
                turn2, turn1 = 'O', 'X'
                m2, m1 = 'Введите номер клетки, на которую хотите совершить ход O: ', 'Введите номер клетки, на которую хотите совершить ход X: '
            move = int(input(m1)) - 1
            if move in range(9) and str(game_board[move]) not in 'XO':
                game_board[move] = turn1
                break
            else:
                print('Недопустимый ввод, попробуйте еще раз!')
        except ValueError as e:
            print('Недопустимый ввод, попробуйте еще раз!', e)
    create_board(game_board)


#проверка комбинаций на итог партии
def check_combinations(game_board):
    # По горизонтали
    for i in range(0, 9, 3):
        if game_board[i] == game_board[i + 1] == game_board[i + 2]:
            return game_board[i]
    # По вертикали
    for i in range(0, 3):
        if game_board[i] == game_board[i + 3] == game_board[i + 6]:
            return game_board[i]
    # По диагонали
    if game_board[0] == game_board[4] == game_board[8] or game_board[2] == game_board[4] == game_board[6]:
        return game_board[4]
    return False


#объявление победителя
def result():
    global flag
    global counter

    counter += 1
    if check_combinations(game_board):
        print(f'Победил {check_combinations(game_board)}')
        flag = False
    elif counter == 9:
        print('Ничья')
        flag = False


main()