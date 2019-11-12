
''' Title: Performs calculations over rows
           to determine the pivot element '''

def LLP5(E,IND1,K,LCOL,TD):

    ''' PHIMAX is set equal to a small number for initialisation purposes '''

    PHIMAX=-1E6
    IMAX=0
    KK=K-1
    LL=LCOL-1

    ''' Calculate '''

    for K1 in range(1,KK+1):
        KL=IND1[K1-1]
        JMAX[KL-1]=0
        DELMAX[KL-1]=-1E6

        for J in range(1,LL+1):

            if(E[KL-1][J-1] <= (-TD)):
                if(E[0][J-1]>=(-TD)):
                    DELTA=E[0][J-1]/E[KL-1][J-1]
                    if(DELTA > DELMAX[KL-1]):
                        DELMAX[KL-1]=DELTA
                        JMAX[KL-1]=J

        PHI=DELMAX[KL-1]*E[KL-1][LCOL-1]
        if(DELMAX[KL-1] ==(-1E6)): PHI=-1E8

        if(PHI > PHIMAX):
            PHIMAX=PHI
            IMAX=IND1[K1-1]

    if(IMAX> 0): JM=JMAX[IMAX-1]

    return IMAX,JM,PHIMAX,DELMAX,JMAX
