
''' Title:  Output of the no-load characteristics. '''
from npage import NPAGE
from nloadn import NLOADN
def PRNLD(BBRES):

    import com as C
    QNOLO=[0. for i in range(5)]
    JCOUNT =[ 1, 2, 4, 5, 3 ]

    ''' Print a new page heading '''

    NPAGE(0)

    ''' WRITE (C.JFC,10) '     NO-LOAD CONDITIONS  (Principal tap)' '''

    BBRESC=False
    BBRES= False
    BLIMB9=C.BLIMB

    ''' Calculate no-load losses for 5 flux densities '''

    for JLEVEL in range(1,6):
        ILEVEL=JCOUNT[JLEVEL-1]
        C.BLIMB=BLIMB9*(0.85+0.05*float(ILEVEL))

        ''' BBRESC= True because the resonance calculation is needed only
                    after the last loop (See FUNK) '''

        if(JLEVEL == 5): BBRESC=True

        ''' Calculate no-load losses '''

        NLOADN(BBRESC)

        C.PNOLO[ILEVEL-1]=C.P00[0]
        QNOLO[ILEVEL-1]=C.Q00[0]
        C.SOUND[ILEVEL-1]=C.SOUND0[0]
        C.RINOLO[ILEVEL-1]=C.Q00[0]/C.SRATE[0]

        C.BLIMB=BLIMB9
    return
