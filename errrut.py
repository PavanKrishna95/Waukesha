
''' Title:  Prints warnings when the optimisation goes wrong '''

def ERRRUT(BBERR1,BBFREQ,JFC):

    ''' Print the appropriate error message if necessary. '''

    ''' SBBL Start of the Printing block. '''

    ''' WRITE(JFC,600)
    IF(BBERR1) WRITE(JFC,610)
    IF(BBFREQ) WRITE(JFC,620)
    WRITE(JFC,630) '''

    ''' SEBL End of the Printing block. '''


    ''' 600   FORMAT(1X,'**************'/1X,'***')
         610   FORMAT(1X,'***  WARNING: Optimization not complete.')
         620   FORMAT(1X,'***  WARNING: Unreliable calculation of P0 because'/
         &        1X,'***           frequency not equal to 50 or 60 Hz')
         630   FORMAT(1X,'***'/1X,'**************') '''
    return
