
''' Title:  Calculates the yoke section
               for the TAC Core '''
from avtral import AVTRAL
def TACOK(DCOR,BSTEP,N,X1,Y1):

    ''' TACOK '''

    ''' Dimensioning of the yoke section '''

    ''' First width '''
    OK=[0. for i in range(N)]
    XG=[0. for i in range(N)]
    
    if (DCOR >=300.) :
        OK[0]=X1[2]+40.
    else:
        OK[0]=X1[2]+20.

    ''' Second width to N-1 width '''

    if (DCOR >= 300.) :
        for I in range(2,N):
            OK[I-1]=X1[I]+40.
  
    else:
        for I in range(2,N):
            OK[I-1]=X1[I]+20.

    ''' Nth width '''

    I=N
    OK[I-1]=X1[I]+20.

    ''' Stepping against yoke '''

    for I in range(1,N+1):
        XG[I-1]=0.

    ''' First Step '''

    M=N
    IX1=1
    XG=AVTRAL(M,IX1,XG,Y1,70.,14.)

    ''' Second Step '''

    IX1=1
    XG=AVTRAL(M,IX1,XG,Y1,40.,70.)

    ''' Outer Stepping '''

    ''' Cut off packets which are sticking up. Max 2.*BSTEP may be cut off.
        Begin with Packet N. '''

    N1=N-1
    for I in range(1,N1+1):
        I1=N+1-I
        TSTEG=0.
        while(XG[I1-1]+OK[I1-1] < XG[I1-2]+OK[I1-2]):
            TSTEG=TSTEG+BSTEP
            if (TSTEG >(2.*BSTEP)):break
            else:OK[I1-2]-= BSTEP
            
    ''' Filling up remaining notches '''

    N1=N-1
    for I in range(1,N1+1):
        while(XG[I]+OK[I] < XG[I-1]+OK[I-1]) :
            OK[I]+= BSTEP

    return XG,OK
