
''' Title:  Auxiliary optimisation routine '''

from goto import with_goto

@with_goto
def LLP1(M,N,P,E,TD,X,IND,IMIN,THMIN,CHK,IND1,DELMAX,JMAX):

    ''' DUAL is a LOGICAL which should be set to True
        if you need to know the values of the calculated
        DUAL variables and False otherwise '''

    DUAL=True
    LCOL=M+N-P+1
    II=M+1
    KK=M-P+2
    LL=LCOL-1
    RES=0
    if(KK <= II):
        for I in range(KK,II+1):
            if(E[I-1][LCOL-1] >= 0.0):continue
            for J in range(1,N+1):
                E[I-1][J-1]=-E[I-1][J-1]
            E[I-1][LCOL-1]=-E[I-1][LCOL-1]

    for I in range(2,II+1):
        CHK[I-1]=0

    ''' If there are any equality constraints in the problem,
        the program first goes to PHASE1(OPT115),
        otherwise it goes directly to RCS(30) '''

    if(P !=0):
        CHK,E,GMIN,IM,JMIN,L,RES,IMIN,THMIN=LLP6(CHK,E,K,LCOL,M,N,P,RES,TD)

    if(RES > 0):return

    ''' RCS '''

    label ._30
    L=1
    K=1
    for J in range(1,LL+1):
        if(E[0][J-1] >= (-TD)):continue
        IND[L-1]=J
        L=L+1
        ''' IND[L-1] keeps track of the columns in which E[0][J-1] is negative '''

    II=M+1
    for I in range(2,II+1):
        if(E[I-1][LCOL-1] >=(-TD)):continue
        IND1[K-1]=I
        K=K+1

        ''' IND1[L-1] keeps track of the rows in which E[0][LCOL-1] is negative '''

    if(L != 1):goto ._80

    if(K != 1):goto ._60
    else:
        CHK,RES,X=LLP2 (CHK,DUAL,E,LCOL,M,N)
        goto .end

    label ._60
    if(K != 2):goto ._130

    else:
        for J in range(1,LL+1):
            II=IND1[0]
            if(E[II-1][J-1]<0.0): goto ._130

        RES=4

        ''' If RES=4 then the primal problem has no feasible solutions
            DUAL objective function is unbounded '''

        goto .end

    label ._80
    if(L == 2):
        if(K != 1):goto ._150
        II=M+1
        for I in range(2,II+1):
            JJ=IND[0]
            if(E[I-1][JJ-1] > 0.0):goto ._140
   
        RES=5

        ''' If RES=5 then the primal objective function is unbounded
            DUAL problem has no feasible solutions '''

        goto .end

    if(K == 1):goto ._140
    goto ._150

    ''' R PROPHI ROWTRANS(IMAX,JM) GOTO RCS '''

    
    label ._130
    IMAX,JM,PHIMAX,DELMAX,JMAX=LLP5 (E,IND1,K,LCOL,TD)
    CHK,E,RES=LLP3 (CHK,E,LCOL,M,RES,IMAX,JM)
    if(RES > 0.):goto ._end
    goto ._30
    
    ''' C  PROGRAMMA ROWTRANS(IM,JMIN) GOTO RCS '''

    label ._140
    E,GMIN,IM,JMIN,THMIN,IMIN=LLP4 (E,IND,IM,L,LCOL,M,TD)
    CHK,E,RES=LLP3(CHK,E,LCOL,M,RES,IM,JMIN)
    if(RES > 0.):goto .end
    goto ._30

    ''' S  PROGRAMMA PROPHI '''

    label ._150
    E,GMIN,IM,JMIN,THMIN,IMIN=LLP4 (E,IND,IM,L,LCOL,M,TD)
    IMAX,JM,PHIMAX,DELMAX,JMAX=LLP5 (E,IND1,K,LCOL,TD)

    if(GMIN != 1E6):
        CHK,E,RES=LLP3 (CHK,E,LCOL,M,RES,IMAX,JM)
        if(RES > 0.):goto .end
        goto ._30
        
    if(PHIMAX != (-1E6)):
        CHK,E,RES=LLP3 (CHK,E,LCOL,M,RES,IM,JMIN)
        if(RES > 0.):goto .end
        goto ._30    

    if(abs(PHIMAX) <= abs(GMIN)):
        CHK,E,RES=LLP3 (CHK,E,LCOL,M,RES,IM,JMIN)
        if(RES > 0.):goto .end
        goto ._30

    CHK,E,RES=LLP3 (CHK,E,LCOL,M,RES,IMAX,JM)
    if(RES<=0):goto ._30

    ''' Last '''
    label .end
    return E,RES,X,IND,IMIN,THMIN,CHK,IND1,DELMAX,JMAX

''' 
M      = The No. of constraints of which the last
          P are equality constraints
N      = The No. of variables
E      = A matrix with (M+1) rows and (M+N-P+1) columns
NA     = The size of first index with declaration of
          matrix E in the calling program
TD     = A small positive number which is used to test
          whether a number is non-negative ( > -TD)
X      = A vector such that :
          X(1,N) contains the optimal values of the variables and
          X(N+1,N+M) (only if DUAL is True) contains the optimal
                  values of the DUAL variables corresponding to the
                  LQ-constraints
 RES    = 1 If an optimum has been reached
          2 If there is no solution because the row index
            for the pivot element is zero
          3 If there is no solution because the column index
            for the pivot element is zero
          4 if the primal problem has no feasible solutions,
            DUAL objective function is unbounded.
          5 If the primal objective function is unbounded
            DUAL problem has no feasible solutions.
'''
