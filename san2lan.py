## chess moves parser attempt, not sucessful at all. i gave up on this one


def possible_knight(curr : list, white=True) -> list:

    pos = [[-2, 1],
        [-1, 2],
        [1, 2],
        [2, 1],
        [2, -1],
        [1, -2],
        [-1, -2],
        [-2, -1]]
    
    l = []

    #logic --> if square is occupied by a piece in the same colour, then I cant make a move there
    # but, if there is a piece of other colour I can and its a capture. Same logic is used for every piece below.

    ### now i think somethings wrong here but i dont know what, feel free to correct me it will be appreciated

    if white:

        for el in pos: 
            if curr[0] + el[0] <= 8 and curr[0] + el[0] >= 1 and curr[1] + el[1] <= 8 and curr[1] + el[1] >= 1: 
                if conversion([curr[0] + el[0], curr[1] + el[1]]) not in [piece[0] for piece in white_pieces.values()]:
                    l.append(conversion([curr[0] + el[0], curr[1] + el[1]]))

    if not white:

        pos = [[-2, 1],
            [-1, 2],
            [1, 2],
            [2, 1],
            [2, -1],
            [1, -2],
            [-1, -2],
            [-2, -1]]
        
        l = []


        for el in pos: 
            if curr[0] + el[0] <= 8 and curr[0] + el[0] >= 1 and curr[1] + el[1] <= 8 and curr[1] + el[1] >= 1: 
                if conversion([curr[0] + el[0], curr[1] + el[1]]) not in [piece[0] for piece in black_pieces.values()]:
                    l.append(conversion([curr[0] + el[0], curr[1] + el[1]]))

    return l



def possible_bishop(curr : list, white=True) -> list:

    if white:


        l = []

        i = 1

        while curr[0] + i <= 8 and curr[1] + i <= 8:
            if conversion([curr[0]+i, curr[1]+i]) in [piece[0] for piece in white_pieces.values()]:
                break
            elif conversion([curr[0]+i, curr[1]+i]) in [piece[0] for piece in black_pieces.values()]:
                l.append(conversion([curr[0]+i, curr[1]+i]))
                break
            l.append(conversion([curr[0]+i, curr[1]+i]))
            i += 1

        j = 1

        while curr[0] - j >= 1 and curr[1] - j >= 1:
            if conversion([curr[0]-j, curr[1]-j]) in [piece[0] for piece in white_pieces.values()]:
                break
            elif conversion([curr[0]-j, curr[1]-j]) in [piece[0] for piece in black_pieces.values()]:
                l.append(conversion([curr[0]-j, curr[1]-j]))
                break
            else:
                l.append(conversion([curr[0]-j, curr[1]-j]))
            j += 1

        x,y = 1,1

        while curr[0] - x >= 1 and curr[1] + x <= 8:
            if conversion([curr[0]-x,curr[1]+x]) in [piece[0] for piece in white_pieces.values()]:
                break
            elif conversion([curr[0]-x,curr[1]+x]) in [piece[0] for piece in black_pieces.values()]:
                l.append(conversion([curr[0]-x,curr[1]+x]))
                break
            else:
                l.append(conversion([curr[0]-x,curr[1]+x]))
            x += 1

        while curr[0] + y <= 8 and curr[1] - y >= 1:
            if conversion([curr[0]+y,curr[1]-y]) in [piece[0] for piece in white_pieces.values()]:
                break
            elif conversion([curr[0]+y,curr[1]-y]) in [piece[0] for piece in black_pieces.values()]:
                l.append(conversion([curr[0]+y,curr[1]-y]))
                break
            else:
                l.append(conversion([curr[0]+y,curr[1]-y])) 
            y += 1

    if not white:

        l = []

        i = 1

        while curr[0] + i <= 8 and curr[1] + i <= 8:
            if conversion([curr[0]+i, curr[1]+i]) in [piece[0] for piece in white_pieces.values()]:
                break
            elif conversion([curr[0]+i, curr[1]+i]) in [piece[0] for piece in black_pieces.values()]:
                l.append(conversion([curr[0]+i, curr[1]+i]))
                break
            else:
                l.append(conversion([curr[0]+i, curr[1]+i]))
                i += 1

        j = 1

        while curr[0] - j >= 1 and curr[1] - j >= 1:
            if conversion([curr[0]-j, curr[1]-j]) in [piece[0] for piece in white_pieces.values()]:
                break
            elif conversion([curr[0]-j, curr[1]-j]) in [piece[0] for piece in black_pieces.values()]:
                l.append(conversion([curr[0]-j, curr[1]-j]))
                break
            else:
                l.append(conversion([curr[0]-j, curr[1]-j]))
                j += 1

        x,y = 1,1

        while curr[0] - x >= 1 and curr[1] + x <= 8:
            if conversion([curr[0]-x,curr[1]+x]) in [piece[0] for piece in white_pieces.values()]:
                break
            elif conversion([curr[0]-x,curr[1]+x]) in [piece[0] for piece in black_pieces.values()]:
                l.append(conversion([curr[0]-x,curr[1]+x]))
                break
            else:
                l.append(conversion([curr[0]-x,curr[1]+x]))
                x += 1

        while curr[0] + y <= 8 and curr[1] - y >= 1:
            if conversion([curr[0]+y,curr[1]-y]) in [piece[0] for piece in white_pieces.values()]:
                break
            elif conversion([curr[0]+y,curr[1]-y]) in [piece[0] for piece in black_pieces.values()]:
                l.append(conversion([curr[0]+y,curr[1]-y]))
                break
            else:
                l.append(conversion([curr[0]+y,curr[1]-y])) 
                y += 1



    return l

def possible_rook(curr : list, white=True) -> list:

    if white:

        l = []

        i = 1

        while curr[1] + i <= 8:

            if conversion([curr[0], curr[1]+i]) in [piece[0] for piece in white_pieces.values()]:
                break
            elif conversion([curr[0], curr[1]+i]) in [piece[0] for piece in black_pieces.values()]:
                l.append(conversion([curr[0], curr[1]+i]))
                break
            l.append(conversion([curr[0], curr[1]+i]))
            i += 1

        s = 1

        while curr[1] - s >= 1:

            if conversion([curr[0], curr[1]-s]) in [piece[0] for piece in white_pieces.values()]:
                break
            elif conversion([curr[0], curr[1]-s]) in [piece[0] for piece in black_pieces.values()]:
                l.append(conversion([curr[0], curr[1]-s]))
                break
            l.append(conversion([curr[0], curr[1]-s]))
            s += 1


        j = 1

        while curr[0] - j >= 1:
        
            if conversion([curr[0]-j, curr[1]]) in [piece[0] for piece in white_pieces.values()]:
                break
            elif conversion([curr[0]-j, curr[1]]) in [piece[0] for piece in black_pieces.values()]:
                l.append(conversion([curr[0]-j, curr[1]]))
                break
                
            l.append(conversion([curr[0]-j, curr[1]]))
            j += 1

        x = 1

        while curr[0] + x <= 8:
            if conversion([curr[0]+x, curr[1]]) in [piece[0] for piece in white_pieces.values()]:
                break
            elif conversion([curr[0]+x, curr[1]]) in [piece[0] for piece in black_pieces.values()]:
                l.append(conversion([curr[0]+x, curr[1]]))
                break
            l.append(conversion([curr[0]+x, curr[1]]))
            x += 1

    if not white:

        l = []

        x,i,s,j = 1,1,1,1
        while curr[0] + x <= 8:

            if conversion([curr[0]+x, curr[1]]) in [piece[0] for piece in black_pieces.values()]:
                break
            elif conversion([curr[0]+x, curr[1]]) in [piece[0] for piece in white_pieces.values()]:
                l.append(conversion([curr[0]+x, curr[1]]))
                break
            l.append(conversion([curr[0]+x, curr[1]]))
            x += 1

        while curr[0] - i >= 1:

            if conversion([curr[0]-i, curr[1]]) in [piece[0] for piece in black_pieces.values()]:
                break
            elif conversion([curr[0]-i, curr[1]]) in [piece[0] for piece in white_pieces.values()]:
                l.append(conversion([curr[0]-i, curr[1]]))
                break
            l.append(conversion([curr[0]-i, curr[1]]))
            i += 1

        while curr[1] + s <= 8:

            if conversion([curr[0], curr[1]+s]) in [piece[0] for piece in black_pieces.values()]:
                break
            elif conversion([curr[0], curr[1]+s]) in [piece[0] for piece in white_pieces.values()]:
                l.append(conversion([curr[0], curr[1]+s]))
                break
            l.append(conversion([curr[0], curr[1]+s]))
            s += 1

        while curr[1] - j >= 1:

            if conversion([curr[0], curr[1]-j]) in [piece[0] for piece in black_pieces.values()]:
                break
            elif conversion([curr[0], curr[1]-j]) in [piece[0] for piece in white_pieces.values()]:
                l.append(conversion([curr[0], curr[1]-j]))
                break
            l.append(conversion([curr[0], curr[1]-j]))
            j += 1


    return l
        
    

def possible_queen(curr, white=True):

    # reusing previous funcs

    if white:

        l= possible_bishop(curr) + possible_rook(curr)

    if not white:

        l = possible_bishop(curr, white=False) + possible_rook(curr, white=False)


    return l

def possible_king(curr, white=True):
        
    pos = [

        [1, 0],
        [0, 1],
        [-1, 0],
        [0, -1],
        [1, 1],
        [-1, 1],
        [-1, -1],
        [1, -1]

    ]

    l = []

    if white:
        for el in pos:
            if curr[0] + el[0] <= 8 and curr[0] + el[0] >= 1 and curr[1] + el[1] <= 8 and curr[1] + el[1] >= 1: 
                if conversion([curr[0] + el[0], curr[1] + el[1]]) not in [piece[0] for piece in white_pieces.values()]:
                    l.append(conversion([curr[0] + el[0], curr[1] + el[1]]))



    if not white:
        for el in pos:
            if curr[0] + el[0] <= 8 and curr[0] + el[0] >= 1 and curr[1] + el[1] <= 8 and curr[1] + el[1] >= 1: 
                if conversion([curr[0] + el[0], curr[1] + el[1]]) not in [piece[0] for piece in black_pieces.values()]:
                    l.append(conversion([curr[0] + el[0], curr[1] + el[1]]))


    return l

## i did not forget about the pawn promote ability, just gave up ;/

def possible_pawn(curr, black=False):

    if not black:

        l = []
        pos = [
            [0,1],
        ]

        for el in pos:
            if curr[0] + el[0] <= 8 and curr[0] + el[0] >= 1 and curr[1] + el[1] <= 8 and curr[1] + el[1] >= 1:
                l.append(conversion([curr[0]+el[0], curr[1] + el[1]]))

        return l

    if black:

        l =[]

        pos = [
            [0,-1]
            ]

        for el in pos:

            if curr[1] - abs(el[1]) >= 1 and curr[1] - abs(el[1]) <= 8:
                l.append(conversion([curr[0]+el[0], curr[1] + el[1]]))

        return l




def possible_pawn_take(curr, black = False):

    if not black:

        l = []

        pos = [

            [1,1],
            [-1,1]
        ]

        for el in pos:

            if curr[0] + el[0] <= 8 and curr[0] + el[0] >= 1 and curr[1] + el[1] <= 8 and curr[1] + el[1] >= 1:
                l.append(conversion([curr[0]+el[0], curr[1] + el[1]]))

        return l
    
    if black:

        l = []

        pos = [

            [-1,-1],
            [1,-1]
        ]

        for el in pos:

            if curr[0] + el[0] <= 8 and curr[0] + el[0] >= 1 and curr[1] + el[1] <= 8 and curr[1] + el[1] >= 1:
                l.append(conversion([curr[0]+el[0], curr[1] + el[1]]))

        return l



def possible_pawn_start(curr, black=False):

    if not black:
        return conversion([curr[0], curr[1]+2])
    
    else:
        return conversion([curr[0], curr[1]-2])
    



# converting from [1,1] to 'a1'

def conversion(curr):

    literki = ['xxx', 'a', 'b','c','d','e','f','g','h']

    cyferki = ['xxx', '1','2','3','4','5','6','7','8']

    return  literki[curr[0]] + cyferki[curr[1]]


# converting from 'a1' to [1,1]


def conversion2(curr):

    d = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8}


    return [d[curr[0]], int(curr[1])]


# i made this func to check for possible moves for every piece after every move. If first move is e4, then queen can go to e2, f3 etc.

def update_all():

    for k,v in white_pieces.items():

        if k[0] == 'Q':
            v[1] = possible_queen(conversion2(v[0]))

        elif k[0] == 'R':
            v[1] = possible_rook(conversion2(v[0]))

        elif k[0] == 'B':
            v[1] = possible_bishop(conversion2(v[0]))

        elif k[0] == 'N':
            v[1] = possible_knight(conversion2(v[0]))

        elif k[0] == 'K':
            v[1] = possible_king(conversion2(v[0]))

        elif k[0] == 'P':
            v[1] = possible_pawn(conversion2(v[0]))
            v[2] = possible_pawn_take(conversion2(v[0]))

    for k,v in black_pieces.items():

        if k[0] == 'q':
            v[1] = possible_queen(conversion2(v[0]), white=False)

        elif k[0] == 'r':
            v[1] = possible_rook(conversion2(v[0]), white=False)

        elif k[0] == 'b':
            v[1] = possible_bishop(conversion2(v[0]), white=False)

        elif k[0] == 'n':
            v[1] = possible_knight(conversion2(v[0]), white=False)

        elif k[0] == 'k':
            v[1] = possible_king(conversion2(v[0]), white=False)

        elif k[0] == 'p':
            v[1] = possible_pawn(conversion2(v[0]), black=True)
            v[2] = possible_pawn_take(conversion2(v[0]), black=True)





pawnlet = 'abcdefgh'

# starting positions

# when it comes to all pieces that are not pawns, index zero of values is their current position and index 1 are all possible moves.
# 
# pawns on index zero have curr position, on index one possible move, on index2 possible capture and on index 3 possible starting move

white_pieces = {'P1': ['a2', ['a3'], ['b3'], 'a4'], 'P2': ['b2', ['b3'], ['c3', 'a3'], 'b4'], 'P3': ['c2', ['c3'], ['d3', 'b3'], 'c4'], 
'P4': ['d2', ['d3'], ['e3', 'c3'], 'd4'], 'P5': ['e2', ['e3'], ['f3', 'd3'], 'e4'], 'P6': ['f2', ['f3'], ['g3', 'e3'], 'f4'],
'P7': ['g2', ['g3'], ['h3', 'f3'], 'g4'], 'P8': ['h2', ['h3'], ['g3'], 'h4'],
'B1': ['c1', []], 
'B2': ['f1', []], 
'N1': ['b1', ['a3', 'c3']],
'N2': ['g1', ['f3', 'h3']],
'R1': ['a1', []], 
'R2': ['h1', []],
'Q1': ['d1', []],
'K': ['e1', []]}



black_pieces = {'p1': ['a7', ['a6'], ['b6'], 'a5'], 'p2': ['b7', ['b6'], ['a6', 'c6'], 'b5'], 'p3': ['c7', ['c6'], ['b6', 'd6'], 'c5'],
'p4': ['d7', ['d6'], ['c6', 'e6'], 'd5'], 'p5': ['e7', ['e6'], ['d6', 'f6'], 'e5'], 'p6': ['f7', ['f6'], ['e6', 'g6'], 'f5'], 
'p7': ['g7', ['g6'], ['f6', 'h6'], 'g5'], 'p8': ['h7', ['h6'], ['g6'], 'h5'],
'b1': ['c8', []],
'b2': ['f8', []],
'n1': ['b8', ['a6', 'c6']],
'n2': ['g8', ['f6', 'h6']], 
'r1': ['a8', []], 
'r2': ['h8', []], 
'q1': ['d8', []],
'k': ['e8', []]}




game = ''
moves = ' '.join([el for el in game.split() if not el.endswith('.')])
moves = moves.replace('#', '').replace('+', '')
moves = ' '.join(moves.split())
text = ''

for i,el in enumerate(moves.split()):

    if i % 2 == 0:

        # castle

        if el == 'O-O':

            white_pieces['K'][0] = 'g1'
            white_pieces['R2'][0] = 'f1'
            white_pieces['K'][1] = possible_king(conversion2(white_pieces['K'][0]))
            white_pieces['R2'][1] = possible_rook(conversion2(white_pieces['R2'][0]))
            text += 'e1g1' + ' '
            update_all()

        elif el == 'O-O-O':

            white_pieces['K'][0] = 'c1'
            white_pieces['R1'][0] = 'd1'
            white_pieces['K'][1] = possible_king(conversion2(white_pieces['K'][0]))
            white_pieces['R1'][1] = possible_rook(conversion2(white_pieces['R1'][0]))
            text += 'e1c1' + ' '
            update_all()

        # pawn moves

        if el[0] in pawnlet:

            for k,v in white_pieces.items():

                if k[0] == 'P':

                    if v[3] == el:
                        text += v[0] + el + ' '
                        v[0] = el
                        v[1] = possible_pawn(conversion2(v[0]))
                        v[2] = possible_pawn_take(conversion2(v[0]))
                        v[3] = None
                        update_all()

                    elif el in v[1]:
                        text += v[0] + el + ' '
                        v[0] = el
                        v[1] = possible_pawn(conversion2(v[0]))
                        v[2] = possible_pawn_take(conversion2(v[0]))
                        v[3] = None
                        update_all()

                    elif el[2:] in v[2] and v[0][0] == el[0]:

                        for k2,v2 in black_pieces.items():
                                
                            if el[2:] == v2[0]:
                                del black_pieces[k2]
                                break

                        text += v[0] + el[2:] + ' '
                        v[0] = el[2:]
                        v[1] = possible_pawn(conversion2(v[0]))
                        v[2] = possible_pawn_take(conversion2(v[0]))
                        v[3] = None
                        update_all()

        elif el[0] == 'Q':

            # basic move, Qe5   

            if len(el) == 3:

                for k,v in white_pieces.items():

                    if k[0] == 'Q':

                        if el[1:] in v[1]:
                            text += v[0] + el[1:] + ' '
                            v[0] = el[1:]
                            v[1] = possible_queen(conversion2(v[0]))
                            update_all()

            # take, Qxe5

            if len(el) == 4 and el[1] == 'x':

                for k,v in white_pieces.items():

                    if k[0] == 'Q':

                        if el[2:] in v[1]:

                            for k2,v2 in black_pieces.items():

                                if el[2:] == v2[0]:
                                    del black_pieces[k2]
                                    break

                            text += v[0] + el[2:] + ' '
                            v[0] = el[2:]
                            v[1] = possible_queen(conversion2(v[0]))
                            update_all()

            # Q4e5

            if len(el) == 4 and el[1] in ['1','2','3','4','5','6','7','8']:

                for k,v in white_pieces.items():

                    if k[0] == 'Q':

                        if v[0][1] == el[1] and el[2:] in v[1]:

                            for k2,v2 in black_pieces.items():

                                if el[2:] == v2[0]:
                                    del black_pieces[k2]
                                    break

                            text += v[0] + el[2:] + ' '
                            v[0] = el[2:]
                            v[1] = possible_queen(conversion2(v[0]))
                            update_all()

            # Qfe5

            if len(el) == 4 and el[1] in ['a','b','c','d','e','f','g','h']:

                for k,v in white_pieces.items():

                    if k[0] == 'Q':

                        if v[0][0] == el[1] and el[2:] in v[1]:

                            for k2,v2 in black_pieces.items():

                                if el[2:] == v2[0]:
                                    del black_pieces[k2]
                                    break

                            text += v[0] + el[2:] + ' '
                            v[0] = el[2:]
                            v[1] = possible_queen(conversion2(v[0]))
                            update_all()

            # situation when there are two queens that can take the same piece

            # 1. Qfxe5

            if len(el) == 5 and el[2] == 'x':

                for k,v in white_pieces.items():

                    if k[0] == 'Q':

                        if v[0][0] == el[1] and el[3:] in v[1]:

                            for k2,v2 in black_pieces.items():

                                if el[3:] == v2[0]:
                                    del black_pieces[k2]
                                    break

                            text += v[0] + el[3:] + ' '
                            v[0] = el[3:]
                            v[1] = possible_queen(conversion2(v[0]))
                            update_all()

            # 2. Q4xe5

            if len(el) == 5 and el[1] in ['1','2','3','4','5','6','7','8']:

                for k,v in white_pieces.items():

                    if k[0] == 'Q':

                        if v[0][1] == el[1] and el[3:] in v[1]:

                            for k2,v2 in black_pieces.items():

                                if el[3:] == v2[0]:
                                    del black_pieces[k2]
                                    break

                            text += v[0] + el[3:] + ' '
                            v[0] = el[3:]
                            v[1] = possible_queen(conversion2(v[0]))
                            update_all()
    
        elif el[0] == 'K':

            if len(el) == 3:

                for k,v in white_pieces.items():

                    if k[0] == 'K':

                        if el[1:] in v[1]:
                            text += v[0] + el[1:] + ' '
                            v[0] = el[1:]
                            v[1] = possible_king(conversion2(v[0]))
                            update_all()

            elif len(el) == 4:

                for k,v in white_pieces.items():

                    if k[0] == 'K':

                        if el[1:] in v[1]:

                            for k2,v2 in black_pieces.items():

                                if el[1:] == v2[0]:
                                    del black_pieces[k2]
                                    break

                            text += v[0] + el[1:] + ' '
                            v[0] = el[1:]
                            v[1] = possible_king(conversion2(v[0]))
                            update_all()

        elif el[0] == 'N':

            if len(el) == 3:
            
                for k,v in white_pieces.items():
        
                    if k[0] == 'N':
        
                        if el[1:] in v[1]:
                            text += v[0] + el[1:] + ' '
                            v[0] = el[1:]
                            v[1] = possible_knight(conversion2(v[0]))
                            update_all()

            if len(el) == 4 and el[1] == 'x':

                for k,v in white_pieces.items():

                    if k[0] == 'N':

                        if el[2:] in v[1]:

                            for k2,v2 in black_pieces.items():

                                if el[2:] == v2[0]:
                                    del black_pieces[k2]
                                    break

                            text += v[0] + el[2:] + ' '
                            v[0] = el[2:]
                            v[1] = possible_knight(conversion2(v[0]))
                            update_all()

            # Nfe5

            if len(el) == 4 and 'x' not in el and el[1] in ['a','b','c','d','e','f','g','h']:

                for k,v in white_pieces.items():

                    if k[0] == 'N':

                        if el[1] == v[0][0] and el[2:] in v[1]:

                            for k2,v2 in black_pieces.items():

                                if el[2:] == v2[0]:
                                    del black_pieces[k2]
                                    break

                            text += v[0] + el[2:] + ' '
                            v[0] = el[2:]
                            v[1] = possible_knight(conversion2(v[0]))
                            update_all()

            # N4e5

            if len(el) == 4 and 'x' not in el and el[1] in ['1','2','3','4','5','6','7','8']:

                for k,v in white_pieces.items():

                    if k[0] == 'N':

                        if el[1] == v[0][1] and el[2:] in v[1]:

                            for k2,v2 in black_pieces.items():

                                if el[2:] == v2[0]:
                                    del black_pieces[k2]
                                    break

                            text += v[0] + el[2:] + ' '
                            v[0] = el[2:]
                            v[1] = possible_knight(conversion2(v[0]))
                            update_all()


            # Nfxe5

            if len(el) == 5 and el[1] in ['a','b','c','d','e','f','g','h']:

                for k,v in white_pieces.items():

                    if k[0] == 'N':

                        if el[3:] in v[1]:

                            for k2,v2 in black_pieces.items():

                                if el[3:] == v2[0]:
                                    del black_pieces[k2]
                                    break

                            text += v[0] + el[3:] + ' '
                            v[0] = el[3:]
                            v[1] = possible_knight(conversion2(v[0]))
                            update_all() 

            # N4xe5
            if len(el) == 5 and el[1] in ['1','2','3','4','5','6','7','8']:

                for k,v in white_pieces.items():

                    if k[0] == 'N':

                        if el[3:] in v[1]:

                            for k2,v2 in black_pieces.items():

                                if el[3:] == v2[0]:
                                    del black_pieces[k2]
                                    break

                            text += v[0] + el[3:] + ' '
                            v[0] = el[3:]
                            v[1] = possible_knight(conversion2(v[0]))
                            update_all()

        elif el[0] == 'B':

            if len(el) == 3:

                for k,v in white_pieces.items():

                    if k[0] == 'B':

                        if el[1:] in v[1]:
                            text += v[0] + el[1:] + ' '
                            v[0] = el[1:]
                            v[1] = possible_bishop(conversion2(v[0]))
                            update_all()


            elif len(el) == 4 and el[1] == 'x':

                for k,v in white_pieces.items():

                    if k[0] == 'B':

                        if el[2:] in v[1]:

                            for k2,v2 in black_pieces.items():

                                if el[2:] == v2[0]:
                                    del black_pieces[k2]
                                    break

                            text += v[0] + el[2:] + ' '
                            v[0] = el[2:]
                            v[1] = possible_bishop(conversion2(v[0]))
                            update_all()

        elif el[0] == 'R':

            if len(el) == 3:

                for k,v in white_pieces.items():

                    if k[0] == 'R':

                        if el[1:] in v[1]:
                            text += v[0] + el[1:] + ' '
                            v[0] = el[1:]
                            v[1] = possible_rook(conversion2(v[0]))
                            update_all()

            elif len(el) == 4 and el[1] == 'x':

                for k,v in white_pieces.items():

                    if k[0] == 'R':

                        if el[2:] in v[1]:

                            for k2,v2 in black_pieces.items():

                                if el[2:] == v2[0]:
                                    del black_pieces[k2]
                                    break

                            text += v[0] + el[2:] + ' '
                            v[0] = el[2:]
                            v[1] = possible_rook(conversion2(v[0]))
                            update_all()

            # Rfe5                

            elif len(el) == 4 and 'x' not in el and el[1] in ['a','b','c','d','e','f','g','h']:

                for k,v in white_pieces.items():

                    if k[0] == 'R':

                        if el[2:] in v[1]:

                            for k2,v2 in black_pieces.items():

                                if el[2:] == v2[0]:
                                    del black_pieces[k2]
                                    break

                            text += v[0] + el[2:] + ' '
                            v[0] = el[2:]
                            v[1] = possible_rook(conversion2(v[0]))
                            update_all()

            # R4e5

            elif len(el) == 4 and 'x' not in el and el[1] in ['1','2','3','4','5','6','7','8']:

                for k,v in white_pieces.items():

                    if k[0] == 'R':

                        if el[2:] in v[1]:

                            for k2,v2 in black_pieces.items():

                                if el[2:] == v2[0]:
                                    del black_pieces[k2]
                                    break

                            text += v[0] + el[2:] + ' '
                            v[0] = el[2:]
                            v[1] = possible_rook(conversion2(v[0]))
                            update_all()

            # Rfxe5

            elif len(el) == 5 and el[1] in ['a','b','c','d','e','f','g','h']:

                for k,v in white_pieces.items():

                    if k[0] == 'R':

                        if el[3:] in v[1]:

                            for k2,v2 in black_pieces.items():

                                if el[3:] == v2[0]:
                                    del black_pieces[k2]
                                    break

                            text += v[0] + el[3:] + ' '
                            v[0] = el[3:]
                            v[1] = possible_rook(conversion2(v[0]))
                            update_all()

            # R4xe5

            elif len(el) == 5 and el[1] in ['1','2','3','4','5','6','7','8']:

                for k,v in white_pieces.items():

                    if k[0] == 'R':

                        if el[3:] in v[1]:

                            for k2,v2 in black_pieces.items():

                                if el[3:] == v2[0]:
                                    del black_pieces[k2]
                                    break

                            text += v[0] + el[3:] + ' '
                            v[0] = el[3:]
                            v[1] = possible_rook(conversion2(v[0]))
                            update_all()


    elif i % 2 == 1:

        # castle

        if el == 'O-O':

            black_pieces['k'][0] = 'g8'
            black_pieces['r2'][0] = 'f8'
            black_pieces['k'][1] = possible_king(conversion2(black_pieces['k'][0]), white=False)
            black_pieces['r2'][1] = possible_rook(conversion2(black_pieces['r2'][0]), white=False)
            text += 'e8g8' + ' '
            update_all()

        elif el == 'O-O-O':

            black_pieces['k'][0] = 'c8'
            black_pieces['r1'][0] = 'd8'
            black_pieces['k'][1] = possible_king(conversion2(black_pieces['k'][0]), white=False)
            black_pieces['r1'][1] = possible_rook(conversion2(black_pieces['r1'][0]), white=False)
            text += 'e8c8' + ' '
            update_all()

        # pawn moves

        if el[0] in pawnlet:

            for k,v in black_pieces.items():

                if k[0] == 'p':

                    if v[3] == el:
                        text += v[0] + el + ' '
                        v[0] = el
                        v[1] = possible_pawn(conversion2(v[0]), black=True)
                        v[2] = possible_pawn_take(conversion2(v[0]), black=True)
                        v[3] = None
                        update_all()

                    elif el in v[1]:
                        text += v[0] + el + ' '
                        v[0] = el
                        v[1] = possible_pawn(conversion2(v[0]), black=True)
                        v[2] = possible_pawn_take(conversion2(v[0]), black=True)
                        v[3] = None
                        update_all()

                    elif el[2:] in v[2] and v[0][0] == el[0] :
                            
                        for k2,v2 in white_pieces.items():
                                    
                            if el[2:] == v2[0] and el[0] == v2[0][0]:
                                del white_pieces[k2]
                                break
    
                        text += v[0] + el[2:] + ' '
                        v[0] = el[2:]
                        v[1] = possible_pawn(conversion2(v[0]), black=True)
                        v[2] = possible_pawn_take(conversion2(v[0]), black=True)
                        v[3] = None
                        update_all()

        elif el[0] == 'Q':

            # basic move, Qe5   

            if len(el) == 3:

                for k,v in black_pieces.items():

                    if k[0] == 'q':

                        if el[1:] in v[1]:
                            text += v[0] + el[1:] + ' '
                            v[0] = el[1:]
                            v[1] = possible_queen(conversion2(v[0]), white=False)
                            update_all()

            # take, Qxe5

            if len(el) == 4 and el[1] == 'x':

                for k,v in black_pieces.items():

                    if k[0] == 'q':

                        if el[2:] in v[1]:

                            for k2,v2 in white_pieces.items():

                                if el[2:] == v2[0]:
                                    del white_pieces[k2]
                                    break

                            text += v[0] + el[2:] + ' '
                            v[0] = el[2:]
                            v[1] = possible_queen(conversion2(v[0]), white=False)
                            update_all()


            # Q4e5

            if len(el) == 4 and el[1] in ['1','2','3','4','5','6','7','8']:

                for k,v in black_pieces.items():

                    if k[0] == 'q':

                        if v[0][1] == el[1] and el[2:] in v[1]:

                            for k2,v2 in white_pieces.items():

                                if el[2:] == v2[0]:
                                    del white_pieces[k2]
                                    break

                            text += v[0] + el[2:] + ' '
                            v[0] = el[2:]
                            v[1] = possible_queen(conversion2(v[0]), white=False)
                            update_all()

            # Qfe5

            if len(el) == 4 and el[1] in ['a','b','c','d','e','f','g','h']:

                for k,v in black_pieces.items():

                    if k[0] == 'q':

                        if v[0][0] == el[1] and el[2:] in v[1]:

                            for k2,v2 in white_pieces.items():

                                if el[2:] == v2[0]:
                                    del white_pieces[k2]
                                    break

                            text += v[0] + el[2:] + ' '
                            v[0] = el[2:]
                            v[1] = possible_queen(conversion2(v[0]), white=False)
                            update_all()

            # situation when there are two queens that can take the same piece

            # 1. Qfxe5

            if len(el) == 5 and el[2] == 'x':

                for k,v in black_pieces.items():

                    if k[0] == 'q':

                        if v[0][0] == el[1] and el[3:] in v[1]:

                            for k2,v2 in white_pieces.items():

                                if el[3:] == v2[0]:
                                    del white_pieces[k2]
                                    break

                            text += v[0] + el[3:] + ' '
                            v[0] = el[3:]
                            v[1] = possible_queen(conversion2(v[0]), white=False)
                            update_all()

            # 2. Q4xe5

            if len(el) == 5 and el[1] in ['1','2','3','4','5','6','7','8']:

                for k,v in black_pieces.items():

                    if k[0] == 'q':

                        if v[0][1] == el[1] and el[3:] in v[1]:

                            for k2,v2 in white_pieces.items():

                                if el[3:] == v2[0]:
                                    del white_pieces[k2]
                                    break

                            text += v[0] + el[3:] + ' '
                            v[0] = el[3:]
                            v[1] = possible_queen(conversion2(v[0]), white=False)
                            update_all()

        elif el[0] == 'K':

            if len(el) == 3:

                for k,v in black_pieces.items():

                    if k[0] == 'k':

                        if el in v[1]:
                            text += v[0] + el[1:] + ' '
                            v[0] = el[1:]
                            v[1] = possible_king(conversion2(v[0]), white=False)
                            update_all()

            elif len(el) == 4:

                for k,v in black_pieces.items():

                    if k[0] == 'k':

                        if el[2:] in v[1]:

                            for k2,v2 in white_pieces.items():

                                if el[2:] == v2[0]:
                                    del white_pieces[k2]
                                    break

                            text += v[0] + el[2:] + ' '
                            v[0] = el[2:]
                            v[1] = possible_king(conversion2(v[0]), white=False)
                            update_all()


        elif el[0] == 'N':

            if len(el) == 3:
            
                for k,v in black_pieces.items():
        
                    if k[0] == 'n':
        
                        if el[1:] in v[1]:
                            text += v[0] + el[1:] + ' '
                            v[0] = el[1:]
                            v[1] = possible_knight(conversion2(v[0]), white=False)
                            update_all()

            if len(el) == 4 and el[1] == 'x':

                for k,v in black_pieces.items():

                    if k[0] == 'n':

                        if el[2:] in v[1]:

                            for k2,v2 in white_pieces.items():

                                if el[2:] == v2[0]:
                                    del white_pieces[k2]
                                    break

                            text += v[0] + el[2:] + ' '
                            v[0] = el[2:]
                            v[1] = possible_knight(conversion2(v[0]), white=False)
                            update_all()

            # Nfe5

            if len(el) == 4 and 'x' not in el and el[1] in ['a','b','c','d','e','f','g','h']:

                for k,v in black_pieces.items():

                    if k[0] == 'n':

                        if el[1] == v[0][0] and el[2:] in v[1]:

                            for k2,v2 in white_pieces.items():

                                if el[2:] == v2[0]:
                                    del white_pieces[k2]
                                    break

                            text += v[0] + el[2:] + ' '
                            v[0] = el[2:]
                            v[1] = possible_knight(conversion2(v[0]), white=False)
                            update_all()

            # N4e5

            if len(el) == 4 and 'x' not in el and el[1] in ['1','2','3','4','5','6','7','8']:

                for k,v in black_pieces.items():

                    if k[0] == 'n':

                        if el[1] == v[0][1] and el[2:] in v[1]:

                            for k2,v2 in white_pieces.items():

                                if el[2:] == v2[0]:
                                    del white_pieces[k2]
                                    break

                            text += v[0] + el[2:] + ' '
                            v[0] = el[2:]
                            v[1] = possible_knight(conversion2(v[0]), white=False)
                            update_all()


            # Nfxe5

            if len(el) == 5 and el[1] in ['a','b','c','d','e','f','g','h']:

                for k,v in black_pieces.items():

                    if k[0] == 'n':

                        if el[3:] in v[1]:

                            for k2,v2 in white_pieces.items():

                                if el[3:] == v2[0]:
                                    del white_pieces[k2]
                                    break

                            text += v[0] + el[3:] + ' '
                            v[0] = el[3:]
                            v[1] = possible_knight(conversion2(v[0]), white=False)
                            update_all() 

            # N4xe5
            if len(el) == 5 and el[1] in ['1','2','3','4','5','6','7','8']:

                for k,v in black_pieces.items():

                    if k[0] == 'n':

                        if el[4:] in v[1]:

                            for k2,v2 in white_pieces.items():

                                if el[3:] == v2[0]:
                                    del white_pieces[k2]
                                    break

                            text += v[0] + el[3:] + ' '
                            v[0] = el[3:]
                            v[1] = possible_knight(conversion2(v[0]), white=False)
                            update_all()

        elif el[0] == 'R':

            if len(el) == 3:

                for k,v in black_pieces.items():

                    if k[0] == 'r':

                        if el[1:] in v[1]:
                            text += v[0] + el[1:] + ' '
                            v[0] = el[1:]
                            v[1] = possible_rook(conversion2(v[0]), white=False)
                            update_all()

            elif len(el) == 4 and el[1] == 'x':

                for k,v in black_pieces.items():

                    if k[0] == 'r':

                        if el[2:] in v[1]:

                            for k2,v2 in white_pieces.items():

                                if el[2:] == v2[0]:
                                    del white_pieces[k2]
                                    break

                            text += v[0] + el[2:] + ' '
                            v[0] = el[2:]
                            v[1] = possible_rook(conversion2(v[0]), white=False)
                            update_all()

            # Rfe5                

            elif len(el) == 4 and 'x' not in el and el[1] in ['a','b','c','d','e','f','g','h']:

                for k,v in black_pieces.items():

                    if k[0] == 'r':

                        if el[2:] in v[1]:

                            for k2,v2 in white_pieces.items():

                                if el[2:] == v2[0]:
                                    del white_pieces[k2]
                                    break

                            text += v[0] + el[2:] + ' '
                            v[0] = el[2:]
                            v[1] = possible_rook(conversion2(v[0]), white=False)
                            update_all()

            # R4e5

            elif len(el) == 4 and 'x' not in el and el[1] in ['1','2','3','4','5','6','7','8']:

                for k,v in black_pieces.items():

                    if k[0] == 'r':

                        if el[2:] in v[1]:

                            for k2,v2 in white_pieces.items():

                                if el[2:] == v2[0]:
                                    del white_pieces[k2]
                                    break

                            text += v[0] + el[2:] + ' '
                            v[0] = el[2:]
                            v[1] = possible_rook(conversion2(v[0]), white=False)
                            update_all()

            # Rfxe5

            elif len(el) == 5 and el[1] in ['a','b','c','d','e','f','g','h']:

                for k,v in black_pieces.items():

                    if k[0] == 'r':

                        if el[3:] in v[1]:

                            for k2,v2 in white_pieces.items():

                                if el[3:] == v2[0]:
                                    del white_pieces[k2]
                                    break

                            text += v[0] + el[3:] + ' '
                            v[0] = el[3:]
                            v[1] = possible_rook(conversion2(v[0]), white=False)
                            update_all()

            # R4xe5

            elif len(el) == 5 and el[1] in ['1','2','3','4','5','6','7','8']:

                for k,v in black_pieces.items():

                    if k[0] == 'r':

                        if el[3:] in v[1]:

                            for k2,v2 in white_pieces.items():

                                if el[3:] == v2[0]:
                                    del white_pieces[k2]
                                    break

                            text += v[0] + el[3:] + ' '
                            v[0] = el[3:]
                            v[1] = possible_rook(conversion2(v[0]), white=False)
                            update_all()

        elif el[0] == 'B':

            if len(el) == 3:

                for k,v in black_pieces.items():

                    if k[0] == 'b':

                        if el[1:] in v[1]:

                            text += v[0] + el[1:] + ' '
                            v[0] = el[1:]
                            v[1] = possible_bishop(conversion2(v[0]), white=False)
                            update_all()

            if len(el) == 4 and el[1] == 'x':

                for k,v in black_pieces.items():

                    if k[0] == 'b':

                        if el[2:] in v[1]:

                            for k2,v2 in white_pieces.items():

                                if el[2:] == v2[0]:
                                    del white_pieces[k2]
                                    break

                            text += v[0] + el[2:] + ' '
                            v[0] = el[2:]
                            v[1] = possible_bishop(conversion2(v[0]), white=False)
                            update_all()



def board_repr():

    board = [[" " for _ in range(1,9)] for _ in range(1,9)]
    

    for k,v in white_pieces.items():
        pos = conversion2(v[0])
        board[pos[1]-1][pos[0]-1] = k[0]

    for k,v in black_pieces.items():
        pos = conversion2(v[0])
        board[pos[1]-1][pos[0]-1] = k[0]

    for row in board:
        print(row)



def convert_to_fen(board, separator='.'):
    
    fen = ""
    
    for row in board:
        ec = 0
        for el in row:
            if el == separator:
                ec += 1
            else:
                if ec > 0:
                    fen += str(ec)
                    ec = 0
                
                if el[0] == 'P':
                    fen += 'P'
                elif el[0] == 'R':
                    fen += 'R'
                elif el[0] == 'H':
                    fen += 'N'
                elif el[0] == 'B':
                    fen += 'B'
                elif el[0] == 'Q':
                    fen += 'Q'
                elif el[0] == 'K':
                    fen += 'K'
                elif el[0] == 'p':
                    fen += 'p'
                elif el[0] == 'r':
                    fen += 'r'
                elif el[0] == 'h':
                    fen += 'n'
                elif el[0] == 'b':
                    fen += 'b'
                elif el[0] == 'q':
                    fen += 'q'
                elif el[0] == 'k':
                    fen += 'k'
        
        if ec > 0:
            fen += str(ec)
        
        fen += '/'
    
    fen = fen[:-1]
    
    fen += ' w - - 0 1'
    
    return fen

def is_square_occupied(pos : str) -> bool:

    l = [pc[0] for pc in white_pieces.values()] + [pc[0] for pc in black_pieces.values()]
    
    return pos in l

def is_square_attacked(pos : str) -> bool:
    l = []

    for k,v in black_pieces.items():

        if k[0] != 'p':
            l += v[1]
        else:    
            l += v[2]

    for k,v in white_pieces.items():
            
        if k[0] != 'P':
            l += v[1]
        else:
            l += v[2]

    return pos in l
