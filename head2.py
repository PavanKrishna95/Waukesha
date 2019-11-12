
''' Title: Optimisation control routine '''
#from readch import READCH
from funk import FUNK
from lminca import LMINCA
from errrut import ERRRUT
from prep1 import PREP1
from wdglay import WDGLAY
from pnmass import PNMASS
#from cooleq import COOLEQ

from readch import READCH

from goto import with_goto
@with_goto
def HEAD2():

    import com as C
    TEXT=['Fundamental error','Max.No.of calc. reached',
          'Interrupt:  FUNK routine','Optimisation successful',
          'Optimum detected']

    RRWDG0=[0. for i in range(9)]
    FACTOR =1.E+3

    BBLAYD=True
    if(C.BBLAY):BBLAYD=False
    C.BBEND=False
    C.BBERR1=False
    C.BBFREQ=False
    if(abs(C.FREQ-50.) > 1.E-3 and abs(C.FREQ-60.)>1.E-3):
        C.BBFREQ=True
    C.XA[0]=C.DCORE
    C.XA[1]=C.HLIMB
    C.AVALUE=0.
    NTRIES=0

    ''' Quantities required for the optimisation subroutine '''

    NA=3+C.NWILI
    NB=15+3*(C.NWILI-1)

    ''' Reading the cost file required '''

    ''' *****HEAD2: Before READCH******* '''
    
    READCH(C.MNLY,C.MNL,C.RUBCH,C.CHCOST)

    ''' *****HEAD2: After  READCH Rubch: ',C.RUBCH '''
    ''' Backtracking '''
    
    if(C.ISTOP==1):return

    ''' Starting a new page on the output file '''

    ''' NPAGE(0) '''

    ''' Calculate the function '''

    ''' Optimise '''
    #VALUE=1.
    #NCYC=1
    #VALUE,ICONV,NF,NCYC=LMINCA(VALUE,NA,NB,NCYC)
    label ._400
    if(C.BBOPTI):
        C.BBEXAC=True

        ''' C.AVALUE scales VALUE to approximately 1 in FUNK via LMIN '''

        C.AVALUE=1.

        ''' Calculate the transformer '''
        
        a,C.XA,C.G,VALUE=FUNK(C.XA)
        
        if a ==1:
            goto ._299

        ''' Adjustment of certain quantities '''

        C.AVALUE=VALUE/1.2
        C.BBEXAC=False

        if ( not C.BBLAY):

            if(NTRIES<=1):
                VALUE,ICONV,NF,NCYC=LMINCA(VALUE,NA,NB,NCYC)
                if(ICONV<=0):C.BBERR1=True

                ''' Print an error warning, if any '''

                if(C.BBERR1 or C.BBFREQ):ERRRUT(C.BBERR1,C.BBFREQ,C.JFC)

        else:

            if( not BBLAYD):

                NTRIES=1+NTRIES

                PREP1()

                ''' BACKTRACKING '''
                if(C.ISTOP==1):return

                VALUE,ICONV,NF,NCYC=LMINCA(VALUE,NA,NB,NCYC)
                if(ICONV <= 0):C.BBERR1=True

                ''' Print an error warning, if any '''

                if(C.BBERR1 or C.BBFREQ):ERRRUT(C.BBERR1,C.BBFREQ,C.JFC)

                ''' Save the old winding widths and space factors '''

                for IWDG in range(1,C.NWILI+1):
                    RRWDG0[IWDG-1]=C.RRWDG[IWDG-1]

                ''' Automatic winding layout '''

                if( not C.BBERR1 and NTRIES <= 12):
                    #NPAGE(3)
                    ''' WRITE (C.JFC,100) 'Automatic winding layout' '''
                    WDGLAY()
                    ''' BACKTRACKING '''
                    if(C.ISTOP == 1):return

                ''' Check whether winding layout fits the transformer window 
                RRTOL = winding width tolerance between optimized and exact '''

                RRTOL=0.99
                for IWDG in range(1,C.NWILI+1):

                    DIFFRR=FACTOR*abs(C.RRWDG[IWDG-1]-RRWDG0[IWDG-1])

                    ''' BBLAYX(IWDG) = Layout of winding (IWDG) within tolerance '''

                    BBLAYX[IWDG-1]=True
                    if(DIFFRR > RRTOL):BBLAYX[IWDG-1]=False

                ''' BBLAYD       = Layout of all windings within tolerance '''

                BBLAYD=True
                for IWDG in range(1,C.NWILI+1):
                    if( not BBLAYX[IWDG-1] or not BBLAYD):BBLAYD=False

                ''' WRITE (*,127) (FACTOR*C.RRWDG(IWDG),IWDG=1,C.NWILI)
                    WRITE (*,128) (FACTOR*ABS(C.RRWDG(IWDG)-RRWDG0(IWDG)),IWDG=1,C.NWILI)
                    WRITE (*,*)
                    NPAGE(2)
                    WRITE (C.JFC,127) (FACTOR*C.RRWDG(IWDG),IWDG=1,C.NWILI)
                    WRITE (C.JFC,128) (FACTOR*ABS(C.RRWDG(IWDG)-RRWDG0(IWDG)),IWDG=1,C.NWILI) '''
                goto ._400

        ''' Print an error warning, if any '''

        if (C.BBERR1 or C.BBFREQ):ERRRUT(C.BBERR1,C.BBFREQ,C.JFC)

        ''' CALL NPAGE(2)'''
        ''' WRITE (C.JFC,91) TEXT(ICONV+3),NF,' calculations.','Optimisation accuracy',C.IOPT '''
        ''' WRITE (C.JFC,92) NCYC,' cycles.' '''

    ''' 'No optimisation requested.' '''

    label ._299
    C.BBEXAC=True
    C.AVALUE=1.

    ''' Function calculation '''

    a,C.XA,C.G,VALUE=FUNK(C.XA)
    C.BBEND=True
    C.BBREA=True

    ''' Function calculation '''
    
    a,C.XA,C.G,VALUE=FUNK(C.XA)
    if a==1:
        print('END of HEAD2')
        return

    ''' Cooling calculation for TAD. '''

    ''' if(C.TARR(82)=='YES    '):COOLEQ() '''

    if(C.MNLY > 91 ):
        PNMASS()
    
    print('END of HEAD2')
    
    return

'''    91  FORMAT('0','     ',A26,1X,I4,A14,2X,A21,I2)
       92  FORMAT(' ','     ',26X,1X,I4,A14)
       100  FORMAT (' ',/,' ',A,/)
       127  FORMAT(' Current  radial width',9(F8.2))
       128  FORMAT(' Diff. in radial width',9(F8.2)) '''


