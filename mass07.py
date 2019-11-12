def MASS07(BBPRNT,JFC,NCLA,NWILI,NG,VTANK,RLTANK,BTANK,
           HTANK,BB132,RAACON,VACTP,GVVAH,GOFWF):
    import common as CM
#OIL ABSORBED , VOLUME OF ACTIVE PART, FINAL ASSEMBLY DETAILS,
#      SOUND SCREENS, HEAT EXCHANGERS.
#      #########################################################
#
#      BBPRNT     PRINTOUT OF INPUT/OUTPUT DATA IF TRUE
#      JFC        FILECODE FOR PRINTOUT
#      NCLA =     CORE CLAMP CODE
#                 1 = WOOD          CORE CLAMPS
#                 2 = STEEL PROFILE CORE CLAMPS
#                 3 = STEEL PLATE   CORE CLAMPS
#
#      NWILI =    NUMBER OF WINDINGS PER LIMB
#      NG =       NUMBER OF TERMINALS ON THE TRANSFORMER
#      VTANK =    VOLUME OF TRANSFORMER TANK                (DM3)
#      RLTANK =   TANK LENGTH              (MM)
#      BTANK =    TANK WIDTH               (MM)
#      HTANK =    TANK HEIGHT              (MM)
#      BB132 =    LOGICAL VARIABLE = TRUE IF SOUND SCREENS
#                 SHALL BE INCLUDED.
#      RAACON =   DENSITY OF WINDING CONDUCTORS       (KG/DM3)
#      VACTP =    OUTPUT DATA : VOLUME OF ACTIVE PART (DM3)
#      GVVAH =    MASS OF HEAT EXCHANGERS OFAF  (ESTIMATED)
#      GOFWF =    MASS OF HEAT EXCHANGERS OFWF  (ESTIMATED)
#
    print('VACTP',VACTP)
    if(BBPRNT):
        #PMASS7(BBPRNT,JFC,NCLA,NWILI,NG,VTANK,RLTANK,BTANK,\
    #HTANK,BB132,RAACON,VACTP,GVVAH,GOFWF)
        pass
    ####   NET MASS OF OIL ABSORBED
#
#      AUXILIARY VARIABLE FOR CORE CLAMPS

    RK10= 0.09*(CM.GSN241+CM.GSN242)
    if(NCLA>=2): RK10=0.021 *(CM.GSN241+CM.GSN242)**0.825
    
    #OIL IN THE WINDINGS:
    SHELP1=0
    for I in range(1,1+NWILI):
        SHELP1=SHELP1 + 0.15*(CM.GSN131[I-1]+CM.GSN132[I-1]+CM.GSN133[I-1]+
                              CM.GSN134[I-1]+CM.GN1351[I-1]+CM.GN1352[I-1] ) +0.33*(
                                  CM.GSN121[I-1]+CM.GSN122[I-1])  + 0.3*CM.GSN41[I-1]
    #OIL IN CLEATS AND LEADS
    SHELP2=0
    for I in range(1,1+NG):
        SHELP2=SHELP2 + 0.1*CM.GSN31[I-1] + 0.3*CM.GSN32[I-1]

    CM.GSN141 = (SHELP1 + SHELP2 +0.15*CM.GSN46 +
                 0.3*(CM.GSN42+CM.GSN45+CM.GSN212+RK10) +0.02*VTANK)    

    #VOLUME OF ACTIVE PART
    SHELP1=0
    for I in range(1,1+NWILI):
        SHELP1=(SHELP1 + 0.9*(CM.GSN121[I-1]+CM.GSN122[I-1]) +0.95*CM.GSN41[I-1] +
                0.8*(CM.GSN131[I-1]+CM.GSN132[I-1]+CM.GSN133[I-1]+
                     CM.GSN134[I-1]+CM.GN1351[I-1]+CM.GN1352[I-1]+CM.GSN136[I-1]) +\
                CM.GSN11[I-1]/RAACON[I-1])

    SHELP2=0
    for I in range(1,1+NG):
        SHELP2=SHELP2+ 0.9*CM.GSN32[I-1] + 0.2*CM.GSN31[I-1]
    VACTP = (SHELP1 + SHELP2 +0.15*CM.GSN211 +
             0.95*(CM.GSN212+CM.GSN42+CM.GSN45)  +
             1.04*CM.GSN25 + 0.2*CM.GG49 + 0.7*CM.GSN46 + 0.35*CM.GSN53 +
             0.13*(CM.GSN241 +CM.GSN242 +CM.GSN47) )   
     #DETAILS, FINAL ASSEMBLY
#*
#****   NORMAL FINAL ASSEMBLY DETAILS         
    
    CM.GN1210= 0
    CM.GG1210= 0.15 *(CM.GSN241+CM.GSN242)**0.75
    CM.GSN142=0
    print('vactp',VACTP)
    if(VTANK > 0):
        CM.GSN142 = 0.96 *(0.98*VTANK -VACTP)

    #SOUND SCREENS
    CM.GSN112  = 0
    if(BB132):  CM.GSN112 =30.E-6 *(RLTANK+BTANK+1300)*(HTANK-200)
    CM.GSN111  = 3.5 *CM.GSN112
    CM.GG111   = 0.05 *(CM.GSN111 + CM.GSN112)

    #HEAT EXCHANGERS
    CM.GG151=GVVAH
    CM.GG152=GOFWF

    return VACTP
