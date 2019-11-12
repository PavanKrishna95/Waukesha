
''' Title:  Convert tank data from indata fields to SI-units
            and transfer them to internal variables '''

def SITANK():
    import com as C
    C.KTANK=C.IARR[52]

    ''' Illegal tank type '''

    if(C.KTANK < 0 or C.KTANK >= 40) :
        C.JFC,C.BBERR=FPRINT(2,C.BBERR,
                    'SITANK:ILLEGAL TANK TYPE')
        
        ''' Backtracking '''
        if(C.ISTOP == 1):return

    C.DWITA=C.AARR[150]/1.E+3
    EXTTA=C.AARR[151]/1.E+3
    C.DCOCOV=C.AARR[152]/1.E+3

    XTANK=0.5
    if (C.KTANK == 2):XTANK=0.4
    if (C.KTANK == 4 or C.KTANK == 5): XTANK=0.45

    if (C.BBSLIM): C.EXTANK=EXTTA+XTANK
    if ( not C.BBSLIM): C.EXTANK=EXTTA+2.*C.DWITA

    OPTTNK=C.UARR[19]

    ''' When the tank dimensions have been fixed ( OPTTNK = 'NO' )
        then the additional tank-distances are assumed to be the actual
        tank-dimensions. '''

    ''' If fixed tank dimensions '''

    if (OPTTNK[0] == 'N') :
        C.HTANK=C.DCOCOV
        C.BTANK=C.DWITA
        C.RLTANK=EXTTA

    C.HTANKM=C.AARR[173]/1.E+3
    C.BTANKM=C.AARR[174]/1.E+3
    C.RLTNKM=C.AARR[175]/1.E+3

    return
