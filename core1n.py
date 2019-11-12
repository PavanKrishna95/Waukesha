
''' Title:  Calculation of core data '''
from preta1 import PRETA1
from corta1 import CORTA1
from cor130 import COR130
from cor1 import COR1
from cor2 import COR2
from asec import ASEC
from pysamp import pysamp
def CORE1N(BBEXAC,BBSLIM,BLIMB,BMAXPU,CORBND,DCORE,
           DOUTW,DPHAS,DPHSL,FEXTV,FNEXTV,FREQ,GACTP,
           HLIMB,ILACK,JFC,KCOOL,KCORE,NPHAS,NWOULI,
           QFINAL,TTOILM,TTOILC,TWSUP,TYPCOR,U0IN,UDIM1,
           UMAXPU,YHADD,YHRED,PLIMB,PLSL,DCFCTR,BBEXON,CORESE,
           BBSTLA, STKFAC,ISTGRD,NCOOLI,SPFADJ):

    import com as C
    import common as CM

    SBF=0
    DN0=FHD=MWB=ACCL=ACCV=OVRLPI=DIWBI=DEWBI=MAP=TCORST=0.
    NK=KB=IFLMT=NPACK=0
    NSHT=[0 for i in range(100)]
    A=MLMB=MYK=MCRNR=TASC=ETA=BSTEPI=BPLMAI=MAXWDT=MINWDT=HYK=HCR=TKO=RNFLP=0.
    SHWDT=[0. for i in range(100)]
    THKPCK=[0. for i in range(100)]
    
    ''' Set BBEXON=True if core diameter has changed sufficiently '''

    if (not(BBEXAC or BBEXON)):
        BBEXON=False
        if (((abs(1.-CM.DCORE0/DCORE) > DCFCTR) or
             (abs(1.-CM.HLIMB0/HLIMB) > DCFCTR))):BBEXON=True

    if (BBEXAC or BBEXON) :

        ''' Round off core diameter to integral mm '''

        if (BBEXAC): DCORE=round(1.E+3*DCORE)/1.E+3

        CM.DCORE0=DCORE
        CM.HLIMB0=HLIMB
        ZLIMB =float(NWOULI)

        ''' Calculate the core '''

        ''' NO side-limbs '''

        if ( not BBSLIM  and  KCORE == 7682) :

            ''' TA1 core '''
            (TCORST,DN0, NK, FHD, ifLPMT,MWB, ACCL, ACCV,KB,ETA,BSTEPI,BPLMAI,
             OVRLPI,NCOOLW)=PRETA1(DCORE, HLIMB, CORBND, TTOILC, BLIMB,FREQ,TASC,
                                   NCOOLI)
            C.DN = DN0
            RNK = float(NK)

            '''(A, MLMB, MYK, MCRNR,NPACK, NSHT, SHWDT, THKPCK,MAXWDT,
                MINWDT,HYK,
             HCR, TKO, RNFLP, BBLARM, ALARM)=CORTA1(C.DN, TCORST, RNK, PLIMB, HLIMB,
                                                    FHD, ifLPMT,MWB, QFINAL, ACCL, ACCV,ETA,BSTEPI,BPLMAI,
                                                    False,OVRLPI,BBSTLA , DEWBI, DIWBI, MAP) '''
            CM.ACORE0 = A
            ANDEL = 0.
            BDRAG = 0.
            CM.DKSL0 =0.
            CM.GCORN0 = MCRNR
            CM.GLIMM0 = MLMB
            CM.GLIMY0 = 0.
            CM.GYOKE0 = MYK
            HCORE = HCR
            CM.HYOKE0 = HYK
            KBAND = KB
            NCOOLC = NK
            RDRAG = 0.
            CM.RLYOK0 = 2.*PLIMB + C.DN
            TASEC = TASC
            TCORE = TKO
            TDRAG = 0.
            CM.U00 = (2.*3.14159*FREQ*CM.ACORE0*1.)/numpy.sqrt(2.)
            print('CM.ACORE0,FREQ',CM.ACORE0,FREQ)
            YOKAMP = 1.

        elif( not BBSLIM  and  KCORE == 3) :

            ''' 130 -kv CORE '''
             
            (CM.ACORE0,ANDEL,BDRAG,CM.GCORN0,CM.GLIMM0,CM.GLIMY0,CM.GYOKE0,CM.HYOKE0,NCOOLC,RDRAG,
             CM.RLYOK0,TASEC,TCORE,TDRAG,CM.U00,YOKAMP,CORBND,KBAND,NCOOLW)=COR130(ZLIMB,
                    DCORE, NPHAS, FREQ, BLIMB, UMAXPU,HLIMB, PLIMB,STKFAC,NCOOLI,SPFADJ)

        elif( not BBSLIM  and  KCORE != 3  and KCORE != 101) :
   
            (CM.ACORE0,ANDEL,BDRAG,CM.GCORN0,CM.GLIMM0,
                 CM.GLIMY0,CM.GYOKE0,CM.HYOKE0,KBAND,NCOOLC,RDRAG,CM.RLYOK0,TASEC,TCORE,
                 TDRAG,CM.U00,YOKAMP,NCOOLW )=COR1(BLIMB,BMAXPU,CORBND,DCORE,FEXTV,FNEXTV,FREQ,HLIMB,ILACK,
                 JFC,KCOOL,KCORE,NPHAS,NWOULI,PLIMB,TTOILM,TTOILC,TWSUP,
                 TYPCOR,YHADD,YHRED,CORESE,BBSTLA,ISTGRD,NCOOLI)
        
            CM.DKSL0=0.

            ''' Side-limbs '''

        else :
            
            ''' Calculate the core '''
            print('cor2456')
            (PLSL,QFINAL,CM.ACORE0,ANDEL,BDRAG,CM.DKSL0,
                 CM.GCORN0,CM.GLIMM0,CM.GLIMY0,CM.GYOKE0,CM.HYOKE0,KBAND,NCOOLC,RDRAG,CM.RLYOK0,
                 SBF,TASEC,TCORE,TDRAG,CM.U00,YOKAMP,NCOOLW)=COR2(BLIMB,BMAXPU,CORBND,DCORE,DOUTW,DPHSL,FEXTV,FNEXTV,FREQ,
                 GACTP,HLIMB,ILACK,JFC,KCOOL,KCORE,NPHAS,PLIMB,PLSL,QFINAL,
                 TTOILM,TTOILC,TWSUP,TYPCOR,YHADD,CORESE,BBSTLA,
                 ISTGRD,NCOOLI)

        ''' Turn voltage & core area '''

        ''' if turn voltage at 1T given '''
        
        if (U0IN > 0.1) :
            CM.U00=U0IN*FREQ/50.
            CM.ACORE0=U0IN/222.15

        ASECL=0.
        CM.ASECL0=0.

        ''' Core banding '''

        ''' ASECOND '''

        if (KBAND == 1  and  KCORE != 101) :

            ACC=0.8

            ''' ASECOND '''

            (N1C,N2C,T1C,T2C,ALCC,AKRPC,MC,N10,
             N20,T10,T20,ALC0,AKRP0,M0)=ASEC(1.E+3*DCORE,1.E+3*HLIMB,ACC)

            CM.ASECL0=float(NWOULI)*ALCC
            if (BBSLIM): CM.ASECL0=CM.ASECL0+2.*ALC0

    ''' Proportionation of core data '''

    X=(DCORE-0.024)/(CM.DCORE0-0.024)
    XX=X*X
    XXX=X*X*X
    U0=CM.U00*XX
    ACORE=CM.ACORE0*XX
    DKSL=CM.DKSL0*X
    HYOKE=CM.HYOKE0*X
    TURNRA=UDIM1/U0/BLIMB
    
    RLYOKE=CM.RLYOK0
    HCORE=HLIMB+2.*HYOKE
    if (KBAND == 1): ASECL=CM.ASECL0*X*HLIMB/CM.HLIMB0

    ''' Length of the transformer '''

    ''' NO side-limbs '''

    if ( not BBSLIM) :
        PLSL=0.
        RLTRAN=float(NWOULI)*PLIMB-DPHAS
        if (NWOULI == 1): RLTRAN=DOUTW+DPHSL+DCORE

        ''' Side-limbs '''

    else :
          PLSL=(DOUTW+DKSL)/2.+DPHSL+TASEC
          RLTRAN=float(NWOULI-1)*PLIMB+2.*PLSL+DKSL

    if (BBEXAC or BBEXON): CM.RLTRA0=RLTRAN
    GCORN=CM.GCORN0*XXX
    GLIMBM=CM.GLIMM0*HLIMB/CM.HLIMB0*XX
    GLIMBY=CM.GLIMY0*HLIMB/CM.HLIMB0*XX
    GYOKE=CM.GYOKE0*RLTRAN/CM.RLTRA0*XX
    GCORLA=GLIMBM+GLIMBY+GYOKE+GCORN

    print(DOUTW,DPHSL,GACTP,
           JFC,QFINAL,TWSUP,U0IN,
           YHADD,YHRED,PLSL, STKFAC,NCOOLI)
    

    return (CORBND,DCORE,QFINAL,ACORE,ANDEL,ASECL,BDRAG,DKSL,
           GCORLA,GCORN,GLIMBM,GLIMBY,GYOKE,HCORE,HYOKE,KBAND,
           NCOOLC, PLSL,RDRAG,RLTRAN,RLYOKE,SBF,TASEC,
           TCORE,TDRAG,TURNRA,U0,YOKAMP,BBEXON,NCOOLW)
