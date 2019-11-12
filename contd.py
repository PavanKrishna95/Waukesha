
''' Title:  Winding layout for continuous disc windings
        Calculations can be done in two ways:
        1. A simple calculation using decimal fractions.
        2. A full calculation with rounding to integer values. '''
from corn import CORN
def CONTD(IWDG):
    import com as C
    HPART1=[0. for i in range(9)]
    EXTU=[0. for i in range(9)]
    EXT20=[0.,2.,2.,2.,4.,4.]
    EXT10=[2.,2.,4.,6.,6.,8.]
    FACINS=0.95

    ''' Help variables HELP1 and X1 have to be initiated. '''

    HELP1=0.
    X1=1.

    ''' LINDNINGSHöJD '''

    C.HWIND[IWDG-1]=C.HLIMB-C.DYOKE[IWDG-1]
    JTML=C.KGROUP[IWDG-1]

    ''' TOTAL BREDD AV KYLKANALER '''

    CDUCT=C.ZCODU[IWDG-1]*0.005
    RGROUP=float(C.NGROUP[IWDG-1])
    HPART1[IWDG-1]=C.HPART[IWDG-1]+C.TSPIN[IWDG-1]
    HELP=C.HWIND[IWDG-1]-C.EXTRAR[IWDG-1]
    if ( C.BBADJU):

        ''' Following calculation formulae are used during the optimization '''

        if (C.KCODE[IWDG-1] == 4):
            HELP=HELP-RGROUP*C.HCLAC[IWDG-1]*(float(C.NPSTEP[JTML-1]+C.NMSTEP[JTML-1])+2.)
        C.ZDISC[IWDG-1]=HELP/(HPART1[IWDG-1]+C.HCLAC[IWDG-1])
        C.ZDISC[IWDG-1]=2.*round(C.ZDISC[IWDG-1]/2.)

        ''' Extra turns '''

        if (C.USURG[JTML-1] <= 380.):
            EXTU[IWDG-1]=C.ZWIND[IWDG-1]*3./100.
        else:
            EXTU[IWDG-1]=C.ZWIND[IWDG-1]*4./100.

        ''' Number of strands '''

        X1=1.
        if (C.IPISOL[IWDG-1] > 1): X1=2.
        while True:
            C.ZPART[IWDG-1]=C.ACOND[IWDG-1]/RGROUP/(C.BPART[IWDG-1]*C.HPART[IWDG-1]-CORN(C.BPART[IWDG-1])/1.E+6)/X1
            C.ZPART[IWDG-1]=round(C.ZPART[IWDG-1])
            if (C.ZPART[IWDG-1] < 1.):
                X1=1.
                C.ZPART[IWDG-1]=1.

            if (X1 > 2. or C.TSPIN[IWDG-1] <= 0.001 or C.ZPART[IWDG-1] < 2. or
                C.IPISOL[IWDG-1] > 1):break
            X1=round(X1+1.)

        if (C.ZPART[IWDG-1] > 8.): C.ZPART[IWDG-1]=8.

        ''' ANTAL VARV/SKIVA '''

        C.ZTUDI[IWDG-1]=(C.ZWIND[IWDG-1]+EXTU[IWDG-1])*RGROUP/C.ZDISC[IWDG-1]
        C.ZTUDI[IWDG-1]=round(C.ZTUDI[IWDG-1]*C.ZPART[IWDG-1])/C.ZPART[IWDG-1]
        if (C.ZTUDI[IWDG-1] < 2.):  C.ZTUDI[IWDG-1]=2.

        if (C.KWITYP[IWDG-1] == 4):
            while True:
                STAB=C.ZTUDI[IWDG-1]*C.ZPART[IWDG-1]/2.
                if (STAB-int(STAB) > 0.25):break
                C.ZTUDI[IWDG-1]=C.ZTUDI[IWDG-1]+1./C.ZPART[IWDG-1]
        
        ''' ANTAL SKIVOR SLUTJUSTERAS '''

        C.ZDISC[IWDG-1]=round((C.ZWIND[IWDG-1]+EXTU[IWDG-1])*RGROUP/C.ZTUDI[IWDG-1]+1.)
        C.ZDISC[IWDG-1]=2.*round(C.ZDISC[IWDG-1]/2.)

        ''' PARTDIM '''

        C.HPART[IWDG-1]=HELP/C.ZDISC[IWDG-1]-C.HCLAC[IWDG-1]-C.TSPIN[IWDG-1]
        C.BPART[IWDG-1]=(C.ACOND[IWDG-1]/RGROUP/C.ZPART[IWDG-1]/X1+
                     CORN(C.BPART[IWDG-1])/1.E+6)/C.HPART[IWDG-1]
        if (C.BBADJU):
            C.HPART[IWDG-1]=round(C.HPART[IWDG-1]*20000.)/20000.
            C.BPART[IWDG-1]=round(C.BPART[IWDG-1]*20000.)/20000.
            C.ACOND[IWDG-1]=RGROUP*C.ZPART[IWDG-1]*X1*(C.HPART[IWDG-1]*C.BPART[IWDG-1]-CORN(C.BPART[IWDG-1]-1)/1.E+6)
    
        C.ZPART[IWDG-1]=C.ZPART[IWDG-1]*X1

        ''' X1 = Number of strands in common covering '''

        if (X1 <= 1.):
            if(C.IPISOL[IWDG-1] <= 1):
                HELP1=0.0003
                if(X1 > 2. or C.HPART[IWDG-1] > 0.012): HELP1=0.0005
                HELP1=C.TSPIN[IWDG-1]/FACINS-HELP1
                C.TSPIN1[IWDG-1]=0.0003
                if(X1 > 2.or C.HPART[IWDG-1] > 0.012): C.TSPIN1[IWDG-1]=0.0005
                HELP1=C.TSPIN[IWDG-1]/FACINS-C.TSPIN1[IWDG-1]

        C.ZRR[IWDG-1]=C.ZPART[IWDG-1]


    ''' THE EXACT FORMULAS FOR THE DISC WINDING DIMENSIONS '''

    ''' BER³KNING AV LINDNINGENS BREDD OCH INNERDIAMETER '''

    if (X1 > 1):
        if (C.IPISOL[IWDG-1]==1):
            C.RRWDG[IWDG-1]=((C.BPART[IWDG-1]+C.TSPIN1[IWDG-1])*X1+HELP1)*C.ZPART[IWDG-1]/X1*C.ZTUDI[IWDG-1]+CDUCT
        elif (C.IPISOL[IWDG-1] > 1):
            C.RRWDG[IWDG-1]=(C.BPART[IWDG-1]*X1+(X1-1.)*C.TSPIN1[IWDG-1]+
                             C.TSPIN[IWDG-1]/FACINS)*C.ZPART[IWDG-1]/X1*C.ZTUDI[IWDG-1]+CDUCT
    
    else:
        C.RRWDG[IWDG-1]=(C.BPART[IWDG-1]+C.TSPIN[IWDG-1]/FACINS)*C.ZPART[IWDG-1]*C.ZTUDI[IWDG-1]+CDUCT


    if (C.BBADJU): C.RRWDG[IWDG-1]=round(C.RRWDG[IWDG-1]*1.E+5)/1.E+5

    if (IWDG == 1):C.RINNER[IWDG-1]=C.DCORE/2.+C.BDUCT[IWDG-1]
    else:C.RINNER[IWDG-1]=C.RINNER[IWDG-2]+C.BDUCT[IWDG-1]+C.RRWDG[IWDG-2]

    C.SWIND[IWDG-1]=(2.*C.RINNER[IWDG-1]+C.RRWDG[IWDG-1])*C.PI
    C.RPART[IWDG-1]=X1

    return
