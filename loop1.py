''' Title:  Winding layout for SLL-windings '''

from goto import with_goto
from fprint import FPRINT
from wmess import WMESS
from corn import CORN
@with_goto
def LOOP1(IWDG):

    NWARN=[0,0,0,0,0]

    C.HWIND[IWDG-1]=C.HLIMB-C.DYOKE[IWDG-1]

    ''' No. of turns/loop '''

    C.ZTULO[IWDG-1]=C.ZWIND[IWDG-1]/float(C.NLOOP[IWDG-1])

    ''' Strand height '''

    HELP=(C.HWIND[IWDG-1]-C.EXTRAR[IWDG-1])/float(C.NGROUP[IWDG-1])
    label ._10
    if (C.KWIND[IWDG-1] == 7 or C.KWIND[IWDG-1] == 10):
        C.HPART[IWDG-1]=HELP/(float(C.NLOOP[IWDG-1])/float(C.NLORR[IWDG-1])*(C.ZTULO[IWDG-1]+1.))-C.TSPIN[IWDG-1]

    label ._20
    if (C.KWIND[IWDG-1] == 8 or C.KWIND[IWDG-1] == 11):
        C.HPART[IWDG-1]=(HELP-float(C.NLOOP[IWDG-1]+1)*0.005)/((C.ZTULO[IWDG-1]+1.)*float(C.NLOOP[IWDG-1])/float(C.NLORR[IWDG-1]))-C.TSPIN[IWDG-1]

    if (C.KWIND[IWDG-1] == 9):
        C.HPART[IWDG-1]=(HELP-float(C.NLOOP[IWDG-1]+1)*0.01)/(float(C.NLOOP[IWDG-1])*(C.ZTULO[IWDG-1]+1.))-C.TSPIN[IWDG-1]

    if (C.HPART[IWDG-1] <= 0.020 or C.KWIND[IWDG-1] != 11): goto ._300
    C.KWIND[IWDG-1]=7
    C.NLORR[IWDG-1]=1
    NWARN[3]=0
    MESTXT='LOOP1:SLL2 changed to SLL1 - Winding '+C.NCOL[IWDG-1]+' strand height > 20 mm )        '
    WMESS (C.JFC,MESTXT,NWARN[4])
    goto ._10

    label ._300
    if (C.HPART[IWDG-1] <= 0.001):
        if (C.HPART[IWDG-1]<= 0.007): goto ._350
        C.KWIND[IWDG-1]=11
        C.NLORR[IWDG-1]=2
        NWARN[4]=0
        MESTXT='LOOP1:SLL1 changed to SLL2 - Winding '+C.NCOL[IWDG-1]+' strand height <  1 mm )        '
        WMESS (C.JFC,MESTXT,NWARN[3])
        goto ._20
        label ._350
        C.JFC,C.BBERR=FPRINT(2,C.BBERR,
               'LOOP1:Strand height of winding '+C.NCOL[IWDG-1]+' is too low.')
        exit()

    ''' Strand width '''

    C.BPART[IWDG-1]=(C.ACOND[IWDG-1]/C.ZPART[IWDG-1]+CORN(C.BPART[IWDG-1])*1.E-6)/C.HPART[IWDG-1]/C.NGROUP[IWDG-1]

    ''' Calculate winding width and inner diameter '''

    C.RRWDG[IWDG-1]=(C.BPART[IWDG-1]+C.TSPIN[IWDG-1]/0.95)*float(C.NLORR[IWDG-1])+0.0005
    if (IWDG == 1):
        C.RINNER[IWDG-1]=C.DCORE/2.+C.BDUCT[IWDG-1]
    else:
        C.RINNER[IWDG-1]=C.RINNER[IWDG-2]+C.BDUCT[IWDG-1]+C.RRWDG[IWDG-2]


    C.SWIND[IWDG-1]=(2.*C.RINNER[IWDG-1]+C.RRWDG[IWDG-1])*C.PI

    ''' Check winding strand width '''

    DWIND = 2.*C.RINNER[IWDG-1]+C.RRWDG[IWDG-1]
    if(C.BBADJU and C.BPART[IWDG-1] < DWIND/200.):
        MESTXT='LOOP1:Winding '+C.NCOL[IWDG-1]+' strand width is less '+'than DWIND/200 (Series loop)     '
        WMESS (C.JFC,MESTXT,NWARN[0])

    if(C.BBADJU and C.BPART[IWDG-1] < 0.004):
        MESTXT='LOOP1:Winding '+C.NCOL[IWDG-1]+' strand width is less '+'than 4 mm      (Series loop)     '
        WMESS (C.JFC,MESTXT,NWARN[1])

    if(C.BBADJU and C.BPART[IWDG-1] < 1.5*C.TSPIN[IWDG-1]):
        MESTXT='LOOP1:Winding '+C.NCOL[IWDG-1]+' strand width is less '+'than 1.5*C.TSPIN (Series loop)     '
        WMESS (C.JFC,MESTXT,NWARN(3))

    ''' Instructions for TAC and for temperature calculation '''

    C.ZLAG[IWDG-1]=1.
    C.ZCOIAR[IWDG-1]=1.
    C.ZNLAG[IWDG-1]=C.ZWIND[IWDG-1]

    return
