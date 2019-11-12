from funkfr import FUNKFR
from nloadn import NLOADN
from core1n import CORE1N
from opcalc import OPCALC
from mass79 import MASS79
from mass92 import MASS92
from cost92 import COST92

from cooldp import COOLDP
from scdime import SCDIME
from penlty import PENLTY
from frfunk import FRFUNK
from byta79 import BYTA79
from cost79 import COST79

from pysamp import pysamp
def FUNK(XA):
    
    import com as C
    import common as CM
    print("START OF FUNK")

    CORESE=C.UARR[20]
    CORTYP=C.UARR[21]
    ISTEG=0
    INTRVL=200
    ISTEG2=0

    KBAND=0
    BBSTLA=None

    #END OF DECLARATIONS

    #Count the number of times FUNK has been called
    ISTEG=ISTEG+1
    if(ISTEG==ISTEG/INTRVL*INTRVL): print(ISTEG)

    #Assignation of free variables       

    C.BLIMB,C.DCORE,C.HLIMB,C.ACOND=FUNKFR(XA,C.ACOND,C.BBCURD,C.BBDLI,C.BBFLU,C.BBHLI,C.NWILI,C.BLIMB,C.DCORE,C.HLIMB)
   
    #Core calculations
    #Start of the core calculations block.
    C.BBEXON=False
    
    C.PLIMB=C.DOUTW+C.DPHAS
    
    # DCFCTR used to decide when to re-calculate the core exactly
   #( 5.*C.DRV = 5% of either limb height or core diameter
    #   assuming C.DRV = 0.01 )
    DCFCTR=10*C.DRV

    #Core calculations
    BBSTLA = (C.UARR[22]=='YES')
    print("FUNK calling CORE1N")
    C.CORBND,C.DCORE,C.QFINAL,C.ACORE,C.ANDEL,C.ASECL,\
    C.BDRAG,C.DKSL,C.GCORLA,C.GCORN,C.GLIMBM,C.GLIMBY,C.GYOKE,C.HCORE,C.HYOKE,KBAND,\
    C.NCOOLC,C.PLSL,C.RDRAG,C.RLTRAN,C.RLYOKE,C.SBF,\
    C.TASEC,C.TCORE,C.TDRAG,C.TURNRA,C.U0,C.YOKAMP,C.BBEXON,C.NCOOLW, =CORE1N(C.BBEXAC,C.BBSLIM\
    ,C.BLIMB,C.BMAXPU,C.CORBND,C.DCORE,C.DOUTW,C.DPHAS,C.DPHSL,C.FEXTV,C.FNEXTV,C.FREQ,C.GACTP,\
           C.HLIMB,C.ILACK,C.JFC,C.KCOOL,C.KCORE,C.NPHAS,C.NWOULI,\
           C.QFINAL,C.TTOILM,C.TTOILC,C.TWSUP,C.TYPCOR,C.U0IN,C.UDIM[1-1],\
           C.UMAXPU,C.YHADD,C.YHRED,C.PLIMB,C.PLSL,DCFCTR,C.BBEXON,CORESE,\
           BBSTLA, C.STKFAC,C.ISTGRD,C.NCOOLI,C.SPFADJ)

    #End of the core calculations block.

    # Currents, losses and reactances
    print("FUNK calling OPCALC")
    OPCALC(C.BBOUT)

    #Backtracking
    if C.ISTOP==1:
        return

    #Core. The limb-pitch is now calculated accurately

    # Start of the core calculations block.

    C.PLIMB=C.DOUTW+C.DPHAS

    #Core calculations
    if(C.BBEXON):   print("calculations . Diameter = {0} mm,  Limb height = {1} mm   ,  Adjusting the core".format(1.E+3*C.DCORE,1.E+3*C.HLIMB))
        
    print("FUNK calling CORE1N")
    C.CORBND,C.DCORE,C.QFINAL,C.ACORE,C.ANDEL,C.ASECL,\
    C.BDRAG,C.DKSL,C.GCORLA,C.GCORN, C.GLIMBM,C.GLIMBY,C.GYOKE,C.HCORE,C.HYOKE,KBAND,\
    C.NCOOLC,C.PLSL,C.RDRAG,C.RLTRAN,C.RLYOKE,C.SBF,\
    C.TASEC,C.TCORE,C.TDRAG,C.TURNRA,C.U0,C.YOKAMP,C.BBEXON,C.NCOOLW, =CORE1N(C.BBEXAC,C.BBSLIM\
    ,C.BLIMB,C.BMAXPU,C.CORBND,C.DCORE,C.DOUTW,C.DPHAS,C.DPHSL,C.FEXTV,C.FNEXTV,C.FREQ,C.GACTP,\
           C.HLIMB,C.ILACK,C.JFC,C.KCOOL,C.KCORE,C.NPHAS,C.NWOULI,\
           C.QFINAL,C.TTOILM,C.TTOILC,C.TWSUP,C.TYPCOR,C.U0IN,C.UDIM[1-1],\
           C.UMAXPU,C.YHADD,C.YHRED,C.PLIMB,C.PLSL,DCFCTR,C.BBEXON,CORESE,\
           BBSTLA, C.STKFAC,C.ISTGRD,C.NCOOLI,C.SPFADJ)

    #End of the core calculations block. 

    # No-load losses

    #BBRESC=.FALSE. because no resonance calc. needed here (See PRNLD)

    #SBBL Start of the core resonance calculation block.

    BBRESC=False
    BBRES=False

    # No-load losses and resonance
    print("FUNK calling NLOADN")
    BBRES=NLOADN(BBRESC)

    # End of the core resonance calculation block.
    print("FUNK calling COOLDP")
    # Cooling calculation
    COOLDP()
    print("FUNK calling SCDIME")
    #Short-circuit forces
    SCDIME(C.BBOUT)

    #Force exact MASS & C.COST calculations when C.BBEXON=.TRUE.

    if(C.BBEXON):
        BBDUMM=C.BBEXAC
        C.BBEXAC=True

    # Masses & costs    

    #Initialisation of result fields for masses & costs in MNL79.

    if(C.MNLY < 91):
        for IROW in range(1,1+241):
            for JCOL in range(1,1+6):
                CM.RES79[IROW-1][JCOL-1]=0

    #Initialisation of summation vector in subroutine C.COST (ZKLIB)
        print("FUNK calling COSTZO")
        #COSTZO()

    #masses and costs
        print("FUNK calling MASS79")
        MASS79()
        print("FUNK calling COST79")
        
        COST79()

    #MNL79 summation of costs
        print("FUNK calling BYTA79")
        BYTA79()

    else:
    #"MNL92 - FORMULAS"
        print("FUNK calling MASS92")
        MASS92()
        print("FUNK calling COST92")
        COST92()

    #Return C.BBEXAC to its original value if C.BBEXON=.TRUE.
    if(C.BBEXON):
        C.BBEXAC=BBDUMM

    X=C.PKLOSS*C.URC[1-1][1-1][1-1]*C.ZWOULI  
    Y=C.P0LOSS*C.P00[1-1]  
    C.CLOSSV=(X+Y)

    #VALUE = the value which the optimisation routine LMIN
    #is to minimise
    C.VALUEO=C.CLOSSV+C.COST

    #Calculation of limits.
    print("FUNK calling PENLTY")
    G=PENLTY()
    HELP=0
    if(C.BBOOVN and C.VALUEO > C.VALUEM): HELP=C.VALUEO-C.VALUEM
    if(C.BBOOVN): C.VALUEO=C.COST+HELP*2.
    VALUE=C.VALUEO/C.AVALUE

    #XA-values must be assigned if FUNK shall be OK
    #outside the optimisation routine
    print("FUNK calling FRFUNK")
    XA=FRFUNK(XA,C.ACOND,C.BBCURD,C.BBDLI,C.BBFLU,C.BBHLI,C.BLIMB,C.DCORE,C.HLIMB,C.NWILI)

    print("END OF FUNK")

    return 1,XA,G,VALUE



