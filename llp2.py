
''' Title:  Results '''

def LLP2(CHK,DUAL,E,LCOL,M,N):

    X=[0]*10

    JJ=M+1

    ''' Set X '''
    for I in range(2,JJ+1):
        II=CHK[I-1]
        if(CHK[I-1] >N): CHK[I-1]=0
        if(CHK[I-1] > 0): X[II-1]=E[I-1][LCOL-1]

    ''' If DUAL '''

    if(DUAL):
        JJ=LCOL-1
        II=N+1

        ''' Set  '''

        for I in range(II,JJ+1):
            X[I-1]=E[0][I-1]

    ''' If RES=1 the optimum has been found '''

    RES=1

    return CHK,RES,X
