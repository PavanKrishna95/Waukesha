
''' Title:  Adjust the conductor dimensions
            to the nearest standard value. '''
from goto import with_goto
from contd import CONTD
from corn import CORN
@with_goto
def ADJUST():
    import com as C
    NDISC =[0 for i in range(9)]
    C.BBADJU= True
    C.HLIMB=round(C.HLIMB*1000.)/1000.

    for IWDG in range(1,C.NWILI+1):
        C.HWIND[IWDG-1]=C.HLIMB-C.DYOKE[IWDG-1]
        RGROUP=float(C.NGROUP[IWDG-1])
        USURGK=C.USURG[C.KGROUP[IWDG-1]-1]

        ''' Disc winding '''

        if (C.KWIND[IWDG-1] == 0 or C.KWIND[IWDG-1] == 100):

            if ( not C.BBRR[IWDG-1]):CONTD(IWDG)

            ZPART1=C.ZPART[IWDG-1]
            X1=1.
            if (USURGK > 380.): 
                if (abs(int(ZPART1/3.)-ZPART1/3.) < 0.01): X1=3.
                if (X1 != 3. or C.HPART[IWDG-1] <= 0.012): 
                    X1=1.
                    if (abs(int(ZPART1/2.)-ZPART1/2.) < 0.01): X1=2.
    
            if (int(C.ZTUDI[IWDG-1])< C.ZTUDI[IWDG-1] and
                int(ZPART1/(X1*2.)) < ZPART1/(X1*2.)): X1=1.
            HELP1=0.
            if (X1 != 1.):
                if (X1 == 3.): HELP1=C.TSPIN[IWDG-1]/0.95-0.0005
                if (X1 != 3.):
                    if (C.HPART[IWDG-1] > 0.012): HELP1=C.TSPIN[IWDG-1]/0.95-0.0005
                    if (C.HPART[IWDG-1] <= 0.012): HELP1=C.TSPIN[IWDG-1]/0.95-0.0003

            C.TSPIN1[IWDG-1]=C.TSPIN[IWDG-1]/0.95-HELP1
            if (C.IPISOL[IWDG-1] == 2): C.TSPIN1[IWDG-1]=0.15E-3
            if (C.IPISOL[IWDG-1] == 3): C.TSPIN1[IWDG-1]=0.18E-3
            if ( not C.BBRR[IWDG-1]):
                C.RRWDG[IWDG-1]=((C.BPART[IWDG-1]+C.TSPIN1[IWDG-1])*X1+HELP1)*ZPART1/X1*C.ZTUDI[IWDG-1]+C.ZCODU[IWDG-1]*0.005
            if (not C.BBRR[IWDG-1] and C.IPISOL[IWDG-1] >= 2 and C.IPISOL[IWDG-1] <= 3):
                C.RRWDG[IWDG-1]=(C.BPART[IWDG-1]*X1+C.TSPIN1[IWDG-1]*(X1-1.)+C.TSPIN[IWDG-1])*ZPART1/X1*C.ZTUDI[IWDG-1]+C.ZCODU[IWDG-1]*0.005
            C.RPART[IWDG-1]=round(X1)
            goto ._8900

            ''' Screw '''

        else:
            if (C.KWIND[IWDG-1] <= 6): 
                NDISC[IWDG-1]=round(C.ZDISC[IWDG-1])
                if (not C.BBRR[IWDG-1]):  goto ._8900
                Q=1.
                if (C.KWIND[IWDG-1] == 1 and C.HCLAC[IWDG-1] < 0.0025):Q=2.
                if (C.KWIND[IWDG-1] > 1): Q=0.

                if (not C.BBRR[IWDG-1]):
                    C.ZRR[IWDG-1]=round(C.ZRR[IWDG-1])
                    C.ZPART[IWDG-1]=C.ZRR[IWDG-1]*float(C.KWIND[IWDG-1])
                    C.BPART[IWDG-1]=C.ACOND[IWDG-1]/(C.HPART[IWDG-1]*C.ZPART[IWDG-1])/RGROUP
                    if (C.BPART[IWDG-1] > 0.003): C.ZRR[IWDG-1]=C.ZRR[IWDG-1]+1.
                    C.ZPART[IWDG-1]=C.ZRR[IWDG-1]*float(C.KWIND[IWDG-1])

                KW=C.KWIND[IWDG-1]
                C.ZDISC[IWDG-1]=(C.ZWIND[IWDG-1]+1.)*RGROUP*KW
                NDISC[IWDG-1]=round(C.ZDISC[IWDG-1])
                C.ZDISC[IWDG-1]=float(NDISC[IWDG-1])
                if (C.BBRR[IWDG-1]): goto ._8900
                C.HPART[IWDG-1]=((C.HWIND[IWDG-1]-C.EXTRAR[IWDG-1])/RGROUP-
                         KW*C.ZWIND[IWDG-1]*C.HCLAC[IWDG-1]-C.HCLAC[IWDG-1]*
                         (C.ZRR[IWDG-1]+3.)*Q-(KW-1.)*C.HCLAC[IWDG-1])/(KW*(C.ZWIND[IWDG-1]+1.))-C.TSPIN[IWDG-1]
                if ( not C.BBRR[IWDG-1]):
                    C.HPART[IWDG-1]=round(C.HPART[IWDG-1]*20000.)/20000.
                    C.BPART[IWDG-1]=(C.ACOND[IWDG-1]/C.ZPART[IWDG-1]/RGROUP+
                             CORN(C.BPART[IWDG-1])*1.E-6)/C.HPART[IWDG-1]
                    C.BPART[IWDG-1]=round(C.BPART[IWDG-1]*20000.)/20000.
    
                C.RRWDG[IWDG-1]=(C.BPART[IWDG-1]+C.TSPIN[IWDG-1]/0.95)*C.ZRR[IWDG-1]+C.ZCODU[IWDG-1]*0.005
                goto ._8900

                ''' Sling '''
            else:
        
                if (C.KCODE[IWDG-1] != 2):
                    if (C.KWIND[IWDG-1] > 10 and C.KWIND[IWDG-1] < 40):
                        C.FILLF[IWDG-1]=C.ACOND[IWDG-1]*C.ZWIND[IWDG-1]/(C.HWIND[IWDG-1]*C.RRWDG[IWDG-1])
                        continue

                if (not C.BBRR[IWDG-1]):
                    C.HPART[IWDG-1]=round(C.HPART[IWDG-1]*20000.)/20000.
                    C.BPART[IWDG-1]=(C.ACOND[IWDG-1]/C.ZPART[IWDG-1]+
                         CORN(C.BPART[IWDG-1])*1.E-6)/C.HPART[IWDG-1]/RGROUP
                    C.BPART[IWDG-1]=round(C.BPART[IWDG-1]*20000.)/20000.
                    C.ZLAG[IWDG-1]=1.
                    C.ZCOIAR[IWDG-1]=1.
                    C.ZNLAG[IWDG-1]=C.ZWIND[IWDG-1]
                    C.RRWDG[IWDG-1]=float(C.NLORR[IWDG-1])*(C.BPART[IWDG-1]+C.TSPIN[IWDG-1]/0.95)
       

        label ._8900
        if (not C.BBRR[IWDG-1]):
            C.ACOND[IWDG-1]=C.ZPART[IWDG-1]*(C.HPART[IWDG-1]*C.BPART[IWDG-1]-
                                             CORN(C.BPART[IWDG-1])*1.E-6)*RGROUP
        C.RRWDG[IWDG-1]=round(C.RRWDG[IWDG-1]*1000.+0.49)/1000.

        if (IWDG == 1):
            C.RINNER[IWDG-1]=C.DCORE/2.+C.BDUCT[IWDG-1]
        else:
            C.RINNER[IWDG-1]=C.RINNER[IWDG-2]+C.BDUCT[IWDG-1]+C.RRWDG[IWDG-2]
    
        C.SWIND[IWDG-1]=(2.*C.RINNER[IWDG-1]+C.RRWDG[IWDG-1])*C.PI

        C.FILLF[IWDG-1]=C.ACOND[IWDG-1]*C.ZWIND[IWDG-1]/(C.HWIND[IWDG-1]*C.RRWDG[IWDG-1])

    return
