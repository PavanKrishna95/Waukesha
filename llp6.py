
''' Title:  Applied only to equality constraints, if any '''

from goto import with_goto
@with_goto
def LLP6(CHK,E,K,LCOL,M,N,P,RES,TD):

    for R in range(1,P+1):

        ''' GMIN is set equal to a large number for initialisation purposes '''

        GMIN=1E6
        L=1
        JMIN=0
        FIRST=1
        for J in range(1,N+1):
            THMIN[J-1]=1E6
            if(E[0][J-1] >=(-TD)):continue
            IND[L-1]=J
            L=L+1

        label ._12
        if(L == 1):
            for J in range(1,N+1):
                IND[J-1]=J
            L=N+1
        LJ=L-1
        for K in range(1,LJ+1):
            II=IND[K-1]
            LL=M-P+2
            JJ=M+1
            for I in range(LL,JJ+1):
                if(CHK[I-1]!=0):continue
                if(E[I-1][II-1] <= TD):continue
                THETA=E[I-1][LCOL-1]/E[I-1][II-1]
                if(THETA >= THMIN[II-1]):continue
                THMIN[II-1]=THETA
                IMIN[II-1]=I


            GAMMA=THMIN[II-1]*E[0][II-1]
            if(THMIN[II-1] == 1E6):GAMMA=1E8
            if(GAMMA >= GMIN):continue
            GMIN=GAMMA
            JMIN=IND[K-1]

        if(JMIN==0):
            if(FIRST ==1):
                FIRST=0
                L=1
                goto ._12
            IM=0
            continue

        IM=IMIN[JMIN-1]
        CHK,E,RES=LLP3 (CHK,E,LCOL,M,RES,IM,JMIN)
        if(RES > 0):goto ._end

    label ._end
    return (CHK,E,GMIN,IM,JMIN,L,RES,IMIN,THMIN)
