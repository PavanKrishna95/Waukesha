#Title:  Calculation of masses using MNL-79 basis
from mass01 import MASS01
from mass02 import MASS02
from mass03 import MASS03
from mass04 import MASS04
from mass05 import MASS05
from mass06 import MASS06
from mass07 import MASS07
from tank79 import TANK79
from pbalk import PBALK
def MASS79():
    import com as C
    import common as CM
    #DECALRATIONS
    BB07=False
    ZCOIAR=[0. for i in range(9)]
    FACTOR=1.E+3
    RAA=[0 for i in range(9)]
    HSPOL=[0 for i in range(9)]
    RGUID=0


    #END OF DECLARATIONS

    #Cooling equipment on tank
    KCOOL1=1

    #Tap changer on short tank side
    BB03=False

    #Conservator located on main tank
    BB08=True

    BBPRNT=False

    if(C.BBEND and C.BBHELP[5]): BBPRNT=True

    #MASS01 Core

    #Start of the MASS01 Core block.
    CORLAN=C.GCORLA*(1-C.ANDEL)
    CORLAX=C.GCORLA*C.ANDEL
    GASEC=C.ASECL*0.048

    #Yoke clamps

    C.JFC=PBALK(BBPRNT,C.JFC,round(C.DCORE*FACTOR),C.HYOKE*FACTOR,
                C.HLIMB*FACTOR,C.PLIMB*FACTOR,round(C.TWSUP*FACTOR),
                C.BBEXAC,C.SNOML/1.E+6,C.RLYOKE*FACTOR,
                C.TCORE*FACTOR,C.KCORE,round(C.TYPCOR),C.BBSLIM)

    #Core
    MASS01(BBPRNT,C.JFC,round(C.TYPCOR),C.ISTGRD,C.NCLA,
           C.HLIMB*FACTOR,round(C.DCORE*FACTOR),C.HYOKE*FACTOR,
           C.RLYOKE*FACTOR,float(C.NCOOLC),CORLAN,CORLAX,GASEC)

    #End of the MASS01 Core block.

    #MASS02  WindinGSN
    #Adjustment height = RJH

    #Start of the MASS02 WindinGSN block.

    RJH=C.HLIMB*FACTOR-0.34*(FACTOR*C.DCORE)**0.83
    for IWDG in range(1,1+C.NWILI):
        C.ZCODU[IWDG-1]=C.RRWDG[IWDG-1]*40-1
        if(C.KWITYP[IWDG-1]>=3 and C.KWITYP[IWDG-1] <=5):
            C.ZCODU[IWDG-1]=C.RRWDG[IWDG-1]*20-1
        if(C.ZCODU[IWDG-1]<0): C.ZCODU[IWDG-1]=0
        if(C.BARR[IWDG-1]>=0): C.ZCODU[IWDG-1]=C.BARR[IWDG-1]
        TCLAC=0

        #Calculation of clacks and parallel parts
        RPRTAR=1
        RPRTRR=1

        #Control if the strands per cable is for OR or LR.
        #  If so it willimply 2 strands per cable
        if(C.IPISOL[IWDG-1]==2 or C.IPISOL[IWDG-1]==3): RPRTRR=2

        if(C.TSPIN[IWDG-1]>0.001 and C.KWITYP[IWDG-1]<6): RPRTRR=2
        C.RPART[IWDG-1]=RPRTRR
        PSPIN=0.5E-3
        if(C.IPISOL[IWDG-1]==2): PSPIN=0.15E-3
        if(C.IPISOL[IWDG-1]==3): PSPIN=0.85E-3
        if(C.DARR[30+IWDG-1]>0): PSPIN=C.DARR[30+IWDG-1]/1.E+3

        #FOR C.KWITYP <> 2 AND <> 7

        if(C.KWITYP[IWDG-1]!=2 and C.KWITYP[IWDG-1]!=7):
            CUTOT=C.ACOND[IWDG-1]*C.ZWIND[IWDG-1]
            HLP=C.BPART[IWDG-1]+(C.TSPIN[IWDG-1]-PSPIN)/RPRTRR+PSPIN
            CURR=(C.RRWDG[IWDG-1]-5.*C.ZCODU[IWDG-1]/1.E+3)/HLP*C.BPART[IWDG-1]
            TCLAC=C.HWIND[IWDG-1]-CUTOT/CURR/C.HPART[IWDG-1]*(C.HPART[IWDG-1]+C.TSPIN[IWDG-1])
            TCLAC=max(0.,TCLAC)

            # Outer cross-overs for SD windinGSN
        C.NOUCO[IWDG-1]=0    
        if(C.KWITYP[IWDG-1]==4):
            C.NOUCO[IWDG-1]=0.5+(C.HWIND[IWDG-1]-TCLAC)/(C.HPART[IWDG-1]+C.TSPIN[IWDG-1])/2
            C.NOUCO[IWDG-1]=C.NOUCO[IWDG-1]*C.NWOULI
            RGUID=C.DARR[IWDG-1]
        if(RGUID>1): C.ZCODU[IWDG-1]=0
        PCSNED=C.DARR[10+IWDG-1]
        MASS02(BBPRNT,C.JFC,IWDG,round(C.DCORE*FACTOR),C.HLIMB*FACTOR,
               C.HWIND[IWDG-1]*FACTOR,RJH,
               C.KWITYP[IWDG-1],C.PLIMB*FACTOR,C.ACOND[IWDG-1]*FACTOR*FACTOR,
               C.RAACON[IWDG-1]/FACTOR,C.NCONDU[IWDG-1],C.NWOULI,
               C.HPART[IWDG-1]*FACTOR,C.BPART[IWDG-1]*FACTOR,RPRTAR,RPRTRR,
               C.TCOV1[IWDG-1]*FACTOR,C.TCOV2[IWDG-1]*FACTOR,float(C.NLOOP[IWDG-1]),
               C.ZWIND[IWDG-1],C.DWIND[IWDG-1]*FACTOR,C.RRWDG[IWDG-1]*FACTOR,
               C.BDUCT[IWDG-1]*FACTOR,C.ISAM,TCLAC*FACTOR,RGUID,C.ZCODU[IWDG-1],
               PCSNED,HSPOL[IWDG-1],C.HCLAC[IWDG-1],C.ZLAG[IWDG-1],ZCOIAR[IWDG-1],
               C.NGROUP[IWDG-1],C.IPISOL[IWDG-1])

    #*SEBL End of the MASS02 WindinGSN block.

#C... MASS03  Cleats & leads

#CC*SBBL Start of the MASS03 Cleats & Leads block.    
    for J1 in range(1,1+C.NG):
        JTML=J1

        #Set KX031

        #3 Phase

        if(C.NPHAS==3):
            KX031=5
            if(C.KCON[JTML-1]==3): KX031=8
            if(C.KCON[JTML-1]==11): KX031=6
            if(C.KCON[JTML-1]==0): KX031=3

        #1 Phase

        else:
            KX031=C.NWOULI
        NCON=0
        RLCON=0

        #Set KTML
        
        #VFR

        if(C.BBVFR):
            KTML=1
            if(C.BBAUTO and not C.BBUPTR): KTML=2

        #CFR
        else:
            KTML=JTML

        #Calculate NCON

        #VFR or regulated terminal
        if(C.BBVFR or C.BBVR[JTML-1]):
            #Calculate NCON
            if(JTML==KTML):
                NCON=C.NPSTEP[KTML-1]+C.NMSTEP[KTML-1]
                if(C.KTYPRW[KTML-1]==2) :NCON=NCON/2
                if(C.KTYPRW[KTML-1]==3) :NCON=2+NCON/2
                NCON=NCON+1
                RLCON=600*C.RLYOKE+1000*C.HLIMB
                if(BB03): RLCON=1200*C.HLIMB


        UNX=C.UN[JTML-1][0]
        if(C.BBVR[JTML-1]): UNX=C.UN[JTML-1][2]
        BOOST=1

        #Cleats & leads
        MASS03(BBPRNT,C.JFC,JTML,KX031,C.UDIM[JTML-1],C.SRATEP[JTML-1]/UNX,
               C.HLIMB*FACTOR,C.NWOULI,NCON,RLCON,BOOST)

    #Correction for BOOSTER. Mass included in goods for cleat and lds.
    CM.GG32[1] = CM.GG32[1] + C.MABOOS

    #End of the MASS03 Cleats & Leads block.
 #   MASS04  Active part : Others

#CC*SBBL Start of the MASS04 Active part : others block.

    DBW=C.DPHAS
    if(C.BBSLIM and C.NWOULI ==1): DBW=C.DPHSL
    WWINDY=C.RRWDG[C.NWILI-1]
    BB048=False

    MASS04(BBPRNT,C.JFC,DBW*FACTOR,C.DOUTW*FACTOR,WWINDY*FACTOR,
           RJH,C.NWOULI,C.NCLA,CORLAN,CORLAX,round(C.TYPCOR),
           round(C.DCORE*FACTOR),C.DPHSL*FACTOR,C.HLIMB*FACTOR,
           round(C.TWSUP*FACTOR),BB048)

# End of the MASS04 Active part : others block.
#*
#C... MASS05  Tank, Cooling equipment, Cover
#*
#CC*SBBL Start of the MASS05  Tank, Cooling equipment, Cover block.
    PK=C.URC[0][0][0]
    if(C.BBVR[0]):  PK=max(PK,C.URC[1][0][0],C.URC[2][0][0])
    if(C.BBVR[1]):  PK=max(PK,C.URC[0][1][0],C.URC[0][2][0])

    #Calculation of tank dimensions

    OPTTNK=C.UARR[19]
    #Set tank dimensions
    # If they are to be optimised

    if(OPTTNK[0]=='Y'):
        C.RLTANK=C.RLTRAN+C.EXTANK
        C.BTANK=C.DOUTW+2*C.DWITA
        C.HTANK=C.HCORE+C.DCOCOV
    #Set tank dimensions to zero
    # NO TANK
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
    
    if(C.KTANK!=0):

        #Tank mass
        TANK79(BBPRNT,C.JFC,C.HTANK,C.BTANK,C.RLTANK,VVAH,RRAD,C.VTANK,
               C.ASHELL,C.ACOVER,C.KTAN79,C.TANKDI,C.GTANK,C.BBLT10,C.BBEXAC)
    #Cooler variables
    PLOSS1=PK*C.ZWOULI+C.P00[2-1]

    if(C.KCOOL==2 or C.KCOOL==4): PK=C.FONAN*C.FONAN*PK
    PLOSS=PK*C.ZWOULI+C.P00[2-1]
    if(PLOSS<0): PLOSS=0
    XT=0
    if(C.BB132): XT=2000
    C.AFIELD=0
    if(C.BBFLDS):  C.AFIELD=2*C.RLTANK*C.HTANK

    #Tank, Cooling equipment, Cover
    MASS05(BBPRNT,C.JFC,C.BB051,C.GTANK,C.VTANK*FACTOR,C.ACOVER,
           C.ASHELL,BB07,C.GCOVER,KCOOL1,PLOSS,C.AFIELD,
           C.GRAD,XT*(C.BTANK+C.RLTANK),C.KTAN79)

    #End of the MASS05  Tank, Cooling equipment, Cover block.
#*
#C... MASS07  Final assembly, Dis-assembly
#*
#CC*SBBL Start of the MASS07  Final assembly, Dis-assembly block.

    for IWDG in range(1,1+C.NWILI):
        RAA[IWDG-1]=C.RAACON[IWDG-1]/1.E+3

    #Final assembly, Dis-assembly
    
    C.VACTP=MASS07(BBPRNT,C.JFC,C.NCLA,C.NWILI,C.NG,C.VTANK*FACTOR,
           C.RLTANK*FACTOR,C.BTANK*FACTOR,C.HTANK*FACTOR,C.BB132,
           RAA,C.VACTP,C.GVVAH,C.GOFWF)
    #Correction for BOOSTER
    C.VACTP=C.VACTP/FACTOR+C.VOBOOS

    #Free oil
    CM.GSN142 = CM.GSN142 - C.VOBOOS * 960

    #MASS06  Conservator, Signal leads
    MASS06(BBPRNT,C.JFC,BB08,KCOOL1,PLOSS1,C.KCOOL2,C.GFAN)

    C.GOIL=CM.GSN142

    return
            
