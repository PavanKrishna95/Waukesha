
''' Title:  Examine indata for additional information '''
from typwdg import TYPWDG
import numpy
def PRESET():
    import com as C

    ''' Convert the winding types for the winding layout routines '''

    TYPWDG()

    ''' Set various winding parameters '''

    for IWDG in range(1,C.NWILI+1):
        C.ZDISC[IWDG-1] =0.
        C.ZTUDI[IWDG-1] =0.
        C.ZTULO[IWDG-1] =0.
        C.ZPART[IWDG-1] =1.
        C.ZCOIAR[IWDG-1] =1.
        C.ZAR[IWDG-1] =1.
        C.ZRR[IWDG-1] =1.
        C.ZNLAG[IWDG-1] =0.
        C.ZLAG[IWDG-1] =1.

        MKWIND=C.KWIND[IWDG-1]

        if (MKWIND >= 11 and MKWIND <= 19 and C.KCODE[IWDG-1]  == 2): MKWIND=7
        if (MKWIND >= 20 and MKWIND <= 39 and C.KCODE[IWDG-1]  == 2): MKWIND=10

        ''' Maximum strand dimensions '''

        if (C.TARR[40+IWDG-1][0] == 'C') :
            C.HPRTMX[IWDG-1] =0.015
            C.BPRTMX[IWDG-1] =0.003
            C.HPRTMN[IWDG-1] =0.008
            C.BPRTMN[IWDG-1] =0.0011
        else:
            C.HPRTMX[IWDG-1] =0.016
            C.BPRTMX[IWDG-1] =0.0035
            C.HPRTMN[IWDG-1] =0.009
            C.BPRTMN[IWDG-1] =0.0013

        ''' Convert insulation thicknesses to compacted values '''

        if (MKWIND <= 10 or MKWIND >= 40) :
            C.TSPIN[IWDG-1] =C.TSPIN[IWDG-1] *0.95
            C.HCLAC[IWDG-1] =C.HCLAC[IWDG-1] *0.95

        ''' Number of strands in axial and radial directions '''

        if (MKWIND >= 11 and MKWIND <= 29) :
            C.ZAR[IWDG-1] =round(MKWIND/10.)
            C.ZRR[IWDG-1] =numpy.mod(round(float(MKWIND)),10.)
        elif (MKWIND >= 2 and MKWIND <= 6) :
            C.ZAR[IWDG-1] =float(MKWIND)
        else:
            C.ZAR[IWDG-1] =1.

        if (MKWIND == 12 or MKWIND == 22): C.ZRR[IWDG-1] =2.

        ''' Number of loops in the radial direction '''

        C.NLORR[IWDG-1] =1
        if (MKWIND >= 7 and MKWIND <= 9):     C.NLORR[IWDG-1] =1
        if (MKWIND == 10):                    C.NLORR[IWDG-1] =2
        if (MKWIND >= 11 and MKWIND <= 39):   C.NLORR[IWDG-1] =1
        if (MKWIND == 8):                     C.NLOOP[IWDG-1] =C.NLOOP[IWDG-1] /2
        if (MKWIND == 9):                     C.NLOOP[IWDG-1] =C.NLOOP[IWDG-1] /3
        if (MKWIND >= 7 and MKWIND != 100 and C.BBRR[IWDG-1] ): C.ZPART[IWDG-1] =1.
        if (MKWIND != 0 or MKWIND != 100  or  not C.BBRR[IWDG-1] ):
            pass

            ''' Adjust the initial values of strand dimensions for disc windings '''

        else:
            while(C.HPART[IWDG-1] *C.BPART[IWDG-1] > C.ACOND[IWDG-1] ):
                C.HPART[IWDG-1] =C.HPART[IWDG-1] *0.95
                C.BPART[IWDG-1] =C.BPART[IWDG-1] *0.95
    
        if ( not C.BBRR[IWDG-1] ) :

            C.ZPART[IWDG-1] =C.ZRR[IWDG-1] *C.ZAR[IWDG-1] 
            if (C.KWIND[IWDG-1]  <= 0 or C.KWIND[IWDG-1]  == 100) :

                '''Calculate the number of discs and number of turns per disc if 
                    the winding dimensions are fixed '''

                C.ZDISC[IWDG-1] =(C.HLIMB-C.DYOKE[IWDG-1] -C.EXTRAR[IWDG-1] +
                                  C.HCLAC[IWDG-1] )/(C.HPART[IWDG-1] +
                                C.TSPIN[IWDG-1] +C.HCLAC[IWDG-1] )
                C.ZDISC[IWDG-1] =2.*round(C.ZDISC[IWDG-1] /2.)
                C.ZTUDI[IWDG-1] =C.ZWIND[IWDG-1] *float(C.NGROUP[IWDG-1] )/C.ZDISC[IWDG-1] 
                C.ZTUDI[IWDG-1] =round(C.ZTUDI[IWDG-1] *2.+1.0)/2.

    return
