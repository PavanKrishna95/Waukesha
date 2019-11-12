
''' Title:  Reading & analysis of indata for the
           power transformer optimisation program '''

from siterm import SITERM
from siwind import SIWIND
from siactp import SIACTP
from sitank import SITANK
from prepar import PREPAR
#from nlossr import NLOSSR
from chfunk import CHFUNK
from preset import PRESET
from voltag import VOLTAG
from curdim import CURDIM
from turnca import TURNCA
from check import CHECK

def HEAD1():
    print('Start HEAD1')
    import com as C
    C.BBERR1=False
    CORESE=C.UARR[20]
    ''' Set the output file (JFC) '''
    ''' REWIND JFC '''

    ''' Print the heading 

    WRITE (JFC,84) '     Program: T31146, O P T R A F',DATE
    WRITE (JFC,85) 'Version ',IVERS,' : ',DVERS
    WRITE (JFC,86) 'Input data are stored on object ',(OBJ(I),I=1,6)
    WRITE (JFC,87) 'Cost file','Identification'
    WRITE (JFC,88) MNL,(IDENT(I),I=1,9)
    NPAGE(0) '''

    ''' Conversion of indata fields to independent variables
        with SI-system units as the dimensions

        Terminal data '''

    SITERM()

    ''' Winding data '''
    SIWIND()

    ''' Active part data
        ( EXTCOR get values within SIACTP) '''

    SIACTP()

    ''' Tank data '''

    SITANK()

    ''' General preliminary calculations '''

    PREPAR()
		
    ''' Checking of function codes and winding fractions '''

    CHFUNK()

    ''' BACKTRACKING '''
    if (C.ISTOP==1):return

    ''' Print the indata onto the output file depending on the environment '''

    NEWP=0

    ''' Print the indata onto the output file in TIME-SHARING mode '''

    ''' ****** HEAD1  Before PRPNL *********** '''
    '''PRPNL(NEWP,JFC,'T146WPNL ','P146-1  ')
    PRPNL(NEWP,JFC,'T146WPNL ','P146-2  ')
    NPAGE(0)
    PRPNL(NEWP,JFC,'T146WPNL ','P146-3  ')
    PRPNL(NEWP,JFC,'T146WPNL ','P146-4  ')
    if(BBOOS):
        NPAGE(0)
        PRPNL(NEWP,JFC,'T146WPNL ','P146-5  ')
    if(CORESE=='TA1 '):
          if(not BBOOS):NPAGE(0)
          PRPNL(NEWP,JFC,'T146WPNL ','P146-6  ') '''
    ''' ****** HEAD1  After  PRPNL *********** '''

    ''' Check of USERID-limitations '''

    CHECK()
    ''' BACKTRACKING '''
    
    if (C.ISTOP==1):return
	
 
    if((not C.BBHELP[10]) and C.BBERR):
        exit()

    ''' Calculation of the relative No. of turns '''

    TURNCA()

    ''' Calculation of currents '''

    CURDIM()

    VOLTAG()

    ''' Winding layout data '''

    PRESET()
    print('End of HEAD1 ')
    
    return
