
''' Title: Transfers terminal data from indata fields to
           internal variables, and converts them to SI-units.
           Corresponding indata checks are performed. '''
from fprint import FPRINT
def SITERM():
    import com as C
    C.BBVFR=False
    if(C.TARR[1]=='YES'): C.BBVFR=True

    ''' For each terminal '''

    for JTML in range(1,C.NG+1):
        C.SRATE[JTML-1]=1.E+6*C.AARR[10+JTML-1]
        C.UNLINE[JTML-1]=1.E+3*C.AARR[15+JTML-1]

        ''' Set Step dimensions '''

        ''' If a regulated terminal '''
        if(C.BBVR[JTML-1]):
            C.NPSTEP[JTML-1]=C.IARR[5+JTML-1]
            C.NMSTEP[JTML-1]=C.IARR[10+JTML-1]
            C.PUSTEP[JTML-1]=C.AARR[20+JTML-1]/1.E+2

            ''' Tap outside specified range '''

            if ((round(C.FARR[52+JTML-1])>(C.NPSTEP[JTML-1]) or
                 round(C.FARR[52+JTML-1])<(-C.NMSTEP[JTML-1]))):
                C.JFC,C.BBERR=FPRINT(2,C.BBERR,
                            'SITERM:Calculation tap chosen beyond the regulation range')

            C.NXSTEP[JTML-1]=int(0.5+C.FARR[52+JTML-1]+C.NMSTEP[JTML-1])

            C.KTYPRW[JTML-1]=0
           
            if (C.TARR[10+JTML-1]=='L'): C.KTYPRW[JTML-1]=1
            if (C.TARR[10+JTML-1]=='PM'): C.KTYPRW[JTML-1]=2
            if (C.TARR[10+JTML-1]=='CF'): C.KTYPRW[JTML-1]=3

            ''' Regulation type not recognised '''
            
            if (C.KTYPRW[JTML-1]==0):
                C.JFC,C.BBERR=FPRINT(2,C.BBERR,
                            'SITERM:Regulating Winding not: L PM CF')

        C.KCON[JTML-1]=-1
        if (C.TARR[20+JTML-1]=='I'): C.KCON[JTML-1]=0
        if (C.TARR[20+JTML-1]=='Y'): C.KCON[JTML-1]=1
        if (C.TARR[20+JTML-1]=='YN'): C.KCON[JTML-1]=1
        if (C.TARR[20+JTML-1]=='D'): C.KCON[JTML-1]=3
        if (C.TARR[20+JTML-1]=='I/AUTO'): C.KCON[JTML-1]=10
        if (C.TARR[20+JTML-1]=='I/A'): C.KCON[JTML-1]=10
        if (C.TARR[20+JTML-1]=='Y/AUTO'): C.KCON[JTML-1]=11
        if (C.TARR[20+JTML-1]=='Y/A'): C.KCON[JTML-1]=11

        ''' Connection illegally stated '''

        if (C.KCON[JTML-1]==-1):
            C.JFC,C.BBERR=FPRINT(2,C.BBERR,
                    'SITERM:Connection illegally stated')

        ''' Autoconnection only for Term 1 and 2 '''

        if (C.KCON[JTML-1]>9 and JTML>2):
            C.JFC,C.BBERR=FPRINT(2,C.BBERR,
                        'SITERM:Autoconnection only for Term 1 and 2') 

        C.USURG[JTML-1]=1.E+3*C.AARR[25+JTML-1]
        C.SLINE[JTML-1]=1.E+9*C.AARR[30+JTML-1]
        if (JTML <= 3): C.XRINT[JTML-1]=C.AARR[35+JTML-1]/1.E+2

    C.XRINT[3]=0.

    C.BBAUTO=(C.KCON[0] >= 10 or C.KCON[1] >= 10)

    HLP=abs(C.SRATE[0]-C.SRATE[1])

    ''' Rating 1 not equal 2 when autoconnected '''

    if (C.BBAUTO and  HLP> 1.):
        C.JFC,C.BBERR=FPRINT(2,C.BBERR,
                    'SITERM:Rating 1 not equal 2 when autoconnected')

    ''' Connection 1 not equal 2 when autoconnected '''

    if (C.BBAUTO and C.KCON[0] != C.KCON[1]):
        C.JFC,C.BBERR=FPRINT(2,C.BBERR,
                    'SITERM:Connection 1 not equal 2 when autoconnected')

    BBA=(C.NG >= 3 and C.BBVR[2])
    BBB=(C.BBVR[0] or not C.BBVR[1] or BBA)
    
    ''' ONLY Terminal 2 shall be regulated when ind.regulation '''

    if (C.BBVFR and BBB):
        C.JFC,C.BBERR=FPRINT(2,C.BBERR,
                    'SITERM:ONLY Terminal 2 shall be regulated when ind.regulation')

    ''' C.BBUPTR = Step-up transformer 
        C.NPG=Terminal number for the parallel winding
        C.NSG=Terminal number for the series   winding '''

    C.BBUPTR=(C.UNLINE[1] >= C.UNLINE[0])
    C.NPG=2
    if (C.BBUPTR):C.NPG=1
    C.NSG=3-C.NPG

    return
