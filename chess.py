import zzz

def sign(x, y):
    if x * y > 0 and abs(x) < abs(y):
        return True
    return False

def check_move(a, x):
    # проверка на выход за край доски

    if a[0] + x[0] > 8 or a[1] + x[1] > 8 or a[0] + x[0] < 1 or a[1] + x[1] < 1:
        # print(a[0],x[0],a[1],x[1])
        return False
    return True


class Piece:

    def __init__(self, place, color, name):
        self.place = place
        self.color = color
        self.name = name
        self.can_move = []
        self.div = 1

    def check_moving(self, move):
        if not (check_move(self.place, move)):
            return False
        if not (move in self.can_move):
            return False
        return True

    def moving(self, move):
        if Piece.check_moving(self, move):
            self.place[0] += move[0]
            self.place[1] += move[1]

    def Print(self):
        return self.place, self.color, self.name

    def check_len_can(self):
        return len(self.can_move)

    def check_can(self):
        return self.can_move

    def check_div(self):
        return self.div

    def check_pawn(self):
        if self.name == 'Pawn':
            return True
        return False


class Hollow(Piece):
    def __init__(self, place):
        Piece.__init__(self, place, 0, 'Hollow')

    def check_moving(self, move):
        return True


class Pawn(Piece):
    # пешка
    def __init__(self, place, color):
        Piece.__init__(self, place, color, 'Pawn')
        if color == 1:
            self.can_move = [[1, 0], [2, 0]]
            self.can_eat = [[1, 1], [1, -1]]
        else:
            self.can_move = [[-1, 0], [-2, 0]]
            self.can_eat = [[-1, -1], [-1, 1]]
        self.div = 1

    def check_eat(self):
        return self.can_eat

    def check_moving(self, move):
        if not (check_move(self.place, move)):
            return False
        if not (move in self.can_move) and not(move in self.can_eat):
            return False
        return True

    def moving(self, move):
        if Pawn.check_moving(self, move):
            self.place[0] += move[0]
            self.place[1] += move[1]


class Horse(Piece):
    # конь

    def __init__(self, place, color):
        Piece.__init__(self, place, color, 'Horse')
        self.can_move = [[1, 2], [2, 1], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]
        self.div = 1


class Bishop(Piece):
    # слон

    def __init__(self, place, color):
        Piece.__init__(self, place, color, 'Bishop')
        self.can_move = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [-1, 1], [-2, 2], [-3, 3], [-4, 4],
                         [-5, 5],
                         [-6, 6], [-7, 7], [-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7],
                         [1, -1], [2, -2], [3, -3],
                         [4, -4], [5, -5], [6, -6], [7, -7]]

        self.div = 4

    # изменение положения


class Rook(Piece):
    # ладья
    def __init__(self, place, color):
        Piece.__init__(self, place, color, 'Rook')
        self.can_move = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [-1, 0], [-2, 0], [-3, 0], [-4, 0],
                         [-5, 0], [-6, 0], [-7, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, -1],
                         [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7]]

        self.div = 4


class Queen(Piece):

    def __init__(self, place, color):
        Piece.__init__(self, place, color, 'Queen')
        self.can_move = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [-1, 0], [-2, 0], [-3, 0], [-4, 0],
                         [-5, 0], [-6, 0], [-7, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, -1],
                         [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5],
                         [6, 6], [7, 7], [-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5],
                         [-6, 6], [-7, 7], [-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7],
                         [1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7]]

        self.div = 8


class King(Piece):

    def __init__(self, place, color):
        Piece.__init__(self, place, color, 'King')
        self.can_move = [[1, 1], [1, 0], [-1, -1], [1, -1], [-1, 1], [0, 1], [-1, 0], [0, -1]]
        self.div = 1


class Game:

    def __init__(self):
        self.board = []

    def make_hollow(self):
        for i in range(1, 9):
            for j in range(1, 9):
                self.board.append(Hollow([i, j]))

    def start_game(self):
        Game.make_hollow(self)
        for j in range(8, 16):
            self.board[j] = Pawn([2, j - 7], 1)
        for i in range(55, 47, -1):
            self.board[i] = Pawn([7, i - 47], -1)
        self.board[0] = Rook([1, 1], 1)
        self.board[7] = Rook([1, 8], 1)
        self.board[56] = Rook([8, 1], -1)
        self.board[63] = Rook([8, 8], -1)
        self.board[1] = Horse([1, 2], 1)
        self.board[6] = Horse([1, 7], 1)
        self.board[57] = Horse([8, 2], -1)
        self.board[62] = Horse([8, 7], -1)
        self.board[2] = Bishop([1, 3], 1)
        self.board[5] = Bishop([1, 6], 1)
        self.board[58] = Bishop([8, 3], -1)
        self.board[61] = Bishop([8, 6], -1)
        self.board[59] = Queen([8, 4], -1)
        self.board[60] = King([8, 5], -1)
        self.board[3] = Queen([1, 4], 1)
        self.board[4] = King([1, 5], 1)

    def Print(self):
        for i in range(64):
            print(self.board[i].Print()[0], '%2d' % self.board[i].Print()[1], '%6s' % self.board[i].Print()[2],
                  end=' | ')
            if (i + 1) % 8 == 0:
                print()

    def check_move_piece(self, place, move):
        place_on_board = (place[0] - 1) * 8 + place[1] - 1
        if not (self.board[place_on_board].check_moving(move)):
            return False
        tmp1 = self.board[place_on_board].Print()[0][0] + move[0]
        tmp2 = self.board[place_on_board].Print()[0][1] + move[1]
        new_place_on_board = (tmp1 - 1) * 8 + tmp2 - 1
        if self.board[place_on_board].check_pawn():
            if move in self.board[place_on_board].check_eat():
                if self.board[place_on_board].Print()[1]!=-self.board[new_place_on_board].Print()[1]:
                    return False
                else:
                    return True
            if self.board[place_on_board].Print()[0][0] != 2 and self.board[place_on_board].Print()[0][0] != 7:
                if move != [1, 0] or move != [-1, 0]:
                    return False
                if self.board[place_on_board].Print()[1] == 1 and move == [1, 0]:
                    return True
                if self.board[place_on_board].Print()[1] == -1 and move == [-1, 0]:
                    return True
        if self.board[new_place_on_board].Print()[1] != self.board[place_on_board].Print()[1]:
            for i in range(self.board[place_on_board].check_div() - 1):
                for j in self.board[place_on_board].check_can()[
                         (self.board[place_on_board].check_len_can() // self.board[place_on_board].check_div() * i):
                         (self.board[place_on_board].check_len_can() // self.board[place_on_board].check_div() * (
                                 i + 1))]:
                    if sign(j[0], move[0]) and sign(j[1], move[1]):
                        k = (self.board[place_on_board].Print()[0][0] + j[0]) * 8 + (
                                self.board[place_on_board].Print()[0][1] + j[1])
                        if self.board[k].Print()[1] != 0:
                            return False
        return True

    def move(self, place, move):
        if Game.check_move_piece(self, place, move):
            place_on_board = (place[0] - 1) * 8 + place[1] - 1
            tmp1 = self.board[place_on_board].Print()[0][0] + move[0]
            tmp2 = self.board[place_on_board].Print()[0][1] + move[1]
            new_place_on_board = (tmp1 - 1) * 8 + tmp2 - 1
            self.board[place_on_board].moving(move)
            self.board[new_place_on_board], self.board[place_on_board] = self.board[place_on_board], self.board[
                new_place_on_board]
            self.board[place_on_board] = Hollow(place)

    def find_piece(self, color, name='King'):
        for i in self.board:
            if i.Print()[2] == name and i.Print()[1] == color:
                return i.Print()[0]

    def danger(self, color):
        king_place = Game.find_piece(self, color)
        count_den = 0
        for i in self.board:
            if i.Print()[1] == -color:
                if Game.check_move_piece(self, i.Print()[0],
                                         [king_place[0] - i.Print()[0][0], king_place[1] - i.Print()[0][1]]):
                    count_den += 1
        return count_den

    def check_mate(self, color):
        # king_place = Game.find_piece(self, -color, 'King')
        a = self.board[:]
        for i in self.board:
            if i.Print()[1] == color:
                for j in self.board:
                    k = i.Print()
                    if k[1] != 0:
                        Game.move(self, k[0], j.Print()[0])
                        if not (Game.danger(self, color)):
                            self.board = a[:]
                            return False
        return True

    def check_color(self, place):
        return self.board[(place[0] - 1) * 8 + place[1] - 1].Print()[1]


class ProcessingConsole:

    def __init__(self):
        self.lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.Brd = Game()

    def console_input(self, color):
        self.Brd.Print()
        if self.Brd.danger(color):
            if self.Brd.check_mate(color):
                if color == -1:
                    print('Game Over \n Win - White')
                else:
                    print('Game Over \n Win - Black')
                return 0
        console_place = input('введите координаты фигуры ')
        step = input('введите координаты хода ')
        place = []
        for i in range(len(self.lst)):
            if self.lst[i] == console_place[0]:
                place = [int(console_place[1]), i + 1]
        for i in range(len(self.lst)):
            if self.lst[i] == step[0]:
                step = [int(step[1]), i + 1]
        move = [step[0] - place[0], step[1] - place[1]]
        if self.Brd.check_color(place) != color or self.Brd.check_move_piece(place,move):
            print('Недопустимый ход! \nСделайте ход еще раз!')
            ProcessingConsole.console_input(self, color)
            return 0
        self.Brd.move(place, move)
        ProcessingConsole.console_input(self, -color)

    def start(self):
        self.Brd.start_game()
        ProcessingConsole.console_input(self, 1)


a = ProcessingConsole()
a.start()

