
''' Title:  Calculation of Gross Thickness of Core Plate
            at the current Width of Packet '''
from corvar import CORVAR
def FTJBR(TNCORS,ETA,ETAL,ILACK,TYP,DCOR,B):

    FTJBR = TNCORS/ETA
    if(ILACK !=2):
        if(ILACK == 1):
            FTJBR = TNCORS/ETAL
        else:
            if(CORVAR(TYP,DCOR,B)): FTJBR = TNCORS/ETAL

    return FTJBR
