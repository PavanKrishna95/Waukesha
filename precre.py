#  Title:  Assign core variables
from fprint import FPRINT
def PRECRE(AARR,BBSLIM,TARR,BBVFR,BMAXPU,NPHAS,NWOULI,UARR,UMAXPU,BBERR):
    print("start of PRECRE")
    #initializations
        
    #Start of KCORE block.
    ISTGRD=1
    if(TARR[1-1]=='HI-B'):    ISTGRD=2
    if(TARR[1-1]=='ZDKH'):    ISTGRD=3
    if(TARR[1-1]=='PLJT'):    ISTGRD=4

    KCORE=2
    if(UARR[20]=='TAA'):
        KCORE=1
    elif(UARR[20]=='130'):
        KCORE=3
    elif(UARR[20]=='TCA'):
        KCORE=4
    elif(UARR[20]=='TAC'):
        KCORE=5
    elif(UARR[20]=='TAD'):
        KCORE=6
    elif(UARR[20]=='TA1'):
        KCORE=101  

    # No side-limb core available for TAA series                     

    if(KCORE==1 and BBSLIM):
        JFC,BBERR=FPRINT(1,BBERR,'Side-limb core does not exist for the TAA-series  ')

    if(KCORE==101 and BBSLIM):
        JFC,BBERR=FPRINT(1,BBERR,'Side-limb core does not exist for the TA1-series  ')
            
    #No side-limb core available for 130 series
    if(KCORE==3 and BBSLIM):
        JFC,BBERR=FPRINT(1,BBERR,"Side-limb core does not exist for the 130-kV ser  ")

    # End of KCORE block.
    #Flux density

    # Start of flux density BLOCK.
    #Maximum flux density

    BMAX=1.95
    if(TARR[0]=='HI-B'): BMAX=1.98
    if(TARR[0]=='ZDKH'): BMAX=1.98
    if(TARR[0]=='PLJT'): BMAX=1.98
    if(AARR[146]>0.1): BMAX=AARR[146]

    # Maximum flux density during optimisation = BLTOPM
    BLTOPM=BMAX/BMAXPU/UMAXPU
    
     #End of Flux density block.
     # Core dimension adjustment
     #Start of Core adjustment block.
    YHADD=AARR[149]/1.e+3
    #Area re-inforcement for TCA (Dimension :  length)
    if(YHADD>0 and KCORE!=4 and KCORE!=5):
        JFC,BBERR=FPRINT(1,'Yoke height addition only for TCA                 ')

    YHRED=AARR[159]/1.e+3

    #Yoke height reduction for TBA
    if(YHRED>0 and KCORE!=2):
        JFC,BBERR=FPRINT(1,BBERR,'Yoke height reduction only for TBA                ')

    FNEXTV=AARR[79]

    #Filling factor for the core-limb (no extra varnish)

    if(FNEXTV<0.9 or FNEXTV>1):
        JFC,BBERR=FPRINT(1,BBERR,'Fillfactor core, without ext.varn. outside limits ')

    FEXTV=AARR[89]    

    #Filling factor for the core-limb (with extra varnish)

    if(FEXTV<0.9 or FEXTV>1):
        JFC,BBERR=FPRINT(1,BBERR,'Fillfactor core, with ext.varn. outside limits    ')

    # End of Core adjustment block.    

    #Turn voltage given as additional indata

    U0IN=AARR[144]

    #Possibly an indata check can be included here

    # Minimum and maximum core diameter

    #TAA core

    if(KCORE==1):
        CHCORE='Without sidelimb acc.to LT-TA 4610-110E (TAA-Core)          '
        NCLA=2
        DCOMIN=265.E-3
        DCOMAX=600.E-3

    #TBA core
    elif(KCORE==2):
        CHCORE='Without sidelimb acc.to LT-TA 4611-107 (TBA-Core)          '
        NCLA=3
        DCOMIN=265.E-3
        DCOMAX=1040.E-3

    #130 kV core
    elif(KCORE==3):
        CHCORE='Without sidelimb , 130 kV core                              '
        NCLA=3
        DCOMIN=265.E-3
        DCOMAX=670.E-3

    #TCA core
    elif(KCORE==4 or KCORE==5):

    #TCA core without side-limb
        if(not BBSLIM):
            CHCORE='TCA - Core without sidelimbs                                '
            NCLA=3
            DCOMIN=500.E-3
            DCOMAX=1040.E-3

    # TCA core with side-limb
        else:
            CHCORE='TCA - Core with sidelimbs                                   '
            NCLA=3
            DCOMIN=680.E-3
            DCOMAX=1500.E-3
    #TAC core without side-limbs
    elif(KCORE==6):
        if(UARR[20]=='TAC'): CHCORE='TAC - Core without sidelimbs                                '
        if(UARR[20]=='TAD'): CHCORE='TAD - Core without sidelimbs                                '            
        NCLA=3
        DCOMIN=265.E-3
        DCOMAX=600.E-3
    # TA1 core
    elif(KCORE==101):
        CHCORE='Core without sidelimb acc.to 1ZBA-TS 4610-101 (TA1-Core)    '
        NCLA=3
        DCOMIN=400.E-3
        DCOMAX=1000.E-3    

    #LTB CORE
    else:
        CHCORE='Core with sidelimb acc.to LT-TA 4610-111E (LTB-Core)        '
        NCLA=3
        DCOMIN=555.E-3
        DCOMAX=1500.E-3

    if(AARR[169]>0):DCOMIN=AARR[169]/1.E+3
    if(AARR[170]>0): DCOMAX=AARR[170]/1.E+3   
    print("end of PRECRE")
    #return
    return (BLTOPM,CHCORE,DCOMAX,DCOMIN,FEXTV,FNEXTV,KCORE,NCLA,ISTGRD,U0IN,YHADD,YHRED,BBERR)

