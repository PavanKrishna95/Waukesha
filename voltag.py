
''' Title:  Assign dimensioning voltages to the
            array "C.UN", with the parameters
            "I" and "J", "C.UN(I,J).
            where "I" is the actual voltage group
            and "J" is the actual voltage regulation
            Position "J" = 1 ==> Nominal position
                     "J" = 2 ==> Extreme PLUS position
                     "J" = 3 ==> Extreme MINUS position
                     "J" = 4 ==> Extra (arbitrary) position

    Relative flux densities( C.BMAXPU, C.BMINPU) are also calculated '''

def VOLTAG():
    import com as C

    ''' Initialisation of certain variables '''

    ''' For each terminal '''
    ''' for ITML=1,4 '''
    UTURN=[0. for i in range(4)]
    TM=[0. for i in range(4)]

    '''In each Terminal For each tap '''
    ''' JTAP=1,4 '''
    
    TR=[[0. for i in range(4)] for i in range(4)]
    ''' For each winding '''

    for IWDG in range(1,C.NWILI+1):

        ''' Summation of relative turns for the different terminals for
            the different tap-positions '''

        ''' Start of the summation block. '''

        KTML=C.KGROUP[IWDG-1]
        TR[KTML-1][0]+=C.ZTALRW[IWDG-1]*C.FRZPOS[IWDG-1]
        TR[KTML-1][1]+=C.ZTALRW[IWDG-1]*C.FRPPOS[IWDG-1]
        TR[KTML-1][2]+=C.ZTALRW[IWDG-1]*C.FRMPOS[IWDG-1]
        TR[KTML-1][3]+=C.ZTALRW[IWDG-1]*C.FRXPOS[IWDG-1]
        print('ZTALRW=',C.ZTALRW)
        
        if(C.ZTALMW[IWDG-1]>0.): TM[KTML-1]=C.ZTALMW[IWDG-1]

        ''' End of the summation block. '''

    ''' Calculation of normalised turn voltage "UTURN" for the different
            tap positions and relative flux densities '''
    print('TM=======',TM)
    print('TR=======',TR)
    JS=1
    if(C.BBVFR): JS=4

    ''' Calculate UTURN for each tap '''

    for JTAP in range(1,JS+1):

        X=TM[0]+TR[0][JTAP-1]
        if(C.BBAUTO and not C.BBUPTR):  X=X+TM[1]
        if(C.BBAUTO and not C.BBUPTR and C.BBVFR):  X=X+TR[1][JTAP-1]
        UTURN[JTAP-1]=C.UDIM[0]/X

    ''' Calculation of relative flux density at
        Extreme PLUS & MINUS positions '''

    ''' Calculate max & min B '''

    ''' VFR '''

    if(C.BBVFR):
        
        ''' Calculate max & min B '''
        
        ''' If UTURN[1] > UTURN[0] '''

        if (UTURN[1]>=UTURN[0]):
            C.BMAXPU=UTURN[1]/UTURN[0]
            C.BMINPU=UTURN[2]/UTURN[0]

            ''' If UTURN[1] <= UTURN[0] '''

        else:
            C.BMAXPU=UTURN[2]/UTURN[0]
            C.BMINPU=UTURN[1]/UTURN[0]

        ''' CFR '''
    else:
        UTURN[3]=UTURN[0]
        UTURN[2]=UTURN[0]
        UTURN[1]=UTURN[0]
        C.BMAXPU=1.
        C.BMINPU=1.

    ''' Calculate C.UN '''

    ''' Start of the C.UN block '''

    ''' For each tap '''
  
    for JTAP in range(1,5):

        ''' For each terminal '''

        for ITML in range(1,C.NG+1):
            C.UN[ITML-1][JTAP-1]=(TM[ITML-1]+TR[ITML-1][JTAP-1])*UTURN[JTAP-1]
       
        if(C.BBAUTO):
            C.UN[C.NSG-1][JTAP-1]=C.UN[C.NSG-1][JTAP-1]+TM[C.NPG-1]*UTURN[JTAP-1]
        if(C.BBAUTO and C.BBVFR):
            C.UN[C.NSG-1][JTAP-1]=C.UN[C.NSG-1][JTAP-1]+TR[C.NPG-1][JTAP-1]*UTURN[JTAP-1]

    ''' End of the C.UN block '''
        
    return
