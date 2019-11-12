
''' Title: ControlliC.NG routine for output of results '''
from fbb import FBB
from page01 import PAGE01
from page02 import PAGE02
from kuts import KUTS
#from tab79 import TAB79
def PAGEUT(BBRES):
    import com as C
    import common as CM

    CONVAR=['' for i in range(9)]
    TCEPOX=['' for i in range(9)]

    for IWDG in range(1,C.NWILI+1):
        CONVAR[IWDG-1]=C.UARR[30+IWDG-1]
        TCEPOX[IWDG-1]=C.UARR[40+IWDG-1]
        
    BFINE=FBB('PAGEUT',C.BBERR,C.TARR[77])
    BBOPCH=FBB('PAGEUT',C.BBERR,C.TARR[59])
    BB79  = (C.MNLY >=79 and C.MNLY < 91)

    ''' Output of results '''

    PAGE01()

    ''' Further output of results '''

    if(BBOPCH): PAGE02(C.JFC,C.BBOUT,BBRES)

    ''' Output of masses and costs '''

    ''' WRITE(C.JFC,80 ) '''

    ''' Print costs '''

    if(BB79):
        KUTS(C.JFC,C.NWILI,C.IDENT,C.DATE,C.IPAGE,C.RUBCH,BBFINE,
             CONVAR,TCEPOX)
        #TAB79 (CM.RES79,C.JFC,C.CHCOST,C.NWILI)
        if(BBFINE):''' PAGE79()'''
