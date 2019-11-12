
'''   Title:   Prints a new heading if required.
            If BBERR1 =.TRUE. an error message is
            printed at the top of each page. '''
from errrut import ERRRUT
def NPAGE(KRAD):
    import com as C
    ''' Declarations '''

    IRAD=KRAD

    ''' Write heading '''

    ''' If a new page '''

    if(IRAD>64 or KRAD<0):
        C.IPAGE=C.IPAGE+1

    ''' Write the heading '''
    ''' WRITE(JFC, 81) (IDENT(I),I=1,9),DATE,IPAGE '''

    ''' Print error warning if needed '''

    if(C.BBERR1 or C.BBFREQ):
        ERRRUT(BBERR1,BBFREQ,JFC)
        IRAD=KRAD


    ''' 81  FORMAT(1H1,'     ',9A4,A26,' Page',I2/1X)
        END '''
