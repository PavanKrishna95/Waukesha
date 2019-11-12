from head1 import HEAD1
from dimcur import DIMCUR
from precre import PRECRE
from prep1 import PREP1
from pretem import PRETEM
from pretan import PRETAN
from pkl79 import PKL79
from dimscc import DIMSCC
from head2 import HEAD2
from constr import CONSTR
from pageut import PAGEUT
from sampleprint import SAMPLEPRINT
from pysamp import pysamp
def SUB146(BBRES):
    import com as C
    C.IPAGE= 0
    ''' Read and analyse the indata '''
    print('********** SUB146 before HEAD1     *********')
    
    HEAD1()
    
    print('********** SUB146 after  HEAD1     *********')
    
    ''' BACKTRACKING '''
    if(C.ISTOP==1):return

    ''' Calculate the dimensioning winding currents and
        equivalent 2-winding rating '''
    print('********** SUB146 before DIMCUR    *********')
    DIMCUR()
    print('********** SUB146 before PRECRE    *********')

    ''' Preliminary core variables '''
    
    (C.BLTOPM,C.CHCORE,C.DCOMAX,C.DCOMIN,C.FEXTV,C.FNEXTV,C.KCORE,C.NCLA,C.ISTGRD,
     C.U0IN,C.YHADD,C.YHRED,C.BBERR)=PRECRE(C.AARR,C.BBSLIM,C.TARR,C.BBVFR,C.BMAXPU,
                                            C.NPHAS,C.NWOULI,C.UARR,C.UMAXPU,C.BBERR)

    ''' Determine the number of parameters '''
    print('********** SUB146 before PREP1     *********')
    PREP1()


    ''' Preliminary temperature variables '''

    print('********** SUB146 before PRETEM    *********')
    C.DTSNN,C.DTSNF,C.DTSFF=PRETEM(C.AARR)

    ''' Preliminary tank variables '''

    print('********** SUB146 before PRETAN    *********')
    C.F1TANK,C.F2TANK,C.F3TANK,C.KTAN79=PRETAN(C.KTANK)

    print('********** SUB146 before PKL79     *********')
    PKL79()

    ''' Determine the dimensioning short-circuit case '''

    print('********** SUB146 before DIMSCC    *********')
    C.BBSCI,C.BBSCJ,C.BBSCK,C.BBSCL=DIMSCC(C.BBVR,C.NG,C.SLINE)

    ''' BACKTRACKING '''
    if(C.ISTOP==1):return

    ''' Optimisation '''
    
    
    print('********** SUB146 before HEAD2     *********')
    HEAD2()

    ''' BACKTRACKING '''
    if(C.ISTOP==1):return

    ''' Check which limits, if any, have been exceeded '''
    print('********** SUB146 before CONSTR    *********')
    CONSTR()

    ''' Print results on file C.JFC, also list on file 06 '''

    print('********** SUB146 before PAGEUT    *********')
    PAGEUT(BBRES)
