
''' Title:  Checks for correct winding function codes
            and for correct winding fractions '''
from fprint import FPRINT
def CHFUNK():
    import com as C

    LX=[[0 for i in range(4)] for j in range(4)]

    ''' Determination of the No. of windings and their respective
        function codes per terminal. '''

    for IWDG in range(1,C.NWILI+1):
        LX[C.KCODE[IWDG-1]-1][C.KGROUP[IWDG-1]-1]=1+LX[C.KCODE[IWDG-1]-1][C.KGROUP[IWDG-1]-1]

    ''' Loop covering checks for each winding by terminal. '''

    for ITML in range(1,C.NG+1):

        ''' Regulating windings are stated illegally. '''

        if( LX[1][ITML-1]+LX[3][ITML-1] > 1  or  LX[2][ITML-1]+LX[3][ITML-1] > 1
             or (LX[2][ITML-1] == 1 and LX[1][ITML-1] != 1)) :
            C.JFC,C.BBERR=FPRINT(2,C.BBERR,
                   'CHFUNK:Reg windings are stated illegally') 
            ''' BACKTRACKING '''
            if(C.ISTOP == 1): return

        ''' Main winding missing. '''

        if(LX[0][ITML-1]+LX[3][ITML-1] < 1) :
            C.JFC,C.BBERR=FPRINT(2,C.BBERR,
                        'CHFUNK:Main winding missing')
            ''' BACKTRACKING '''
            if(C.ISTOP == 1): return

        ''' Initialisation of MTML '''

        MTML=ITML

        ''' Determine MTML , the terminal No. used later. '''

        ''' VFR and terminals 1 & 2 only. '''

        if(ITML <= 2 and   C.BBVFR):

            ''' Determine MTML. '''

            MTML=1
            if(C.BBAUTO): MTML=C.NPG

        ''' Checking the Regulating winding function. '''

        ''' Regulated terminal. '''

        if(C.BBVR[ITML-1]) :

            ''' Preparing some logical variables. '''

            LX1M=LX[0][MTML-1]
            LX2M=LX[1][MTML-1]
            LX3M=LX[2][MTML-1]
            LX4M=LX[3][MTML-1]
            BBX1=False
            if (C.KTYPRW[ITML-1] == 1 and  not (LX2M+LX4M == 1 and LX3M == 0)):BBX1=True
            BBX2=False
            if (C.KTYPRW[ITML-1] == 2 and  not (LX2M == 1 and LX3M+LX4M == 0)):BBX2=True
            BBX3=False
            if (C.KTYPRW[ITML-1] == 3 and  not (LX2M*LX3M == 1 and LX4M == 0)):BBX3=True

            ''' Regulating winding conflicts with function code. '''

            if(BBX1 or BBX2 or BBX3) :
                    C.JFC,C.BBERR=FPRINT(2,C.BBERR,
                            'CHFUNK:Reg-wdg conflicts with function code') 
                    ''' BACKTRACKING '''
                    if(C.ISTOP == 1): return
    
            ''' NON-regulated terminal. '''

        else:

            ''' Preparing some logical variables. '''

            BBX1=False
            if ( not (C.BBVFR and ITML == MTML)):BBX1=True
            BBX2=False
            if ((LX[1][ITML-1]+LX[2][ITML-1]+LX[3][ITML-1]) > 0):BBX2=True

            ''' Reg-wdg given on non-regulated terminal '''

            if(BBX1 and BBX2) :
                C.JFC,C.BBERR=FPRINT(2,C.BBERR,
                       'CHFUNK:Reg-wdg given on non-regulated terminal') 
                ''' BACKTRACKING '''
                if(C.ISTOP == 1): return

        ''' Initialisation prior to winding fractions check. '''

        SUM=0.
        X=1.

        ''' Winding fraction check '''

        for JWDG in range(1,C.NWILI+1):

            ''' If the winding belongs to the group being calculated ..... '''

            if(C.KGROUP[JWDG-1] == ITML) :

                ''' Calculate the fractions and add as necessary '''

                if(C.BBRW[JWDG-1]): X=X*C.FRACT[JWDG-1]
                if( not C.BBRW[JWDG-1]): SUM=SUM+C.FRACT[JWDG-1]

        ''' Sum of fractions is not equal to 1. '''

        if(abs(SUM-1.0)+abs(X-1.0) > 1.E-6) :
            C.JFC,C.BBERR=FPRINT(2,C.BBERR,
                   'CHFUNK:Sum of fractions is not equal to 1') 
            ''' BACKTRACKING '''
            if(C.ISTOP == 1): return

    return
