
''' Title:  Calculates the steps in the core-section
               against the winding '''

def AVTRAL(N,IX1,RK1,TP,AVTR,BMIN):

    IX=0
    BX=0.
    I=1
    while(I <= N):
        BX=BX+TP[I]
        if(BX >= BMIN):
            IX=I
            I=N+1
        else:
            IX=I
            I=I+1
    
    for I in range(IX1,IX+1):
        if(RK1[I-1] < 0.1): RK1[I-1]=AVTR

    IX1=IX
    return RK1
