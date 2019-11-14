import random

# Tetrimino colors
cyan = (69, 206, 204) #rgb(69, 206, 204) # I
blue = (64, 111, 249) #rgb(64, 111, 249) # J
orange = (253, 189, 53) #rgb(253, 189, 53) # L
yellow = (246, 227, 90) #rgb(246, 227, 90) # O
green = (98, 190, 68) #rgb(98, 190, 68) # S
pink = (242, 64, 235) #rgb(242, 64, 235) # T
red = (225, 13, 27) #rgb(225, 13, 27) # Z

class Piece:    #피스에 임의대로 숫자를 바꿔서 아이템 피스를 생성함
    O = (((0,0,0,0,0), (0,0,0,0,0),(0,0,1,1,0),(0,0,1,1,0),(0,0,0,0,0)),) * 4
    O2 = (((0,0,0,0,0), (0,0,0,0,0),(0,0,8,1,0),(0,0,1,1,0),(0,0,0,0,0)),) * 4

    I = (((0,0,0,0,0),(0,0,0,0,0),(0,2,2,2,2),(0,0,0,0,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,0,2,0,0),(0,0,2,0,0),(0,0,2,0,0),(0,0,2,0,0)),
         ((0,0,0,0,0),(0,0,0,0,0),(2,2,2,2,0),(0,0,0,0,0),(0,0,0,0,0)),
         ((0,0,2,0,0),(0,0,2,0,0),(0,0,2,0,0),(0,0,2,0,0),(0,0,0,0,0)))
    
    I2 = (((0,0,0,0,0),(0,0,0,0,0),(0,2,2,9,2),(0,0,0,0,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,0,2,0,0),(0,0,2,0,0),(0,0,9,0,0),(0,0,2,0,0)),
         ((0,0,0,0,0),(0,0,0,0,0),(2,9,2,2,0),(0,0,0,0,0),(0,0,0,0,0)),
         ((0,0,2,0,0),(0,0,9,0,0),(0,0,2,0,0),(0,0,2,0,0),(0,0,0,0,0)))
    
    L = (((0,0,0,0,0),(0,0,3,0,0),(0,0,3,0,0),(0,0,3,3,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,0,0,0,0),(0,3,3,3,0),(0,3,0,0,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,3,3,0,0),(0,0,3,0,0),(0,0,3,0,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,0,0,3,0),(0,3,3,3,0),(0,0,0,0,0),(0,0,0,0,0)))
    
    L2 = (((0,0,0,0,0),(0,0,3,0,0),(0,0,3,0,0),(0,0,3,10,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,0,0,0,0),(0,3,3,3,0),(0,10,0,0,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,10,3,0,0),(0,0,3,0,0),(0,0,3,0,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,0,0,10,0),(0,3,3,3,0),(0,0,0,0,0),(0,0,0,0,0)))
    
    J = (((0,0,0,0,0),(0,0,4,0,0),(0,0,4,0,0),(0,4,4,0,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,4,0,0,0),(0,4,4,4,0),(0,0,0,0,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,0,4,4,0),(0,0,4,0,0),(0,0,4,0,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,0,0,0,0),(0,4,4,4,0),(0,0,0,4,0),(0,0,0,0,0)))
    
    J2 = (((0,0,0,0,0),(0,0,11,0,0),(0,0,4,0,0),(0,4,4,0,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,4,0,0,0),(0,4,4,11,0),(0,0,0,0,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,0,4,4,0),(0,0,4,0,0),(0,0,11,0,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,0,0,0,0),(0,11,4,4,0),(0,0,0,4,0),(0,0,0,0,0)))

    Z = (((0,0,0,0,0),(0,0,0,5,0),(0,0,5,5,0),(0,0,5,0,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,0,0,0,0),(0,5,5,0,0),(0,0,5,5,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,0,5,0,0),(0,5,5,0,0),(0,5,0,0,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,5,5,0,0),(0,0,5,5,0),(0,0,0,0,0),(0,0,0,0,0)))

    Z2 = (((0,0,0,0,0),(0,0,0,12,0),(0,0,5,5,0),(0,0,5,0,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,0,0,0,0),(0,5,5,0,0),(0,0,5,12,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,0,5,0,0),(0,5,5,0,0),(0,12,0,0,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,12,5,0,0),(0,0,5,5,0),(0,0,0,0,0),(0,0,0,0,0)))
    
    S = (((0,0,0,0,0),(0,0,6,0,0),(0,0,6,6,0),(0,0,0,6,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,0,0,0,0),(0,0,6,6,0),(0,6,6,0,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,6,0,0,0),(0,6,6,0,0),(0,0,6,0,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,0,6,6,0),(0,6,6,0,0),(0,0,0,0,0),(0,0,0,0,0)))
    
    S2 = (((0,0,0,0,0),(0,0,6,0,0),(0,0,13,6,0),(0,0,0,6,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,0,0,0,0),(0,0,13,6,0),(0,6,6,0,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,6,0,0,0),(0,6,13,0,0),(0,0,6,0,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,0,6,6,0),(0,6,13,0,0),(0,0,0,0,0),(0,0,0,0,0)))
    
    T = (((0,0,0,0,0),(0,0,7,0,0),(0,0,7,7,0),(0,0,7,0,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,0,0,0,0),(0,7,7,7,0),(0,0,7,0,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,0,7,0,0),(0,7,7,0,0),(0,0,7,0,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,0,7,0,0),(0,7,7,7,0),(0,0,0,0,0),(0,0,0,0,0)))
    
    T2 = (((0,0,0,0,0),(0,0,7,0,0),(0,0,7,7,0),(0,0,14,0,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,0,0,0,0),(0,14,7,7,0),(0,0,7,0,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,0,14,0,0),(0,7,7,0,0),(0,0,7,0,0),(0,0,0,0,0)),
         ((0,0,0,0,0),(0,0,7,0,0),(0,7,7,14,0),(0,0,0,0,0),(0,0,0,0,0)))

    PIECES = {'O': O, 'I': I, 'L': L, 'J': J, 'Z': Z, 'S':S, 'T':T
              ,'O2': O2, 'I2': I2, 'L2': L2, 'J2': J2, 'Z2': Z2, 'S2':S2, 'T2':T2}
    T_COLOR = [yellow ,cyan, orange, blue, red, green, pink, (55, 55, 55)]

    def __init__(self, piece_name=None):
        if piece_name:
            self.piece_name = piece_name
        else:
            self.piece_name = random.choice(list(Piece.PIECES.keys()))
        self.rotation = 0
        self.array2d = Piece.PIECES[self.piece_name][self.rotation]
        

    def __iter__(self):
        for row in self.array2d:
            yield row

    def rotate(self, clockwise=True):
        if clockwise:
            self.rotation = (self.rotation + 1) % 4
        else:
            self.rotation = (self.rotation - 1) % 4
        self.array2d = Piece.PIECES[self.piece_name][self.rotation]
    
