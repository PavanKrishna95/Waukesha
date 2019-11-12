
''' Title:  Winding layout for Layer windings '''
''' 
BBARRR = .TRUE.  => BOTH C.ZAR AND C.ZRR GIVEN TROUGH INPUT DATA
C.ZPART = TOTAL NUMBER OF PARTS
C.ZAR = NUMBER OF AXIAL STRANDS
C.ZRR = NUMBER OF RADIAL STRANDS
C.HWIND = WINDING HEIGHT
HSPOL  = COIL HEIGHT
ULAG   = VOLTAGE PER LAYER
C.ZLAG   = NUMBER OF LAYERS
C.ZNLAG  = NUMBER OF TURNS PER LAYER
HPARTO &  BPARTO INCOMING PART DIMENSIONS
R      = WINDING INNER DIAMETER IN DIRECTION OF TANK-LENGTH
RINNET = WINDING INNER DIAMETER     IN DIRECTION OF TANK-BREADTH
RR     = RADIAL DIMENSION OF WINDING IN DIRECTION OF TANK-LENGTH
RRTADD = RADIAL ADDITION OF WINDING IN DIRECTION OF TANK-BREADTH
TRR    = RADIAL THICKNESS PER CABLE
C.SWIND  = WINDING MEAN CIRCUMFERENCE
C.DSWI = ACCUMULATED INCREASE OF CIRCUMFERENCE. CROSSOVERS
       AFFECT BOTH PRESENT C.DSWI AND C.DSWI FOR OUTER WINDINGS.
       INCREASE OF C.DSWI FOR TAPPINGS AFFECT ONLY OUTER WINDINGS.
       THEREFORE C.SWIND IS CALCULATED AFTER CROSSOVERS BUT BEFORE TAPPINGS
RNX = NUMBER OF TURNS WITH CROSSOVERS
      NUMBER OF CROSSOVERS = C.ZLAG - 1 '''

from goto import with_goto
from corn import CORN
@with_goto
def LWIND (IWDG):

    import com as C

    IHV=0
    HPARTO=[0. for i in range(9)]
    BPARTO=[0. for i in range(9)]
    HSPOL=[0. for i in range(9)]
    X3LAY=[0. for i in range(9)]
    X4LAY=[0. for i in range(9)]
    RRTADD=[0. for i in range(9)]
    RINNET=[0. for i in range(9)]
    RINNER=[0. for i in range(9)]
    TEST=[0. for i in range(9)]
    BBARRR=[False for i in range(9)]
    XLAY=[0. for i in range(9)]

    HPARTO[IWDG-1]=C.HPART[IWDG-1]
    BPARTO[IWDG-1]=C.BPART[IWDG-1]
    ZLOOP=float(C.NLOOP[IWDG-1])
    C.HWIND[IWDG-1]=C.HLIMB-C.DYOKE[IWDG-1]
    HSPOL[IWDG-1]=(C.HWIND[IWDG-1]-(C.ZCOIAR[IWDG-1]-1.)*
                   C.EXTRAR[IWDG-1])/C.ZCOIAR[IWDG-1]
    RGROUP=float(C.NGROUP[IWDG-1])
    COIPG=C.ZCOIAR[IWDG-1]/RGROUP
    ZNSPOL=C.ZWIND[IWDG-1]/COIPG

    X1=1.
    X2=0.5

    if(C.KWIND[IWDG-1] == 13 or C.KWIND[IWDG-1] == 14) :
        X1=3./2.
    elif (C.KWIND[IWDG-1] == 15 or C.KWIND[IWDG-1] == 16) :
        X1=5./3.
    elif (C.KWIND[IWDG-1] == 17 or C.KWIND[IWDG-1] == 18) :
        X1=7./4.
    elif (C.KWIND[IWDG-1] >=20) :
        X2=1.
    
    HELP1=(C.HCLAC[IWDG-1]*X1+C.TSPIN[IWDG-1])*1.E+3
    ULAG=3.E+3*HELP1**0.70*X2
    HELP2=ULAG
    HELP=2.5E+3*HELP1*X2
    if (HELP > ULAG): ULAG=HELP

    if (C.BBRR[IWDG-1]): goto ._302
    C.ZLAG[IWDG-1]=round(ZNSPOL*C.U0*C.BLIMB/ULAG)+1.
    label ._200
    if (BBARRR[IWDG-1]) :
        C.ZNLAG[IWDG-1]=(ZNSPOL+(ZLOOP*0.005/COIPG+XLAY[IWDG-1])/(C.HPART[IWDG-1]+C.TSPIN[IWDG-1])/1.01/C.ZAR[IWDG-1])/C.ZLAG[IWDG-1]-1.
        goto ._299

    label ._298
    C.ZNLAG[IWDG-1]=ZNSPOL/(C.ZLAG[IWDG-1]-(ZLOOP*0.005/COIPG+XLAY[IWDG-1])/HSPOL[IWDG-1])-1.
    C.ZAR[IWDG-1]=HSPOL[IWDG-1]/(C.ZNLAG[IWDG-1]+1.)/(HPARTO[IWDG-1]+C.TSPIN[IWDG-1])/RGROUP/1.01
    C.ZAR[IWDG-1]=round(C.ZAR[IWDG-1]+0.49)
    if (C.ZAR[IWDG-1] < 1.): C.ZAR[IWDG-1]=1.

    label ._299
    C.HPART[IWDG-1]=HSPOL[IWDG-1]/C.ZAR[IWDG-1]/(C.ZNLAG[IWDG-1]+1.)/1.01/RGROUP-C.TSPIN[IWDG-1]
    if (C.BBADJU): C.HPART[IWDG-1]=round(C.HPART[IWDG-1]*2.E+4)/2.E+4

    if (not BBARRR[IWDG-1]) :
        APART=C.HPART[IWDG-1]*BPARTO[IWDG-1]-CORN(BPARTO[IWDG-1])/1.E+6
        C.ZRR[IWDG-1]=C.ACOND[IWDG-1]/APART/C.ZAR[IWDG-1]
        if (C.IPISOL[IWDG-1] > 1): C.ZRR[IWDG-1]=C.ZRR[IWDG-1]/2.
        C.ZRR[IWDG-1]=round(C.ZRR[IWDG-1])
        if (C.ZRR[IWDG-1] < 1.): C.ZRR[IWDG-1]=1.
        if (C.IPISOL[IWDG-1] > 1): C.ZRR[IWDG-1]=C.ZRR[IWDG-1]*2.
    
    C.BPART[IWDG-1]=(C.ACOND[IWDG-1]/C.ZAR[IWDG-1]/C.ZRR[IWDG-1]+
                     CORN(BPARTO[IWDG-1])/1.E+6)/C.HPART[IWDG-1]
    C.ZPART[IWDG-1]=C.ZAR[IWDG-1]*C.ZRR[IWDG-1]
    if ( not BBARRR[IWDG-1]) :
        if (C.HPART[IWDG-1] >= HPARTO[IWDG-1]/2.): goto ._303
        C.ZLAG[IWDG-1]=C.ZLAG[IWDG-1]+1.
        goto ._298

    if (C.BPART[IWDG-1] < BPARTO[IWDG-1]*2. and
        C.HPART[IWDG-1] > HPARTO[IWDG-1]*0.8): goto ._303
    C.ZLAG[IWDG-1]=C.ZLAG[IWDG-1]+1.
    goto ._200

    ''' Fixed dimensions '''

    label ._302
    if (C.BBADJU): C.HPART[IWDG-1]=round(C.HPART[IWDG-1]*2.E+4)/2.E+4
    TURNH=(C.HPART[IWDG-1]+C.TSPIN[IWDG-1])*1.01*C.ZAR[IWDG-1]
    C.ZNLAG[IWDG-1]=HSPOL[IWDG-1]/TURNH-1.
    TRR=(C.BPART[IWDG-1]+C.TSPIN[IWDG-1])*C.ZRR[IWDG-1]+C.HCLAC[IWDG-1]

    if (C.IPISOL[IWDG-1] > 1):
        TRR=(2.*C.BPART[IWDG-1]+C.TSPIN1[IWDG-1]+C.TSPIN[IWDG-1])*C.ZRR[IWDG-1]/2.+C.HCLAC[IWDG-1]
    C.ZLAG[IWDG-1]=((C.RRWDG[IWDG-1]-C.ZCODU[IWDG-1]*4.0/1.E+3)/1.03+C.HCLAC[IWDG-1])/TRR
    if (C.ZLAG[IWDG-1] < 1.): C.ZLAG[IWDG-1]=1.
    if (C.ZLAG[IWDG-1]*C.ZNLAG[IWDG-1] < ZNSPOL) :
        NWARN=0
        WMESS(C.JFC,' Layer winding '+C.NCOL[IWDG-1]+' - data not consistent.           ',NWARN)

    label ._303
    HELP2=ZNSPOL*C.U0*C.BLIMB/C.ZLAG[IWDG-1]

    if (C.KCODE[IWDG-1] !=2) :
        TEST[IWDG-1]=HELP2/ULAG
    else:
        TEST[IWDG-1]=0.
        
    if (TEST[IWDG-1] > 1. and C.BBADJU) :
        ''' WRITE (6,6) IWDG,HELP2,ULAG '''
        NWARN=0
        WMESS(C.JFC,' Layer winding '+C.NCOL[IWDG-1]+' - layer voltage too high.        ',NWARN)

    if(C.BBADJU) :
        C.BPART[IWDG-1]=round(C.BPART[IWDG-1]*2.E+4)/2.E+4
        APART=C.HPART[IWDG-1]*C.BPART[IWDG-1]-CORN(C.BPART[IWDG-1])/1.E+6
        C.ACOND[IWDG-1]=APART*C.ZPART[IWDG-1]*RGROUP

    TRR=(C.BPART[IWDG-1]+C.TSPIN[IWDG-1])*C.ZRR[IWDG-1]+C.HCLAC[IWDG-1]

    if (C.IPISOL[IWDG-1] > 1):
        TRR=(2.*C.BPART[IWDG-1]+C.TSPIN1[IWDG-1]+C.TSPIN[IWDG-1])*C.ZRR[IWDG-1]/2.+C.HCLAC[IWDG-1]
    if ( not C.BBRR[IWDG-1]):
        C.RRWDG[IWDG-1]=(C.ZLAG[IWDG-1]*TRR-C.HCLAC[IWDG-1])*1.03+C.ZCODU[IWDG-1]*4.0/1.E+3
    if (IWDG == 1) :
        C.RINNER[0]=C.DCORE/2.+C.BDUCT[0]
        RINNET[0]=C.DCORE/2.+C.BDUCT[0]
    else:
        C.RINNER[IWDG-1]=C.RINNER[IWDG-2]+C.RRWDG[IWDG-2]+C.BDUCT[IWDG-1]
        RINNET[IWDG-1]=RINNET[IWDG-2]+C.RRWDG[IWDG-2]+RRTADD[IWDG-2]+C.BDUCT[IWDG-1]
    
    RRTADD[IWDG-1]=0.
    C.DSWI[IWDG-1]=0.
    if (IWDG > 1): C.DSWI[IWDG-1]=C.DSWI[IWDG-2]
    if(C.KWIND[IWDG-1] >= 20) :
        BLED=(C.HPART[IWDG-1]+C.TSPIN[IWDG-1])*C.ZAR[IWDG-1]
        RNX=(C.ZLAG[IWDG-1]-1.)*(BLED+0.06)/(2.*C.RINNER[IWDG-1]+C.RRWDG[IWDG-1])*1.5/C.PI
        if(C.BBADJU): RNX=round(RNX*2.+0.49)/2.
        RRX=RNX*(TRR+2.*X3LAY[IWDG-1])
        RRTADD[IWDG-1]=RRX
        C.DSWI[IWDG-1]=C.DSWI[IWDG-1]+0.667*RRX*C.PI

    C.SWIND[IWDG-1]=(2.*C.RINNER[IWDG-1]+C.RRWDG[IWDG-1])*C.PI+C.DSWI[IWDG-1]

    ''' ANTAL VARV REGLEROMR·DET PER PARALLELL GRUPP= ZREG
        ANTAL LAGER SOM KR³VS FöR ATT RYMMA HELA REGLERDELEN=XL
        öKNING AV YTTRE OMKRETS P.G.A UTTAG= C.DSWI[IWDG-1] '''

    if(C.KCODE[IWDG-1] != 1 and C.KCODE[IWDG-1] != 3) :
        JTML=C.KGROUP[IWDG-1]

        if(C.KCODE[IWDG-1] != 4) :
            XL=C.ZLAG[IWDG-1]
            ZREG=C.ZWIND[IWDG-1]
        else:
            ZREG=ZLOOP*C.PUSTEP[JTML-1]*C.ZWIND[IWDG-1]*C.POSIT[IWDG-1][0]/C.POSIT[IWDG-1][1]
            XL=ZREG/C.ZNLAG[IWDG-1]+0.5
            if (C.BBADJU): XL=round(XL+0.49)

        C.ZTULO[IWDG-1]=ZREG/ZLOOP
        if(C.KGROUP[IWDG-1] == IHV) :
            RREX=XL*(C.TSPIN[IWDG-1]+C.HCLAC[IWDG-1]+X4LAY[IWDG-1])
            RRTADD[IWDG-1]=RRTADD[IWDG-1]+RREX
            C.DSWI[IWDG-1]=C.DSWI[IWDG-1]+0.4*RREX

    return

''' FORMAT (1X,'LWIND',I4,' Layer voltages:  ACT=',F10.0,' MAX=',F10.0,' V') '''

