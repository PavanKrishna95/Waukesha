
''' Title:  Calculates the Net Core Diameter '''
from asec import ASEC
def DNET(KSERIE,KOD,HLIMB,ACCTR,DCOR,T1C,T2C):

    TISOL=2.
    TBAND=1.

    ''' Tolerance for ovality and crookedness '''

    TOL= int(0.001667*DCOR+5)

    ''' KOD=0 for GLUED core
        KOD=1 for ASECOND-BANDED core
        KOD=2 for STEEL-BANDED core '''

    if(KOD == 0):
        TTK=1.5
        if (DCOR > 400.):TTK=2.
        if (DCOR > 600.):TTK=3.5
        TOL=0.01*DCOR
        if (TOL < 3.):TOL=3.
        DCORN=int(DCOR-TTK-TOL)

    elif (KOD == 1) :

        (N1C,N2C,T1C,T2C,RLCC,RLKRMC,RMC,
            N1O,N2O,T1O,T2O,RLCO,RLKRMO,RMO)=ASEC(DCOR,HLIMB,ACCTR)

        if (KSERIE == 4) :
            TTK = 2.
            if (DCOR > 600.): TTK = 3.
            if (DCOR > 1000.): TTK = 4.
            TAS = 1.5
            TBU = 2.
            TPA = 1.5
            TKR = 2.
            DCORN  = DCOR-2.*(T2C+0.7)-2.*abs(TKR)-numpy.sqrt(TTK**2+TAS**2+TBU**2+TPA**2)
        else:
            T=T2C+0.3+0.4
            DCORN=DCOR-round(2.*T+TOL)
        
    elif (KOD == 2) :

        if (DCOR > 1000.) :
            NBAND=2
        else:
            NBAND=1

        DCORN=DCOR-round(2.*(TISOL+TBAND*NBAND)+TOL)
    
    return DCORN
