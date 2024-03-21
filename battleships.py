def generate_board():  # to generate the board
    board = [[' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']]  # first row
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']  # fist vertical row
    for i in range(10):
        row = [letters[i]]  # first index of the row is each index of letters
        for q in range(10):
            row.append(' ')  # appending spaces 8 times for an 8 by 8 grid
        board.append(row)  # adding each row to the board
    return board, letters


def placement(board, letters):  # placement of ships
    h_v = ['h', 'v']  # data validity
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # numbers for the ship placement operation
    input_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # numbers allowed for input
    ship_lengths = [5, 4, 3, 3, 2]  # the different ship lengths needing to be placed
    for i in range(len(ship_lengths)):
        axis = input('horizontal(h) or vertical(v)? ').strip().lower()
        while axis not in h_v:
            axis = input("that is not valid, please enter 'h' or 'v' ")
        if axis == 'h':  # horizontal ship placement, asking for which horizontal row and the anchor point
            while True:
                empty = True
                row_letter = input('what row would you like to place your ' + str(ship_lengths[i]) +
                                   ' units long ship in? A, B, C, D, E, F, G, H, I, J. ').strip().upper()  # user input
                if row_letter not in letters:  # data validity, makes sure the input is in the board
                    print('That is not valid, try again. ')
                    continue
                try:  # data validity for the ship placement itself and input and input validity
                    place = int(input('where do you want the left tip of your boat? 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. '))
                    if place not in input_numbers:  # makes sure the input is in the board
                        print('That is not valid, try again. ')
                        continue
                    for y in range(ship_lengths[i]):  # making sure the user doesn't cause ships to overlap
                        if board[letters.index(row_letter) + 1][place + y] == 'S':  # checks each index for taken spaces
                            empty = False
                    if empty is False:
                        print('that location has already been taken, try again. ')
                        continue
                except ValueError:  # checks for non integer inputs
                    print('That is not Valid, try again. ')
                    continue
                except IndexError:  # checks for ships trying to extend out of bounds
                    print('That location extends out of bounds, try again. ')
                    continue
                else:
                    break
            for y in range(ship_lengths[i]):
                board[letters.index(row_letter) + 1][place + y] = 'S'
                # placing the ship segments horizontally with a loop using the inputs as an anchor

        if axis == 'v':  # vertical ship placement, asking for which vertical row and for the anchor point
            while True:  # data validity for integer input
                empty = True
                try:
                    row_number = int(input('what row do you want your ' + str(ship_lengths[i]) +
                                           ' units long ship to be in? 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. '))  # user input
                    if row_number not in input_numbers:  # making sure the number entered is in the board
                        print('That is not valid, try again. ')
                        continue
                    place = input(  # user input
                        'where do you want the tip of your boat? A, B, C, D, E, F, G, H, I, J. ').strip().upper()
                    if place not in letters:  # making sure the letter entered is in the board
                        print('That is not valid, try again. ')
                        continue
                    for y in range(ship_lengths[i]):  # making sure the ships don't over lap
                        if board[letters.index(place) + y + 1][numbers.index(row_number + 1)] == 'S':
                            empty = False
                    if empty is False:
                        print('that location has already been taken, try again. ')
                        continue
                except ValueError:  # checking for non integer inputs
                    print('that is not a number, try again. ')
                    continue
                except IndexError:  # checking for ships extending out of bounds
                    print('that location extends out of bounds, try again. ')
                    continue
                else:
                    break
            for y in range(ship_lengths[i]):
                board[letters.index(place) + y + 1][numbers.index(row_number) + 1] = 'S'
                # placing the ship segments vertically with a loop using the inputs as an anchor
        print_board(board)
    return board


def print_board(board):  # displaying the different boards by printing rows under the previous
    for i in range(len(board)):
        print(board[i])


def turns(letters, p1_view, p2_view, player1, player2):  # bomb placement
    turn1 = ['', '']  # coordinate lists
    turn2 = ['', '']
    input_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    input('switching players: press enter to continue. ')  # so players can't see each others boards when taking turns
    print_board(p1_view)  # printing the view grid
    print_board(player1)  # printing the players grid
    while True:  # data validity for integer input
        turn1[0] = input('Player1 turn: type in the first letter coordinate for your bomb. ').strip().upper()
        if turn1[0] not in letters:  # data validity, - if the input isn't in the list
            print('Please type in a letter that is on the board. ')
            continue
        try:
            turn1[1] = int(input('Type in the second number coordinate for your bomb. '))
            if turn1[1] not in input_numbers:   # making sure the input is a valid number
                print('That is not valid, try again. ')
                continue
            if player2[letters.index(turn1[0]) + 1][turn1[1]] == 'X':
                print('you have already dropped a bomb there, try again. ')
                continue   # making sure the user doesn't drop a bomb in the same location
            if player2[letters.index(turn1[0]) + 1][turn1[1]] == '0':
                print('you have already dropped a bomb there, try again. ')
                continue
        except ValueError:  # checking to make sure the input is a number
            print('That is not valid, try again. ')
            continue
        else:
            break
    print('\n' * 20)  # clear the screen by printing 40 empty lines
    input('switching players: press enter to continue. ')  # prompt so players cant see each others boards between turns
    print('\n' * 20)
    print_board(p2_view)  # printing the view grid
    print_board(player2)  # printing the players grid
    while True:  # data validity
        turn2[0] = input('Player2 turn: type in the first letter coordinate for your bomb. ').strip().upper()
        if turn2[0] not in letters:  # data validity
            print('Please type in a letter that is on the board. ')
            continue
        try:
            turn2[1] = int(input('Type in the second number coordinate for your bomb. '))
            if turn2[1] not in input_numbers:  # checking that the input is in the board
                print('That is not valid, try again. ')
                continue
            if player1[letters.index(turn2[0]) + 1][turn2[1]] == 'X':
                print('you have already dropped a bomb there, try again. ')
                continue  # making sure the user doesn't drop a bomb in the same location
            if player1[letters.index(turn2[0]) + 1][turn2[1]] == '0':
                print('you have already dropped a bomb there, try again. ')
                continue
        except ValueError:  # checking for non integer inputs
            print('That is not valid, try again. ')
            continue
        else:
            break
    return turn1, turn2  # returning the turns for hit_miss check


def hit_miss(player1, player2, turn1, turn2, letters, p1_view, p2_view, p1_ships, p2_ships):
    # display for if the turn was a hit or miss
    if player2[letters.index(turn1[0]) + 1][turn1[1]] == 'S':
        player2[letters.index(turn1[0]) + 1][turn1[1]], p1_view[letters.index(turn1[0]) + 1][turn1[1]] = 'X', 'X'
        p2_ships -= 1
        #  if there is a ship segment where player 1s bomb was placed, that location on the player 2 board and on
        #  player1's view (p1_view) will be marked with an 'X'
    else:
        player2[letters.index(turn1[0]) + 1][turn1[1]], p1_view[letters.index(turn1[0]) + 1][turn1[1]] = '0', '0'
        #  if there isn't a ship segment where player 1s bomb was placed, that location on the player 2 board and on
        #  player1's view (p1_view) will be marked with an '0'

    if player1[letters.index(turn2[0]) + 1][turn2[1]] == 'S':
        player1[letters.index(turn2[0]) + 1][turn2[1]], p2_view[letters.index(turn2[0]) + 1][turn2[1]] = 'X', 'X'
        p1_ships -= 1
        #  if there is a ship segment where player 2s bomb was placed, that location on the player 1 board and on
        #  player2's view (p2_view) will be marked with an 'X'
    else:
        player1[letters.index(turn2[0]) + 1][turn2[1]], p2_view[letters.index(turn2[0]) + 1][turn2[1]] = '0', '0'
        #  if there isn't a ship segment where player 2s bomb was placed, that location on the player 1 board and on
        #  player2's view (p2_vie  w) will be marked with an '0'
    return p1_ships, p2_ships


def main():  # main function for looping the other functions
    p1_view, letters = generate_board()
    p2_view, letters = generate_board()
    p1_ships = 17  # starting amount of ship segments per player
    p2_ships = 17
    while True:
        print('\n' * 40)
        turn1, turn2 = turns(letters,p1_view, p2_view, player1, player2)  # bomb turns
        p1_ships, p2_ships = hit_miss(player1, player2, turn1, turn2, letters, p1_view, p2_view, p1_ships, p2_ships)
        #  hit or miss check
        if p2_ships == 0:  # win check, if all player 2 ship segments are gone, player 1 wins.
            print('')
            print('Game over: Player 1 has won. ')
            exit()
        if p1_ships == 0:  # win check, if all player 1 ship segments are gone, player 2 wins.
            print('')
            print('Game over: Player 2 has won. ')
            exit()


board, letters = generate_board()  # new board
print_board(board)
print('player 1, place your ships. ')
player1 = placement(board, letters)  # player1 grid
print('\n' * 40)  # clearing the screen by printing 40 empty lines
board, letters = generate_board()  # new board
print_board(board)
print('player 2, place your ships. ')
player2 = placement(board, letters)  # player 2 grid
main()  # repetitive operations like taking turns wit bombs and checking for hit or miss and win check
