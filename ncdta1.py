
''' Title:  Number of cooling ducts for the TA1 core

    From the TOPOIL and DCORNI determine horizontal location (XLOC)
    in diagram with limits for number of cooling ducts versus Flux density.

    Then compare XLOC with the limits for different number of cooling ducts
    until Limiting polynomial is higher than actual Flux Density. '''

def NCDTA1(DCORNI,TOPOIL,BLIMB,FREQ,ISTGRD,BBSTLP,JFC):
    import numpy
    ''' Input
        DCORNI Net core diameter (m)
        TOPOIL TOP OIL, max average daisy
        BLIMB  Flux density
        FREQ   Frequency
        ISTGRD Steel grade
        BBSTLP Type of jointing FALSE = normal, TRUE = steplap '''

    ''' Output

        NCDTA1 Number of cooling ducts '''

    ''' Polynomial function TOPOIL for DCORNI = 1. m to determine XLOC '''

    ''' Limit for number of cooling ducts versus XLOC
        1:st degree polymomials '''

    BBERR = False
    ICTOPO=5
    MAXCRV=8
    MAXLIM=5
    NLIM=[0. for i in range(MAXCRV)]
    TABK=[[0. for i in range(MAXLIM)] for j in range(MAXCRV)]
    TABL=[[0. for i in range(MAXLIM)] for j in range(MAXCRV)]
    PTOPO=[0. for i in range(ICTOPO)]
    NLIM[0]=5.
    NLIM[1]=5.
    NLIM[2]=5.
    NLIM[3]=5.
    NLIM[4]=4.
    NLIM[5]=4.
    NLIM[6]=4.
    NLIM[7]=4.

    TABK[0][0]=-0.096154
    TABK[1][0]=-0.104167
    TABK[2][0]=-0.096154
    TABK[3][0]=-0.108696
    TABK[4][0]=-0.100000
    TABK[5][0]=-0.104167
    TABK[6][0]=-0.100000
    TABK[7][0]=-0.104167

    TABK[0][1]=-0.080645
    TABK[1][1]=-0.086207
    TABK[2][1]=-0.081967
    TABK[3][1]=-0.084746
    TABK[4][1]=-0.079365
    TABK[5][1]=-0.092593
    TABK[6][1]=-0.078125
    TABK[7][1]=-0.092593

    TABK[0][2]=-0.064103
    TABK[1][2]=-0.071429
    TABK[2][2]=-0.063291
    TABK[3][2]=-0.070423
    TABK[4][2]=-0.063636
    TABK[5][2]=-0.073529
    TABK[6][2]=-0.064384
    TABK[7][2]=-0.074627

    TABK[0][3]=-0.050000
    TABK[1][3]=-0.055556
    TABK[2][3]=-0.050000
    TABK[3][3]=-0.056180
    TABK[4][3]=-0.050000
    TABK[5][3]=-0.058442
    TABK[6][3]=-0.050000
    TABK[7][3]=-0.058824

    TABK[0][4]=-0.041176
    TABK[1][4]=-0.045918
    TABK[2][4]=-0.042105
    TABK[3][4]=-0.045918
    TABK[4][4]= 0.000000
    TABK[5][4]= 0.000000
    TABK[6][4]= 0.000000
    TABK[7][4]= 0.000000

    TABL[0][0]=2.615385
    TABL[1][0]=2.562500
    TABL[2][0]=2.663462
    TABL[3][0]=2.630435
    TABL[4][0]=2.900000
    TABL[5][0]=2.770833
    TABL[6][0]=2.950000
    TABL[7][0]=2.812500

    TABL[0][1]=2.725805
    TABL[1][1]=2.637932
    TABL[2][1]=2.778689
    TABL[3][1]=2.669492
    TABL[4][1]=2.952381
    TABL[5][1]=2.962963
    TABL[6][1]=2.976563
    TABL[7][1]=3.018519

    TABL[0][2]=2.717949
    TABL[1][2]=2.671429
    TABL[2][2]=2.740506
    TABL[3][2]=2.704225
    TABL[4][2]=2.948182
    TABL[5][2]=2.941176
    TABL[6][2]=3.010822
    TABL[7][2]=3.007463

    TABL[0][3]=2.650000
    TABL[1][3]=2.611111
    TABL[2][3]=2.690000
    TABL[3][3]=2.657303
    TABL[4][3]=2.890000
    TABL[5][3]=2.894156
    TABL[6][3]=2.940000
    TABL[7][3]=2.952941

    TABL[0][4]=2.597059
    TABL[1][4]=2.555612
    TABL[2][4]=2.648421
    TABL[3][4]=2.592347
    TABL[4][4]=0.000000
    TABL[5][4]=0.000000
    TABL[6][4]=0.000000
    TABL[7][4]=0.000000

    PTOPO[0]=34.998871
    PTOPO[1]=-1.554101
    PTOPO[2]=0.397902E-01
    PTOPO[3]=-0.458320E-03
    PTOPO[4]=0.208328E-5

    ''' Check topoil '''

    if (TOPOIL  <  50.)  :
        TOLOC = 50.
    elif (TOPOIL  >=  50.  and  TOPOIL  <=  90.)  :
        TOLOC = TOPOIL
    else :
        BBERR = True
        ''' WRITE(JFC,*)'Error in NCDTA1: Top oil Temperature too high.',
            TOPOIL,' degrees C.' '''
        return 0

    ''' Determine curve of TOPOIL '''

    X1 = 0.1
    Y1 = 2.
    X2 = 1.
    Y2 = numpy.polyval(PTOPO[::-1], TOLOC)
    K = (Y1 - Y2)/(X1 - X2)
    L = Y1 - K*X1

    ''' Location '''

    XLOC = K*DCORNI + L

    ''' Find polynomial, from Fequency, Joints and Plate Grade '''

    if ((ISTGRD ==  1) or (ISTGRD == 11) or (ISTGRD ==  2))  :

        if (BLIMB  <=  1.95)  :

            if (not(BBSTLP))  :
                if (round(FREQ) == 50)  :
                    INDCRV = 1
                elif (round(FREQ) == 60)  :
                    INDCRV = 2
                else :
                    ''' WRITE(JFC,*) 'NCDTA1 has found an illegal frequency ',FREQ,' Hz.' '''
                    BBERR = True
                    return 0
                   
            elif (BBSTLP)  :
                if (round(FREQ) == 50)  :
                    INDCRV = 3
                elif (round(FREQ) == 60)  :
                    INDCRV = 4
                else :
                    ''' WRITE(JFC,*) 'NCDTA1 has found an illegal frequency ',FREQ,' Hz.' '''
                    BBERR = True
                    return 0

            else :
                ''' WRITE(JFC,*) 'NCDTA1 has found an illegal joint type ','Steplap = ',BBSTLP '''
                BBERR = True
                return 0

        else :
            ''' WRITE(JFC,*) 'NCDTA1 has found an illegal flux density ',BLIMB,' T.' '''
            BBERR = True
            return 0

    elif ((ISTGRD == 3) or (ISTGRD == 4))  :
        if (BLIMB  <=  1.98)  :
            if (not (BBSTLP))  :
                if (round(FREQ) == 50)  :
                    INDCRV = 5
                elif (round(FREQ) == 60)  :
                    INDCRV = 6
                else :
                    ''' WRITE(JFC,*) 'NCDTA1 has found an illegal frequency ',FREQ,' Hz.' '''
                    BBERR = True
                    return 0

            elif (BBSTLP)  :
                if (round(FREQ) == 50)  :
                    INDCRV = 7
                elif (round(FREQ) == 60)  :
                    INDCRV = 8
                else :
                    ''' WRITE(JFC,*) 'NCDTA1 has found an illegal frequency ',FREQ,' Hz.' '''
                    BBERR = True
                    return 0

            else :
                ''' WRITE(JFC,*) 'NCDTA1 has found an illegal joint type ','Steplap = ',BBSTLP '''
                BBERR = True
                return 0

        else :
            ''' WRITE(JFC,*) 'NCDTA1 has found an illegal flux density ',BLIMB,' T.' '''
            BBERR = True
            return 0
    
    ''' Compare flux density against curves for number of cooling ducts '''

    BBFND = False
    I = 1
    while (I  <=  NLIM[INDCRV-1] and  not BBFND):
        P[0] = TABL[INDCRV-1] [I-1]
        P[1] = TABK[INDCRV-1] [I-1]
        if (numpy.polyval(P[::-1], XLOC)  >  BLIMB)  :
            NC = I - 1
            BBFND = True

        I=I+1

    ''' If not found below any of the curves, then it is located
        above the last curve.
        The verifications of TOPOIL and BLIMB above will keep us
        inside the permitted area in the diagram. '''

    if(not BBFND):
        NC = NLIM[INDCRV-1]

    NCDTA1=NC

    return NCDTA1
