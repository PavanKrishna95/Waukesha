#Title:  Calculation of masses, simplified routines
from covma import COVMA
from tank79 import TANK79
from pbalk import PBALK
def MASS92():
    import com as C
    #DELCLARATIONS
    OPTTNK=''
    FACTOR=1.E+3
    BBPRNT=False

    #END OF DECLARATIONS

    #Mass and volume of winding conductors
    C.GCONDU = 0
    VOLCU  = 0

    for IWDG in range(1,1+C.NWILI):
        VOLCU  = VOLCU  + C.GWINCO[IWDG-1]/C.RAACON[IWDG-1]*C.ZWOULI
        C.GCONDU = C.GCONDU + C.GWINCO[IWDG-1]*C.ZWOULI

    #Yoke clamps
    C.JFC,C.GPBLK=PBALK(BBPRNT,C.JFC,round(C.DCORE*FACTOR),C.HYOKE*FACTOR,
                        C.HLIMB*FACTOR,C.PLIMB*FACTOR,round(C.TWSUP*FACTOR),
                        C.BBEXAC,C.SNOML/1.E+6,C.RLYOKE*FACTOR,
                        C.TCORE*FACTOR,C.KCORE,round(C.TYPCOR),C.BBSLIM)

    # Calculation of tank dimensions

    OPTTNK=C.UARR[19]

    #Set tank dimensions

    #If they are to be optimised

    if(OPTTNK[0]=='Y'):
        C.RLTANK=C.RLTRAN+C.EXTANK
        C.BTANK=C.DOUTW+2*C.DWITA
        C.HTANK=C.HCORE+C.DCOCOV

    #Set tank dimensions to zero

    #NO TANK
    if(C.KTANK==0):
        C.RLTANK=0
        C.BTANK=0
        C.HTANK=0
    C.ACOVER=(C.F1TANK*C.RLTANK+C.F2TANK*C.BTANK)*C.BTANK
    C.ASHELL=(C.RLTANK+C.F3TANK*C.BTANK)*C.HTANK*2
    if(C.KTANK==0): C.ACOVER=0
    if(C.KTANK==0): C.ASHELL=0
    C.VTANK=C.ACOVER*C.HTANK
    VVAH=C.GVVAH/1250
    RRAD=C.GRAD/500
    if(C.KTANK != 0):
        
        #Tank mass
        TANK79(BBPRNT,C.JFC,C.HTANK,C.BTANK,C.RLTANK,VVAH,RRAD,C.VTANK,
               C.ASHELL,C.ACOVER,C.KTAN79,C.TANKDI,C.GTANK,C.BBLT10,C.BBEXAC)

    #Cover

    C.GCOVER=COVMA(C.ACOVER,C.KTAN79)

    # Volume active part

    C.VACTP = VOLCU + (C.GCORLA+C.GPBLK)*0.13E-3

    #Free oil:
#      Formula from MNL79 mass calculations
    C.GOIL  = 960.*(0.98*C.VTANK - C.VACTP)

    #MASS  Conservator(1st part), pipes to conserv. (2nd part)
  #      Formulas from MNL79 mass calculations
    C.GCONS = 0.129*C.GOIL**0.9  + 1.21E-5*C.GOIL**1.5

    C.GACTP = C.GCONDU+C.GCORLA+C.GPBLK
    C.GTRP  = C.GACTP+C.GTANK+C.GCOVER+C.GCONS

    return
