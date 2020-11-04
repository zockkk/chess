import pickle

with open('Slony', 'rb') as f:
    slony = pickle.load(f)
with open('Ferzi', 'rb') as f:
    ferzi = pickle.load(f)
with open('Koni', 'rb') as f:
    koni = pickle.load(f)
with open('Ladyi', 'rb') as f:
    ladyi = pickle.load(f)
with open('Koroli', 'rb') as f:
    koroli = pickle.load(f)

k = 0
for i in range(16):
    k += 2 ** i

for i in range(48, 64):
    k += 2 ** i

rook_bit = []
z = 0
for k in range(64):
    for i in range(8):
        for j in range(8):
            if k == i * 8 + j:
                z += 2 ** (8 * i + j)
                for o in range(8):
                    if o != j:
                        z += 2 ** (8 * i + o)
                for o in range(8):
                    if o != i:
                        z += 2 ** (8 * o + j)
    rook_bit.append(z)
    z = 0

queen_bit = []
for matrix in ferzi:
    for i in range(8):
        for j in range(8):
            if matrix[i][j] == 1:
                z += 2 ** (8 * i + j)
    queen_bit.append(z)
    z = 0

bishop_bit = []
for matrix in slony:
    for i in range(8):
        for j in range(8):
            if matrix[i][j] == 1:
                z += 2 ** (8 * i + j)
    bishop_bit.append(z)
    z = 0

knight_bit = []
for matrix in koni:
    for i in range(8):
        for j in range(8):
            if matrix[i][j] == 1:
                z += 2 ** (8 * i + j)
    knight_bit.append(z)
    z = 0

flags = []

white_pawn_silence = []
for k in range(8, 64):
    for i in range(1, 8):
        for j in range(8):
            if 8 * i + j == k:
                z += 2 ** (8 * i + j)
                if i == 1:
                    z += 2 ** (8 + j) + 2 ** (16 + j)
                else:
                    z += 2 ** (8 * i + j)
                white_pawn_silence.append(z)
                z = 0

white_pawn_eat = []
for k in range(8, 64):
    for i in range(1, 8):
        for j in range(8):
            if 8 * i + j == k:
                z += 2 ** (8 * i + j)
                if j < 7 and j > 0:
                    z += 2 ** (8 * (i + 1) + j + 1) + 2 ** (8 * (i + 1) + j - 1)
                elif j < 7:
                    z += 2 ** (8 * (i + 1) + j + 1)
                elif j > 0:
                    z += 2 ** (8 * (i + 1) + j - 1)
                white_pawn_eat.append(z)
                z = 0

black_pawn_silence = []
for k in range(56):
    for i in range(7):
        for j in range(8):
            if 8 * i + j == k:
                z += 2 ** (8 * i + j)
                if i == 6:
                    z += 2 ** (8*i - j) + 2 ** (8*(i+1) - j)
                else:
                    z += 2 ** (8 * i + j)
                black_pawn_silence.append(z)
                z = 0

black_pawn_eat = []
for k in range(56, -1, -1):
    for i in range(7):
        for j in range(8):
            if 8 * i + j == k:
                z += 2 ** (8 * i + j)
                if j < 7 and j > 0:
                    z += 2 ** (8 * (i - 1) + j + 1) + 2 ** (8 * (i - 1) + j - 1)
                elif j < 7:
                    z += 2 ** (8 * (i - 1) + j + 1)
                elif j > 0:
                    z += 2 ** (8 * (i - 1) + j - 1)
                black_pawn_eat.append(z)
                z = 0

king_bit = []
for matrix in koroli:
    for i in range(8):
        for j in range(8):
            if matrix[i][j] == 1:
                z += 2 ** (8 * i + j)
    king_bit.append(z)
    z = 0
