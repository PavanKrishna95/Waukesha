
''' Title:  Calculation of cooling ducts in transformer cores '''
from cdtad import CDTAD
from cdtba import CDTBA
from nkyltc import NKYLTC

def NCOOL(CORESE,TYP,DK1,TOPOIL,B,FREKV,BBZDKH,BBSTLA,BBPLJT):

    ''' CORESE  Coreseries (TAA, TAC, TAD, TBA, TCA, SL-C)
        TYP     CORETYP (D, T, EY, ...) AS A REAL NUMBER .
        DK1     Corediameter  (m)
        TOPOIL  Top oil temperature
        B       max flux density (T)
        FREKV   frequency  (HZ)
        BBZDKH  ZDKH core plate (.T.  OR .N.)
        BBPLJT  PLJT core plate (.T.  OR .N.)
        BBSTLA  step-lap core   (.T.  OR .N.) '''


    ''' write(*,*) '***ncool entry' '''
    
    DK = DK1 * 1000.

    ''' TAA, TAD, TAC '''

    ''' write(*,*) '***ncool CORESE', CORESE '''
    
    if(CORESE == 'TAA' or CORESE == 'TAC' or
       CORESE == 'TAD'):

        ''' write(*,*) '***ncool calling cdtad' '''
        NCOOL=CDTAD(DK,TOPOIL,B,FREKV,BBZDKH,BBSTLA,BBPLJT)

        ''' TBA '''

    elif(CORESE == 'TBA'):

        '''write(*,*) '***ncool calling cdtba' '''
        NCOOL=CDTBA(DK,TOPOIL,B,FREKV,BBZDKH,BBSTLA,BBPLJT)

        ''' TCA '''

    elif(CORESE == 'TCA'):

        '''write(*,*) '***ncool calling nkyltc' '''
        NCOOL=NKYLTC(TYP,DK1,TOPOIL,B,FREKV)

        ''' YTTERBENSK#RNOR (LTB-K#RNAN) '''

    else:
        ''' write(*,*) '***ncool typ dk ', typ, dk '''
        NCOOL=0
        if(TYP != 10.):
            if(DK >= 800.): NCOOL=1
            if(DK >= 1025.):NCOOL=2
            if(DK >= 1145.):NCOOL=3
            if(DK >= 1325.):NCOOL=4

        else:
            if(DK >= 720.): NCOOL=1
            if(DK >= 800.): NCOOL=2
            if(DK >= 860.): NCOOL=3
            if(DK >= 960.): NCOOL=4
            if(DK >= 1025.):NCOOL=5
            if(DK >= 1125.):NCOOL=6
            if(DK >= 1225.):NCOOL=7
            if(DK >= 1325.):NCOOL=8
            if(DK >= 1365.):NCOOL=9

    ''' write(*,*) '***ncool exit ' '''

    return NCOOL
