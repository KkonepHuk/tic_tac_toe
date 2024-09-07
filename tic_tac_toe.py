def main():
    game_board = list(range(1, 10))
    create_board(game_board)
    counter = 0
    while True:
        move_O(game_board)
        counter += 1
        if check_combinations(game_board):
            print(f'Победил {check_combinations(game_board)}')
            break
        elif counter == 9:
            print('Ничья')
            break

        move_X(game_board)
        counter += 1
        if check_combinations(game_board):
            print(f'Победил {check_combinations(game_board)}')
            break
        elif counter == 9:
            print('Ничья')
            break


def create_board(game_board):
    print('', game_board[0], '|', game_board[1], '|', game_board[2])
    print('---|---|---')
    print('', game_board[3], '|', game_board[4], '|', game_board[5])
    print('---|---|---')
    print('', game_board[6], '|', game_board[7], '|', game_board[8])


def move_O(game_board):
    while True:
        try:
            move = int(input('Введите номер клетки, на которую хотите совершить ход O: ')) - 1
            if move in range(9) and str(game_board[move]) not in 'XO':
                game_board[move] = 'O'
                break
            else:
                print('Недопустимый ввод, попробуйте еще раз!')
        except ValueError as e:
            print('Недопустимый ввод, попробуйте еще раз!', e)
    create_board(game_board)


def move_X(game_board):
    while True:
        try:
            move = int(input('Введите номер клетки, на которую хотите совершить ход X: ')) - 1
            if move in range(9) and str(game_board[move]) not in 'XO':
                game_board[move] = 'X'
                break
            else:
                print('Недопустимый ввод, попробуйте еще раз!')
        except ValueError as e:
            print('Недопустимый ввод, попробуйте еще раз!', e)
    create_board(game_board)


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


main()