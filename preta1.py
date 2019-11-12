
''' Title:  Prepar data for the TA1 core routines '''
from dntodk import DNTODK
from ncdta1 import NCDTA1
def PRETA1(DLIMB, HLIMB, CORBND, TOPOIL, BLIMB,FREKV, TASEC, NCOOLI):
    
    ''' Transfere data from input form '''

    TCORST  = C.LAMTH
    FHD     = C.TA1HOL
    ACCV    = C.ACCVER
    ACCL    = C.ACCLON
    ETA     = C.LAMSPF
    BSTEPI  = C.LAMSTP
    BPLMAI  = C.LAMMW
    OVRLPI  = C.LAMOVL
    TOPABS  = C.AMBTEM + TOPOIL
    TSTP    = (C.UARR[22] == 'YES' or C.UARR[22] == 'Y')

    ''' Estimate mass of winding block / limb '''

    MWB = 0.
    DOW = DLIMB
    for I in range(1,C.NWILI+1):
        if(C.RRWDG[I-1] > 0. ):
            RR = C.RRWDG[I-1]
        else:
            RR = 0.

        DIW = DOW + 2.*C.BDUCT[I-1]
        DWN = DIW + RR
        DOW = DWN + RR
        WCRA = RR*(HLIMB - C.DYOKE[I-1])
        WWGHT = WCRA*3.14159*DWN*C.FILLF[I-1]*8.9E3
        MWB = MWB + WWGHT

    ''' Estimate mass of one limb '''

    MLMB = DLIMB*DLIMB/4.*3.14159*HLIMB*0.87*7650.

    ''' Find net diameter '''

    CBBAND = CORBND[:5]
    if(CBBAND == 'ASEC'):
        KBAND = 1
    else:
        KBAND = 0

    DN = DLIMB - DNTODK(DLIMB, MLMB, C.ACCTRA, HLIMB, CBBAND, TASEC)

    ''' Cooling Ducts '''

    NCOOLW = NCDTA1(DN,TOPABS,BLIMB,FREKV,C.ISTGRD,TSTP,C.JFC)

    if(NCOOLI < 0):
        NK = NCOOLW
    else:
        NK = NCOOLI

    ''' Flitch plate '''

    IFLPMT  =  1
    if(C.FLPLMA == 'OX812'): IFLPMT = 2

    return (TCORST,DN, NK, FHD, IFLPMT,MWB, ACCL, ACCV,KBAND,
           ETA,BSTEPI,BPLMAI,OVRLPI,NCOOLW)
