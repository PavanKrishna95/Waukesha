
''' Title:  Calculation of the total relative No. of turns
           for each winding = C.ZWINDW( > 0.)
           Also C.POSIT is modified for main windings with
           extra tappings ( Type 4 ) '''

def CURDIM():
    import com as C
    ''' Calculate No. of turns per winding '''

    for IWDG in range(1,C.NWILI+1):

        ''' For each winding type '''

        ''' Main winding with no variation of turns '''

        if (C.KCODE[IWDG-1] == 1):
            C.ZWINDW[IWDG-1]=abs(C.ZTALMW[IWDG-1]*C.FRACT[IWDG-1])

            ''' Regulating winding '''

        elif (C.KCODE[IWDG-1]==2 or C.KCODE[IWDG-1] == 3):
            C.ZWINDW[IWDG-1]=abs(C.ZTALRW[IWDG-1])

            ''' Tapped windings
                The next statements will convert "POSITION" to be valid for
                the whole winding No. "I" instead of only for the tapping part '''

        elif (C.KCODE[IWDG-1]==4):
            X1=C.ZTALMW[IWDG-1]*C.FRACT[IWDG-1]
            X2=C.ZTALRW[IWDG-1]
           
            C.POSIT[IWDG-1][0]=(X1+C.FRZPOS[IWDG-1]*X2)/(X1+X2)
            C.POSIT[IWDG-1][1]=(X1+C.FRPPOS[IWDG-1]*X2)/(X1+X2)
            C.POSIT[IWDG-1][2]=(X1+C.FRMPOS[IWDG-1]*X2)/(X1+X2)
            C.POSIT[IWDG-1][3]=(X1+C.FRXPOS[IWDG-1]*X2)/(X1+X2)
            C.ZWINDW[IWDG-1]=abs(X1+X2)

    return
