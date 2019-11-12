
''' Title:    Calculate:
                1. The physical number of turns in each winding
                2. The geometrical dimensions of each winding '''

from typwdg import TYPWDG
from wdgtyp import WDGTYP
from screw import SCREW
from contd import CONTD
from lwind import LWIND
from loop1 import LOOP1
from adjust import ADJUST
def WDGLAY():

    ''' WRITE (*,100) 'Automatic winding layout' '''

    ''' Convert the winding types for the winding layout routines '''
    import com as C
    TYPWDG()

    WDGTYP()

    for IWDG in range(1,C.NWILI+1):
        C.RPART[IWDG-1]=1.

        ''' Calculate winding '''

        ''' Radial dimension Using space factors '''

        if (C.BBRR[IWDG-1]):
            C.HWIND[IWDG-1]=C.HLIMB-C.DYOKE[IWDG-1]
            C.RRWDG[IWDG-1]=C.ZWIND[IWDG-1]*C.ACOND[IWDG-1]/C.HWIND[IWDG-1]/C.FILLF[IWDG-1]

            if (IWDG == 1):
                C.RINNER[IWDG-1]=C.DCORE/2.+C.BDUCT[IWDG-1]
            else:
                C.RINNER[IWDG-1]=C.RINNER[IWDG-2]+C.BDUCT[IWDG-1]+C.RRWDG[IWDG-2]
    
            C.SWIND[IWDG-1]=(2.*C.RINNER[IWDG-1]+C.RRWDG[IWDG-1])*C.PI

            ''' Complete winding layout '''

        else:

            if  (C.KWITYP[IWDG-1] == 1 or C.KWITYP[IWDG-1] ==6):
                SCREW(IWDG)
            elif (C.KWITYP[IWDG-1] == 2):
                LWIND(IWDG)
            elif (C.KWITYP[IWDG-1] == 3 or C.KWITYP[IWDG-1] == 4 or C.KWITYP[IWDG-1] ==5) :
                CONTD(IWDG)
            elif (C.KWITYP[IWDG-1] == 7):
                LOOP1(IWDG)

    ''' BACKTRACKING '''
    
    if(C.ISTOP == 1):return

    ''' Convert the winding types for the main program routines '''

    WDGTYP()

    ADJUST()
    C.BBADJU=True

    return
