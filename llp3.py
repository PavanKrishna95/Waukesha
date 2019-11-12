
''' Title:  Performs the usual tableau transformations
            in a linear programming problem,
            (IM,JMIN) being the pivotal element '''

def LLP3(CHK,E,LCOL,M,RES,IM,JMIN):

    ''' If RES=2 there is no solution
        because the row index for the pivot element is zero '''

    ''' IM = 0 '''

    if(IM == 0):
        RES=2

        ''' If RES=3 there is no solution
            because the column index for the pivot element is zero '''

        ''' JMIN = 0 '''

    elif(JMIN == 0):
        RES=3

        ''' Neither '''

    else:
        DUMMY=E[IM-1][JMIN-1]

        ''' Set E(*) '''

        for J in range(1,LCOL+1):
            E[IM-1][J-1]=E[IM-1][J-1]/DUMMY

        II=M+1

        ''' Set E '''

        for I in range(1,II+1):

            if(I !=IM):
                if(E[I-1][JMIN-1] != 0.0):
                    DUMMY=E[I-1][JMIN-1]

                    for J in range(1,LCOL+1):E[I-1][J-1]=E[I-1][J-1]-E[IM-1][J-1]*DUMMY
        
        CHK[IM-1]=JMIN
    return CHK,E,RES
