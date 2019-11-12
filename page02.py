
''' Title: Output of detailed losses, no-load losses,
            sound level, reactances, voltage drop and efficiency,
            & check of short circuit stresses. '''

from npage import NPAGE
from opcalc import OPCALC
from prnld import PRNLD
from prux import PRUX
from preff import PREFF
from scdime import SCDIME
def PAGE02(JFC,BBOUT,BBRES):

    BBOUT= True

    ''' Load losses '''

    ''' Start of the load losses block. '''

    ''' New page '''
 
    NPAGE(0)
    ''' WRITE(JFC, 80) '''

    ''' Calculation routine '''

    OPCALC(BBOUT)

    ''' End of the load losses block. '''

    ''' No-load losses and efficiency '''

    PRNLD(BBRES)

    ''' Reactances '''

    PRUX()

    ''' Voltage cases and efficiency '''

    PREFF()

    ''' Short-circuit voltages '''

    ''' New page '''

    NPAGE(0)
    ''' WRITE(JFC,85) '''

    ''' Short circuit dimensioning routine '''

    SCDIME(BBOUT)

    BBOUT = False

    return
