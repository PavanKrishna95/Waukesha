''' Title: Calculation & printout of voltage cases & efficiency '''
from npage import NPAGE
import numpy
def PREFF():
    import com as C
    ETA=[0. for i in range(5)]
    DELTA=[0. for i in range(5)]
      
    ''' Start a new page '''

    NPAGE(13)
    ''' WRITE(C.JFC,80)
       WRITE(C.JFC,81) C.SRATE(2)/1.E+6
       WRITE(C.JFC,82) '''

    COSFI=0.75
    FACT=C.URC[0][0][0]*C.ZWOULI/C.SRATE[1]

    ''' Calculate DELTA for each of 5 power factors '''

    for I in range(1,6):
    
        COSFI=COSFI+0.05
        print(COSFI)
        Q=numpy.sqrt(1.-COSFI*COSFI)
        DELTA[I-1]=(COSFI*FACT+Q*C.UXC[0][0][0]+
                    (COSFI*C.UXC[0][0][0]-Q*FACT)**2/2.)*100.

    '''WRITE(C.JFC,83) (DELTA(I),I=1,5)
       WRITE(C.JFC,84) '''

    HELP1=1.
    COSFI=0.75

    ''' Calculate ETA for each of 4 situations '''

    for I in range(1,5):
        HELP2=HELP1-float(I-1)*0.25
        HELP=C.P00[0]+HELP2**2*C.URC[0][0][0]*C.ZWOULI

        ''' Calculate ETA for each of 5 power factors '''

        for J in range(1,6):
            J1=J
            ETA[J1-1]=  HELP/(C.SRATE[1]*HELP2*(COSFI+float(J1)*0.05)+HELP)
            ETA[J1-1]= (1.-ETA[J1-1])*100.

        ''' Print the result '''

        if (I <=1):
            ''' WRITE(C.JFC,85) HELP2,ETA(1),ETA(2),ETA(3),ETA(4),ETA(5) '''

        else:
            ''' WRITE(C.JFC,86) HELP2,ETA(1),ETA(2),ETA(3),ETA(4),ETA(5) '''

    return
'''
   80  FORMAT(1X/1X/1X,'     VOLTAGE DROP and EFFICIENCY')
   81  FORMAT(1X/1X,5X,'K*',F7.1,
     &       ' MVA  Terminal1-Terminal2, Principal tap')
   82  FORMAT(1X/1X,5X,'COS(Phi)',6X,'      0.80      0.85      0.90',
     &  '      0.95      1.00')
   83  FORMAT(6X,'K=1.00 Delta U(%)  ',5(F6.3,4X))
   84  FORMAT(1X)
   85  FORMAT(6X,'K=',F4.2,' Eta    (%)',T26,4(F6.3,4X),F6.3)
   86  FORMAT(6X,'K=',F4.2,T26,4(F6.3,4X),F6.3)
*
       END
'''
