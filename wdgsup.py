
''' Title:  Calculates the dimensions of the winding supports '''

def WDGSUP(RK,RIADON,DYL1,DCOR,H01,H11,H21,
           B,TWSUPC,BBSLIM):

    ''' Start '''

    HWSUPC= (TWSUPC-6)/1000.
    H= H01/1000.
    H1= H11/1000.
    H2= H21/1000.
    DYL =DYL1/1000.
    DCORI= DCOR/1000.
    RR= DYL-DCORI
    FI1= RIADON*1.E-6
    FI2= B*0.25*(PI/4.*(DYL+DCORI)*RR-DCORI*RR)
    KTEST= 0
    IHELP= 0

    ''' Height of the Winding Support '''

    if(TWSUPC == 40 or TWSUPC == 60 or TWSUPC == 80):

        ''' Height of the Winding Support GIVEN
            Width of the Winding Support '''

        BSUP= (FI1+FI2)/(0.42*RR*HWSUPC)
        HMARG= 1.5/BSUP
        if(BSUP > 1.5):

            ''' Calculate a new height & width '''

            HWSUPC= 1.6/RR*(FI1+FI2)
            TWSUPC= int(HWSUPC*1000.)
            if(HWSUPC < 0.074): TWSUPC= 80
            if(HWSUPC < 0.054): TWSUPC= 60
            if(HWSUPC < 0.034): TWSUPC= 40
            HMARG= (TWSUPC-6)/HWSUPC/1000.
            HWSUPC= (TWSUPC-6)/1000.


        ''' Calculate the Height of the Winding Support '''
    else:
    
        HWSUPC= 1.6/RR*(FI1+FI2)
        TWSUPC= int(HWSUPC*1000.)
        if(HWSUPC < 0.074): TWSUPC= 80
        if(HWSUPC < 0.054): TWSUPC= 60
        if(HWSUPC < 0.034): TWSUPC= 40
        HMARG= (TWSUPC-6)/HWSUPC/1000.
        HWSUPC= (TWSUPC-6)/1000.
    
    AREA= (H1+H2)/2.*(RK*HWSUPC-.015)
    FACT= H+RK*HWSUPC-.015
    FI4= B*0.5*RR*FACT

    ''' Outer limb? '''

    if(BBSLIM):
        
        ''' Yes '''

        BTEST= (FI2+FI4)/AREA

        ''' Connection Plate '''

    else:
        FI3= B*0.5*RR*(FACT+HWSUPC)
        TANSL= 0.67*(FI1+FI2+FI3)/FACT
        TANSL1= TANSL*1000.
        TANSL1= int(TANSL1/10.)*10.+10.
        if (TANSL1 < 120.):  TANSL1=120.
        if (TANSL1 > 300.):  IHELP= 1
        TMARG= TANSL1/TANSL/1000.
        BTEST= 2.*(FI2+FI4)/AREA

    ''' B in Yoke <=1.5 ? '''

    if(BTEST > 1.5 or IHELP == 1):

        ''' New RK '''

        KTEST= 1

        ''' B is OK '''

    else:
        BMARG= 1.5/BTEST
        WMARG= (min(HMARG,BMARG)-1.)*100.
        TMARG= (TMARG-1.)*100.

    return KTEST,TWSUPC,TANSL1,WMARG,TMARG
