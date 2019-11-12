
''' Title:  Performs preliminary calculations
            and sets complementary variables needed
            during the subsequent calculations. '''

def PREPAR():
    import com as C
    ''' Steering variables for the optimisation routine LMIN '''

    ''' Start of the steering block. '''

    C.AF=C.BARR[34]
    C.DRV=C.BARR[33]
    C.EPS=C.BARR[31]
    C.FEPS=C.BARR[32]
    C.NFMX=C.IARR[2]
    if(C.IARR[49] > 0): C.ITR=C.IARR[49]

    ''' End of the steering block. '''

    ''' Allocation of values to C.BBHELP
        Setting to zero via DATA statement in MAIN1 '''

    ''' Start of the allocation block. '''

    IND1=C.IARR[51]
    if(IND1 >= 0 and IND1 <= 10): C.BBHELP[IND1]=True

    OMEGA=2.*C.PI*C.FREQ
    C.BBSCR[2]=False

    ''' End of the allocation block. '''

    ''' Calculation of equivalent power rating for each terminal '''

    for I in range(1,C.NG+1):
        CCON=1.
        if(C.KCON[I-1] == 1 or C.KCON[I-1] == 11): CCON=C.SQR3
    
        C.UDIM[I-1]=C.UNLINE[I-1]/CCON

        ''' Equivalent values for one limb '''

        C.SRATEP[I-1]=C.SRATE[I-1]/C.ZWOULI
        if(I <= 3)  :
            C.BBSCR[I-1]=False
            if (abs(C.SLINE[I-1]) > 0.): C.BBSCR[I-1]=True
    
    ''' Calculation of C.EDDCO1 for each winding '''

    for I in range(1,C.NWILI+1):

        ''' C.EDDCO1 = Auxiliary variable for calculation of additional losses '''
        C.EDDCO1[I-1]=OMEGA*OMEGA*C.RMY0*C.RMY0/(36.*C.RAACON[I-1]/C.SIGM[I-1])
  
    NWLPPH=C.NWOULI/C.NPHAS
    C.SNOML=C.SRATEP[0]

    ''' Impedance (pu) in the network is calculated from short-cct power. '''

    for I in range(1,C.NG+1):
        C.EXTX[I-1]=1000.
        if (C.SLINE[I-1] > 0.): C.EXTX[I-1]=3.*C.SNOML/C.SLINE[I-1]*float(NWLPPH)
        if (C.SLINE[I-1] < 0.): C.EXTX[I-1]=0.

    ''' Determination of constants for "Other eddy losses" '''

    ''' Start of the "Other eddy losses" block '''

    if (C.BBDSHE)  :
        C.BPOED=1.5E-4
    else:
        C.BPOED=2.5E-4

    if (C.BBWISU)  :
        if (C.BBFLDS)  :
            C.APOED=1.6E+5
        else:
            C.APOED=2.0E+5
    else:
        if (C.BBFLDS)  : 
            C.APOED=2.8E+5
        else:
            C.APOED=3.5E+5

    ''' End of the "Other eddy losses" block '''

    ''' Setting to zero of certain variables '''

    ''' Start of the "setting to zero" block '''

    C.DOUTW=0.
    C.GACTP=0.

    ''' End of the "setting to zero" block '''

    return
