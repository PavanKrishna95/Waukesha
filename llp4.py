
''' Title: Performs calculations over columns
           to determine the pivot element '''

def LLP4(E,IND,IM,L,LCOL,M,TD):

    ''' GMIN is set equal to a large number for initialisation purposes '''

    GMIN=1E6
    JMIN=0
    JJ=M+1
    LL=L-1

    for L1 in range(1,LL+1):
        II=IND[L1-1]
        IMIN[II-1]=0
        THMIN[II-1]=1E6

        ''' Calculate '''

        for I in range(2,JJ+1):
    
            if(E[I-1][II-1] >=TD):

                if(E[I-1][LCOL-1] >=(-TD)):
                    THETA=E[I-1][LCOL-1]/E[I-1][II-1]
                    if(THETA < THMIN[II-1]):
                        THMIN[II-1]=THETA
                        IMIN[II-1]=I
            
        GAMMA=THMIN[II-1]*E[0][II-1]
        if(THMIN[II-1] ==1E6):GAMMA=1E8

        ''' Calculate '''

        if(GAMMA < GMIN):
            GMIN=GAMMA
            JMIN=IND[L1-1]

    if(JMIN > 0):IM=IMIN[JMIN-1]

    return E,GMIN,IM,JMIN,THMIN,IMIN
