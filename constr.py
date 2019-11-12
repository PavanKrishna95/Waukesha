
'''  Title: Determination of those limits
            which have been exceeded '''
from limchk import LIMCHK
def CONSTR():
    import com as C
    C.NCONST=0
    C.SAVE1=['' for i in range(50)]
    ''' Check the limits '''

    if (C.PLOADM > 0):
        C.NCONST,C.SAVE1=LIMCHK (C.URC[0][0][0]*C.ZWOULI/C.PLOADM ,' PLOADM','*PLOADM',
                C.NCONST,C.SAVE1)

    ''' Switch off structure analysis (Not all calls need be shown) '''

    if(C.PNOLOM > 0):
        C.NCONST,C.SAVE1=LIMCHK (C.P00[0]/C.PNOLOM,' PNOLOM','*PNOLOM',C.NCONST,C.SAVE1)
    C.NCONST,C.SAVE1=LIMCHK (C.DCORE/C.DCOMAX ,' DCOMAX','*DCOMAX',C.NCONST,C.SAVE1)
    C.NCONST,C.SAVE1=LIMCHK (C.DCOMIN/C.DCORE ,' DCOMIN','*DCOMIN',C.NCONST,C.SAVE1)
    C.NCONST,C.SAVE1=LIMCHK (C.HTANK/C.HTANKM ,' HTANKM','*HTANKM',C.NCONST,C.SAVE1)
    C.NCONST,C.SAVE1=LIMCHK (C.HLIMB/C.HLMBMA ,' HLMBMA','*HLMBMA',C.NCONST,C.SAVE1)
    C.NCONST,C.SAVE1=LIMCHK (C.HLMBMI/C.HLIMB ,' HLMBMI','*HLMBMI',C.NCONST,C.SAVE1)
    C.NCONST,C.SAVE1=LIMCHK (C.BTANK/C.BTANKM ,' BTANKM','*BTANKM',C.NCONST,C.SAVE1)
    C.NCONST,C.SAVE1=LIMCHK (C.RLTANK/C.RLTNKM,' LTANKM','*LTANKM',C.NCONST,C.SAVE1)
    C.NCONST,C.SAVE1=LIMCHK (C.GTRP/C.GTRPM   ,' GTRPM ','*GTRPM ',C.NCONST,C.SAVE1)
    if(C.SOUNDM > 0):
        C.NCONST,C.SAVE1=LIMCHK (C.SOUND0[1]/C.SOUNDM,' SOUNDM','*SOUNDM',C.NCONST,C.SAVE1)

    ''' Switch on  structure analysis (Not all calls need be shown) '''

    ''' Windings '''

    for IWDG in range(1,C.NWILI+1):

        ''' Prepare the parameters '''

        ''' Start of the preparation block. '''

        TEXT1= ' CURD '+str(IWDG)
        TEXT2= '*CURD '+str(IWDG)

        ''' End of the preparation block. '''

        ''' Check the limit '''

        C.NCONST,C.SAVE1=LIMCHK (C.CURDEN[IWDG-1]/C.CURDM[IWDG-1],TEXT1,TEXT2,C.NCONST,C.SAVE1)

        ''' Switch OFF structure analysis (Not all calls need be shown) '''

        TEXT1= ' PRESS'+str(IWDG)
        TEXT2= '*PRESS'+str(IWDG)
        C.NCONST,C.SAVE1=LIMCHK(abs(C.STRWMM[IWDG-1]/C.PRESSM[IWDG-1]),TEXT1,TEXT2,C.NCONST,C.SAVE1)
        TEXT1= ' TENS '+str(IWDG)
        TEXT2= '*TENS '+str(IWDG)
        C.NCONST,C.SAVE1=LIMCHK(abs(C.STRWMP[IWDG-1]/C.TENSM[IWDG-1]),TEXT1,TEXT2,C.NCONST,C.SAVE1)

        ''' Switch ON  structure analysis (Not all calls need be shown) '''

    return
    
