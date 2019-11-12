
''' Title:  Checks certain indata which have different
            limitations for the different USERID's. '''

from icheck import ICHECK
def CHECK():
    import numpy
    import com as C
    ''' Check initialisations '''

    Y=[0. for i in range(20)]

    ''' Terminal initialisations '''

    CURTML=[0. for i in range(4)]

    ''' Power ratiC.NGs '''

    ''' Start of the power ratiC.NGs block. '''

    FONAN=C.AARR[153]
    if(FONAN > 3.): FONAN=FONAN/100.
    SRAT=max(C.AARR[10],C.AARR[11],C.AARR[12],C.AARR[13])
    if (FONAN <= 1):
        Y[0]=SRAT*FONAN
        Y[1]=SRAT
        Y[7]=(-1.)*SRAT
    else:
        Y[0]=SRAT
        Y[1]=SRAT*FONAN
        Y[7]=(-1.)*Y[1]
    
    ''' Set power ratiC.NGs '''

    ''' If not 3-phase '''

    if(C.IARR[0] != 3):
        if(FONAN  <=  1):
            Y[8]=SRAT
            Y[9]=SRAT*FONAN
        else:
            Y[8]=SRAT*FONAN
            Y[9]=SRAT
        
    ''' End of the power ratiC.NGs block. '''

    ''' Maximum windiC.NG currents '''

    for JTML in range(1,C.NG+1):

        ''' C.KCON  I=0, Y=1, D=3,  IAUTO=10, YAUTO=11 '''
        LCON=numpy.mod(C.KCON[JTML-1],10)
        XCON=float(LCON)
        CURTML[JTML-1]=C.AARR[10+JTML-1]/C.AARR[15+JTML-1]*1000./float(C.IARR[50])
        if(LCON != 0):CURTML[JTML-1] = CURTML[JTML-1] * (C.SQR3/numpy.sqrt(XCON))
        if(FONAN > 1):CURTML[JTML-1] = CURTML[JTML-1] * FONAN

    ''' Auto-connected transformers '''

    ''' Start of the auto-transformer block. '''

    if (C.KCON[0] > 9 and C.AARR[15+JTML-1] < C.AARR[16+JTML-1]):
        CURTML[0]=CURTML[0]-CURTML[1]
    if (C.KCON[1] > 9 and C.AARR[15+JTML-1] > C.AARR[16+JTML-1]):
        CURTML[1]=CURTML[1]-CURTML[0]
    Y[2]=max(CURTML[0],CURTML[1],CURTML[2],CURTML[3])

    ''' End of the auto-transformer block. '''

    ''' Line voltage '''

    ''' Start of the line voltage block. '''

    Y[3]=max(C.AARR[15],C.AARR[16],C.AARR[17],C.AARR[18])

    ''' End of the line voltage block. '''

    ''' BIL - value '''

    ''' Start of the BIL block. '''

    Y[4]=max(C.AARR[25],C.AARR[26],C.AARR[27],C.AARR[28])

    ''' End of the BIL block. '''

    ''' Oil-guided cooliC.NG '''

    ''' Start of the BIL block. '''

    ''' Set oil-guided cooliC.NG '''

    for IWDG in range(1,C.NWILI+1):
        if(C.DARR[IWDG-1] > 0.1): Y[5]=4.

    ''' End of the BIL block. '''

    ''' WindiC.NG supports '''

    ''' Start of the windiC.NG support block. '''

    if(C.BARR[29] > 1.E-6): Y[10]=4.

    ''' End of the windiC.NG support block. '''

    ''' Side-limbed cores '''

    ''' Start of the side-limbed cores block. '''

    if(C.TARR[50][0] == 'Y'): Y[11]=4.

    ''' End of the side-limbed cores block. '''

    ''' HI-B core-steel '''

    ''' Start of the HI-B core steel block. '''

    if(C.TARR[0][0] == 'Y'): Y[12]=4.

    ''' End of the HI-B core steel block. '''

    ''' ASECOND core-bandiC.NG '''

    ''' Start of the ASECOND block. '''

    if(C.TARR[79] == 'ASEC'): Y[13]=4.

    ''' End of the ASECOND block. '''

    ''' Check the limitations for the particular UDB '''

    ''' Start of the Check block. '''

    if(C.BBHELP[5]):
        ''' PRINT *,'USER-LIMITS',Y '''

    ''' Check the limitations '''

    BBSTOP=ICHECK( Y,C.JFC)

    ''' End of the Check block. '''

    ''' Check whether to stop or not '''

    if(BBSTOP):
        exit()
        C.ISTOP = 1

    return
