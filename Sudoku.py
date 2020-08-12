prob = [
    [0,0,0,2,4,7,0,0,0],
    [0,0,0,1,0,0,0,7,0],
    [1,9,7,0,0,3,5,0,0],
    [0,0,0,0,0,1,0,0,3],
    [0,5,0,0,0,0,0,6,0],
    [0,0,0,0,0,0,9,0,8],
    [6,0,5,0,0,0,0,0,4],
    [0,3,0,9,0,8,0,0,0],
    [0,0,9,0,7,0,3,0,0]
]
#print(prob[0][4])
def display(prob):
    for i in range (len(prob)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - -')
        for j in range(len(prob)):
            if j % 3 ==0 and j != 0:
                print('|', end=' ')
            print(prob[i][j], end=' ')

        print('')

def check(pos,num, prob):
    for i in range(len(prob)):
        if prob[pos[0]][i]==num and pos[1] != i:
            return False

    for i in range(len(prob)):
        if prob[i][pos[1]]==num and pos[0] != i:
            return False

    row=pos[0] // 3
    col=pos[1] // 3

    for i in range(row*3, row*3 + 3):
        for j in range(col*3, col*3 + 3):
            if prob[i][j] == num and (i,j) != 0:
                return False
    return True

def sol(prob):
    z=is_zero(prob)
    if z is None:
        return True
    else:
        row,col=z
    for i in range(1,10):
        if check((row,col),i,prob):
            prob[row][col]=i

            if sol(prob):
                return True

            prob[row][col]=0
    return False



def is_zero(prob):
    for i in range(len(prob)):
        for j in range(len(prob)):
            if prob[i][j]==0:
                return i,j
    return None

display(prob)
sol(prob)
print('')
display(prob)