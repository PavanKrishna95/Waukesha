#TANK MASS
#      ###########
#
#      BBPRNT   = PRINTOUT OF INPUT/OUTPUT DATA IF TRUE
#      JFC      = FILECODE FOR PRINTOUT
#      HTANK    = TANKHEIGHT  (M)
#      BTANK    = TANKWIDTH   (M)
#      RLTANK   = TANKLENGTH  (M)
#
#      VVAH     = NUMBER OF HEAT EXCHANGERS (VVAH)
#      RRAD     = NUMBER OF RADIATORS
#      VTANK    = TANKVOLUME (M3)
#      ASHELL   = AREA OF TANK WALLS (M2)
#      ACOVER   = COVER AREA (M2)
#      KTAN79   = CODE FOR TANK TYPE
#                 1 = OVAL TANK
#                 2 = RECTANGULAR TANK
#                 3 = TAA - VACUUM-PROOF
#                 4 = TAA - NOT VACUUM-PROOF
#                 5 = TBA
#                 6 = CURVED TANK  AND OTHER TYPES
#
#      TANKDI   = OUTPUT DATA FOR COST CALCULATION
#      GTANK    = MASS OF THE TANK (KG)
#      BBLT10   = LOGICAL VARIABLE = TRUE IF GTANK IS LESS THAN 10000.
#                 BBLT10 MUST BE SAVED IN THE MAIN LINK
#      BBEXAC   = LOGICAL VARIABLE = TRUE   DURING EXACT CALCULATIONS
#                                    AND  FALSE    DURING OPTIMIZING .

from ptnk79 import PTNK79
def TANK79(BBPRNT,JFC,HTANK,BTANK,RLTANK,VVAH,RRAD,VTANK,
           ASHELL,ACOVER,KTAN79,TANKDI,GTANK,BBLT10,BBEXAC):
    import common as CM

    if(BBPRNT):
        PTNK79(BBPRNT,JFC,HTANK,BTANK,RLTANK,VVAH,RRAD,VTANK,
               ASHELL,ACOVER,KTAN79,TANKDI,GTANK,BBLT10,BBEXAC)

    if(KTAN79>2): BBLT10=False

    if(KTAN79==1):
        RM    =  200 * HTANK*(BTANK+RLTANK)
        GTANK =  4.11 * RM** 0.914
        TANKDI=  VTANK
        if(BBEXAC):  BBLT10= (GTANK < 1.E4)
        if(BBLT10):  TANKDI = RM*1.E-2
        if(BBLT10):  GTANK  = 1.67*(HTANK*BTANK*RLTANK*1.E3) **0.816

    elif(KTAN79==2):
        RM = 2.E2*HTANK*(BTANK+RLTANK)
        GTANK= 1.462E-4* RM** 2.054
        if(BBEXAC):  BBLT10 = (GTANK < 1.E4)
        TANKDI =  2*(BTANK+RLTANK)
        if(BBLT10): GTANK= 3.41* RM**0.907

    elif(KTAN79==3):
        if(BBEXAC):
            CM.XTANKS = 0.05
            if(ASHELL > 14.): CM.XTANKS= 0.06
            if(ASHELL > 18.): CM.XTANKS= 0.07
            CM.YTANKS = 0.10
            if(ASHELL > 20.): CM.YTANKS= 0.12
            CM.ZTANKS  = 0.12
            if(VTANK >6.4):  CM.ZTANKS = 0.16
            if(VTANK >12.5): CM.ZTANKS = 0.20

        GTANK = 8.E+2*(ASHELL*(0.9*CM.XTANKS+0.45*CM.YTANKS ) +
                       ACOVER*(1.42*CM.ZTANKS + 0.0492))+ 22.6*RRAD + 125.4*VVAH +92.
        TANKDI= ASHELL    
# TAA-TANK  -  NOT VACUUM-PROOF ..................................
    elif(KTAN79==4):
        if(BBEXAC):
            CM.XTANKS=0.05
            if(ASHELL >28): CM.XTANKS=0.06  
            CM.YTANKS = 0.08
            if(ASHELL > 28): CM.YTANKS= 0.10
            CM.ZTANKS  = 0.12
            if(VTANK > 6.6):  CM.ZTANKS = 0.16
            if(VTANK > 11.5): CM.ZTANKS = 0.20  

        GTANK = 8.E+2*(ASHELL*(0.9*CM.XTANKS+0.45*CM.YTANKS)
                       + ACOVER*(1.42*CM.ZTANKS + 0.0492))+ 22.6*RRAD + 125.4*VVAH +92
        TANKDI= ASHELL    

    elif(KTAN79==5):
        if(BBEXAC):
            CM.TTANKS=0.025
            if(VTANK>19):CM.TTANKS=0.275

        GTANK=(ACOVER*(0.44+10.4*CM.TTANKS )+ 0.25*ASHELL)*100 +94.4*VTANK + 100*HTANK + 10.4
        TANKDI = 2*(BTANK+RLTANK)    

    elif(KTAN79==6):
        GTANK=  0.136*(ASHELL*100)** 1.28
        TANKDI = VTANK

    return (JFC,KTAN79,TANKDI,GTANK)
