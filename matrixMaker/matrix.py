import math
def print_matrix( matrix ):
    x = ""
    y = ""
    z = ""
    track = ""
    for i in range(len(matrix) - 1):
        x += str(matrix[i][0])
        x += " "
        y += str(matrix[i][1])
        y += " "
        z += str(matrix[i][2])
        z += " "
        track += str(matrix[i][3])
        track += " "
    x += str(matrix[-1][0])
    y += str(matrix[-1][1])
    z += str(matrix[-1][2])
    track += str(matrix[-1][3])
    print(x)
    print(y)
    print(z)
    print(track)

def ident( matrix ):
    lenM = len(matrix)
    for i in range(lenM):
        for j in range(len(matrix[i])):
            if(j != i): matrix[i][j] = 0
            else: matrix[i][j] = 1
    return matrix

def matrix_mult( m1, m2 ):
    for i in range(len(m2)):
        track2 = list(m2[i])
        for j in range(4):
            sum = 0
            sum += m2[i][0] * m1[0][j]
            sum += m2[i][1] * m1[1][j]
            sum += m2[i][2] * m1[2][j]
            sum += m2[i][3] * m1[3][j]
            track2[j] = sum
        m2[i] = track2
    return m2

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
