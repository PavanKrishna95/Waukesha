
''' Title:   Calculate masses of presspahn in the active part '''

def PNMASS():
    import com as C
    ''' C.PNFDUC = Fraction of main duct volume which contains presspahn
        C.PNFWIN = Fraction of winding volume, excluding copper volume
                   which contains presspahn.
        C.PNFYOK = Fraction of yoke insulation volume
                   which contains presspahn.
        C.PNDUCT = Mass of presspahn in main ducts  (kg).
        C.PNWIND = Mass of presspahn in windings (kg).
        C.PNYOKE = Mass of presspahn in yoke insulation  (kg).
        Output masses cover all wound limbs and all windings. '''

    ''' Pressphan density (kg/m3) '''

    RAAPN = 1220.
    ZWOULI= float(C.NWOULI)

    C.PNDUCT = 0.
    C.PNWIND = 0.
    C.PNYOKE = 0.

    for IW in range(1,C.NWILI+1):

        ''' DUCT................. '''

        ''' Segment width '''

        WD = C.BDUCT[IW-1]

        ''' Segment mean diameter '''

        DD = C.DWIND[IW-1] - C.RRWDG[IW-1] - WD

        ''' Segment height '''

        HD = C.HLIMB - C.DYOKE[IW-1]

        ''' Presspahn mass '''

        C.PNDUCT = C.PNDUCT + C.PNFDUC*WD*DD*C.PI*HD*RAAPN*ZWOULI

        ''' WINDINGS................ '''

        ''' Segment width '''

        WD = C.RRWDG[IW-1]

        ''' Segment mean diameter '''

        DD = C.DWIND[IW-1]

        ''' Segment height '''

        HD = C.HLIMB - C.DYOKE[IW-1]

        ''' Presspahn mass '''

        C.PNWIND=C.PNWIND+C.PNFWIN*WD*DD*C.PI*HD*RAAPN*(1.-C.FILLF[IW-1])*ZWOULI

        ''' YOKE ................... '''

        ''' Segment width '''

        WD = C.RRWDG[IW-1] + C.BDUCT[IW-1]

        ''' Segment mean diameter '''

        DD = C.DWIND[IW-1] - C.BDUCT[IW-1]

        ''' Segment height '''

        HD = C.DYOKE[IW-1]

        ''' Presspahn mass '''

        C.PNYOKE = C.PNYOKE + C.PNFYOK*WD*DD*C.PI*HD*RAAPN * ZWOULI

    return
