
''' Title:  Winding layout for screw windings '''
from fprint import FPRINT
from corn import CORN
def SCREW(IWDG):

    import com as C

    while True:
        KW=C.KWIND[IWDG-1]
        ZKW=float(KW)
        RGROUP=float(C.NGROUP[IWDG-1])

        C.HWIND[IWDG-1]=C.HLIMB-C.DYOKE[IWDG-1]

        ''' Extra clacks at transpositions '''

        if (KW > 1):
            Q=0.
        else:
            Q=1.

        ''' Number of discs '''

        C.ZDISC[IWDG-1]=round(C.ZWIND[IWDG-1]+1.0)*RGROUP*ZKW

        ''' Strand height '''

        C.HPART[IWDG-1]=((C.HWIND[IWDG-1]-C.EXTRAR[IWDG-1])/RGROUP-
                     ZKW*round(C.ZWIND[IWDG-1])*C.HCLAC[IWDG-1]-C.HCLAC[IWDG-1]*
                     (C.ZRR[IWDG-1]+3.)*Q-(ZKW-1.)*C.HCLAC[IWDG-1])/(ZKW*round(C.ZWIND[IWDG-1]+1.0))-C.TSPIN[IWDG-1]
        C.HPART[IWDG-1]=round(C.HPART[IWDG-1]*2.E+4)/2.E+4

        if(C.HPART[IWDG-1] >= 0.020 and KW <= 3):
            C.KWIND[IWDG-1]=KW+1
            C.ZAR[IWDG-1]=C.KWIND[IWDG-1]
            NWARN=0
            WMESS(C.JFC,' Screw winding '+C.NCOL[IWDG-1]+
              ' - No. of strands in AR increased.',NWARN)
            continue
        if (C.HPART[IWDG-1] <=0.001):
            if (KW == 1):
                FPRINT(2,C.BBERR,C.BBHELP,C.BBTS,C.JFC,
                        'SCREW:Strand height of winding '+C.NCOL[IWDG-1]+' is too low.')
            ''' Backtracking '''
        
            if(C.ISTOP == 1):return

            C.KWIND[IWDG-1]=KW-1
            C.ZAR[IWDG-1]=C.KWIND[IWDG-1]
            NWARN=0
            WMESS(C.JFC,' Screw winding '+C.NCOL[IWDG-1]+
              ' - No. of strands in AR decreased.',NWARN)
            continue
        else:break

    ''' Number of strands '''

    C.ZPART[IWDG-1]=C.ACOND[IWDG-1]/RGROUP/(C.HPART[IWDG-1]*C.BPART[IWDG-1]-CORN(C.BPART[IWDG-1])*1.E-6)
    if(C.ZPART[IWDG-1] <= 0.): C.ZPART[IWDG-1]=15.

    ''' Number of strands in RR : 0.35 limits the width upwards '''

    C.ZRR[IWDG-1]=round(C.ZPART[IWDG-1]/ZKW+0.35)
    while True:
        C.ZPART[IWDG-1]=C.ZRR[IWDG-1]*ZKW
        C.BPART[IWDG-1]=(C.ACOND[IWDG-1]/RGROUP/C.ZPART[IWDG-1]+
                     CORN(C.BPART[IWDG-1])*1.E-6)/C.HPART[IWDG-1]
        C.BPART[IWDG-1]=round(C.BPART[IWDG-1]*2.E+4)/2.E+4

        ''' Check the tilting force '''

        HTILT=3.E+3*C.BPART[IWDG-1]*C.BPART[IWDG-1]
        if(C.HPART[IWDG-1] < HTILT or C.ZRR[IWDG-1] < 2.): break
        C.ZRR[IWDG-1]=C.ZRR[IWDG-1]-1.


    ''' Calculate winding width and inner diameter '''

    C.RRWDG[IWDG-1]=(C.BPART[IWDG-1]+C.TSPIN[IWDG-1]/0.95)*C.ZRR[IWDG-1]+C.ZCODU[IWDG-1]*0.005

    C.RRWDG[IWDG-1]=round(C.RRWDG[IWDG-1]*1.E+5)/1.E+5
    if(IWDG == 1):
        C.RINNER[IWDG-1]=C.DCORE/2.+C.BDUCT[IWDG-1]
    else:
        C.RINNER[IWDG-1]=C.RINNER[IWDG-2]+C.BDUCT[IWDG-1]+C.RRWDG[IWDG-2]
       
    C.SWIND[IWDG-1]=(2.*C.RINNER[IWDG-1]+C.RRWDG[IWDG-1])*C.PI
    return
