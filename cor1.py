
''' Title:  Calculation of cores without side-limbs '''
from ncool import NCOOL
from precor import PRECOR
from core import CORE
def COR1(BLIMB,BMAXPU,CORBND,DCORE,FEXTV,FNEXTV,FREQ,
        HLIMB,ILACK,JFC,KCOOL,KCORE,NPHAS,NWOULI,PLIMB,
        TTOILM,TTOILC,TWSUP,TYPCOR,YHADD,YHRED,
         CORESE,BBSTLA,ISTGRD,NCOOLI):

    COM=[0. for i in range(50)]
    RNP=[0. for i in range(100)]
    TS=[0. for i in range(100)]
    RK1=[0. for i in range(100)]
    B3=[0. for i in range(100)]
    B1=[0. for i in range(101)]
    TP=[0. for i in range(101)]
    FACTOR=1.E+3
    BBFALS=False

    if(KCORE ==2):
        COM[36]=round(YHRED*FACTOR)
    if(KCORE == 4):COM[36]=round(YHADD*FACTOR)

    TEMP=TTOILM+20.
    if(KCOOL ==3): TEMP=TTOILM+10.
    if(TTOILC > 0.1): TEMP=TTOILC+30.

    ''' No. of cooling ducts '''

    BHELP=BLIMB*BMAXPU
    NCOOLW=NCOOL(CORESE,TYPCOR,DCORE,TEMP,BHELP,FREQ,BBSTLA,JFC,ISTGRD  )
    if(NCOOLI < 0):
        NCOOLC = NCOOLW
    else:
        NCOOLC = NCOOLI

    ''' Glued core    given by: KBAND = 0
        Standard with ASECOND : KBAND = 1
        Steel banding given by: KBAND = 2 '''

    ''' Start of the Banding block '''

    KBAND=1
    if(HLIMB >4.): KBAND=2
    if(CORBND[0] == 'S'): KBAND=2
    if(KCORE == 1 or KCORE == 6): KBAND=0

    ''' End of the Banding block '''

    ''' Determine Core input '''

    ''' Start of the Core input block '''

    T1=0.
    TKAN=0.
    if(TYPCOR > 6.):TKAN=6.

    ''' Indata to CORE '''

    BT=0.
    T2=0.
    TT=0.
    DN=0.
    B1MAX=0.
    B1MIN=0.
    
    (DN,B1MAX,B1MIN,BT,TT,RDRAG,BDRAG,
     TDRAG)=PRECOR(round(DCORE*FACTOR),round(HLIMB*FACTOR),KCORE,
                   0.8,T1,T2,BBFALS,KBAND,2000.,10.,TYPCOR,TKAN)

    TASEC=T1/FACTOR
    BDRAG=BDRAG/FACTOR
    TDRAG=TDRAG/FACTOR

    ''' End of the Core input block '''

    ''' Call of CORE '''

    ''' Start of the CORE block '''

    COM[0]=round(float(NPHAS))
    COM[1]=round(DCORE*FACTOR)
    COM[2]=DN
    COM[4]=round(PLIMB*FACTOR)
    COM[5]=round(HLIMB*FACTOR)
    COM[6]=10.
    COM[7]=24.

    if(ISTGRD ==3):COM[7]=32.
    if(ISTGRD == 4): COM[7]=32.
    TJPL=0.3

    if(ISTGRD == 3):TJPL=0.23
    if(ISTGRD == 4):TJPL=0.23
    COM[8]=TJPL
    COM[9]=FNEXTV
    COM[10]=round(float(NCOOLC))
    COM[11]=2.
    COM[12]=B1MIN
    COM[13]=B1MAX
    COM[18]=TT
    COM[32]=round(TWSUP*FACTOR)
    COM[33]=40.
    COM[34]=60.
    COM[35]=round(float(KCORE))
    COM[37]=round(float(ILACK))
    COM[39]=FEXTV
    COM[40]=1.732

    ''' Calculate the core section '''
    
    COM,RNP,B1,B3,RK1,TP,TS=CORE(COM,RNP,B1,B3,RK1,TP,TS)

    ''' TYP=round(float(NPHAS))
    NPKT=round(COM[29]) '''

    ''' End of the CORE block '''

    ''' Calculate the proportion of varnished laminations
        This is always zero as we no longer use varnished core steel '''

    ''' LANDEL(TYP,round(DCORE*FACTOR),ILACK,NPKT,B1,TP,ANDEL) '''
    ANDEL=0.

    ''' Calculations of some core parameters '''

    ''' Start of the core parameter block '''

    UTURN0=COM[19]
    U0=UTURN0*FREQ/50.
    GLIMBM=COM[14]
    GYOKE=COM[15]
    GCORN=COM[16]
    GLIMBY=0.
    HYOKE=COM[27]/FACTOR
    TCORE=COM[28]/FACTOR
    ACORE=COM[21]/1.E+4
    RLYOKE=(float(NWOULI)-1.)*PLIMB+B1MAX/FACTOR
    YOKAMP=COM[22]

    ''' End of the core parameter block '''

    return (ACORE,ANDEL,BDRAG,GCORN,GLIMBM,GLIMBY,GYOKE,HYOKE,KBAND,NCOOLC,
         RDRAG,RLYOKE,TASEC,TCORE,TDRAG,U0,YOKAMP,NCOOLW)
