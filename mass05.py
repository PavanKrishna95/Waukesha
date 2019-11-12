def MASS05(BBPRNT,JFC,BB51,GTANK,VTANK,ACOV,ATAWA,BB07,\
    GCOVER,KCOOL1,PLOSS,AFIELD,GRAD,OTANK,KTAN79):
    import common as CM
    #TANK, COVER, COOLING EQUIPMENT, SOUND SCREENS
#      #############################################
#
#      BBPRNT     TRUE IF PRINTOUT OF INPUT/OUTPUT DATA
#      JFC        FILECODE FOR PRINTOUT
#      BB51 =     SPARE
#      GTANK =    NET MASS TRANSFORMER TANK, CALCULATED IN THE
#                 TECHNICAL ROUTINES       (KG)
#      VTANK =                             (DM3)
#      ACOV =     COVER AREA               (M2)
#      ATAWA =    AREA OF THE TANK SIDES   (M2)
#      BB07 =     LOGICAL VARIABLE = TRUE IF THE COVER MASS IS
#                 ALREADY CALULATED (=GCOVER)
#      GCOVER =   COVER MASS
#
#      KCOOL1 =   CODE FOR THE COOLING EQUIPMENT
#                 0 = NO COOLING EQUIPMENT
#                 1 = BUILT-ON RADIATORS
#                 2 = BUILT-ON RADIATOR BATTERIES
#                 3 = SEPARATE RADIATOR BATTERIES
#                 4 = BUILT-ON HEAT EXCHANGERS (OFAF)
#                 5 = SEPARATE HEAT EXCHANGERS (OFAF)
#                 6 = BUILT-ON HEAT EXCHANGERS (OFWF)
#
#      PLOSS =    MAX TRANSFORMER LOSSES AT ANY TAP         (W)
#      AFIELD =   AREA OF FIELD SHIELDS AGAINST TANK WALL   (M2)
#      GRAD =     MASS OF RADIATORS (FROM TECHNICAL ROUTINES)  (KG)
#      OTANK =    CIRCUMFERENCE OF THE TANK                 (MM)
#
#      KTAN79 =   TANK CODE
#                 1 = OVAL TANK         TMY
#                 2 = RECTANGULAR TANK  TMY
#                 3 = TAA, VACUUM-PROOF
#                 4 = TAA, NOT VAKUUM-PROOF
#                 5 = TBA
#                 6 = OTHER TYPES , TMY
#
#------------------------------------------------------------------
#      IMPLICIT DOUBLE PRECISION(A-H,O-Z)

    CA=[172.6, 121.4, 160.9, 59.71, 110.85, 96.99]
    CB=[1.040, 1.148, 1.172, 1.394, 1.200, 1.230]


    if(BBPRNT):
        #PMASS5(BBPRNT,JFC,BB51,GTANK,VTANK,ACOV,ATAWA,BB07,\
         #              GCOVER,KCOOL1,PLOSS,AFIELD,GRAD,OTANK,KTAN79)
        pass
    #TANK MANUFACURED
    CM.GSN51 = GTANK
    CM.GG51 = 0.01 *CM.GSN51
#*
#****TANK OTHERS
    CM.GSN52 = 0.04 *CM.GSN51
    CM.GG52 = 0.02 *CM.GSN51
#*
#****   RADIATORS
    CM.GG54 =GRAD
#*
#****   FIELD SHIELDS AGAINST TANK WALL
    CM.GSN53 =  9.0 *AFIELD
    CM.GG53 = 0
#*
#****   DETAILS FOR SOUND SCREEN ASSEMBLY
    CM.GSN054=0.012*OTANK
    CM.GG054=0.05*CM.GSN054
#*
#****   GOODS, TANK ASSEMBLY
    CM.GG55= 0.01*CM.GSN51
#*
#****   COOLING EQUIPMENT
    CM.GSN61 = 0
    CM.GG61 = 0

    if(not(KCOOL1<=0)):
        
        if(KCOOL1==2):
            #BUILT-ON RADIATORS
            CM.GSN61=0.0289*PLOSS**0.9
            CM.GG61  = 0.02 *CM.GSN61
            
        elif(KCOOL1==3):
       #      SEPARATE RADIATOR BATTERIES
            CM.GSN61=0.0323*PLOSS**0.9
            CM.GG61  = 0.02 *CM.GSN61
            
        elif(KCOOL1==4 or KCOOL1==6):
         #   BUILT-ON HEAT EXCHANGERS (OFAF, OFWF)
            CM.GSN61=0.0036*PLOSS**0.9
            CM.GG61  = 0.02 *CM.GSN61
    
        elif(KCOOL1==5):
         #    SEPARATE HEAT EXCHANGERS
            CM.GSN61=0.012*PLOSS**0.9
            CM.GG61  = 0.02 *CM.GSN61
      
#    GOODS, COOLING EQUIPMENT ASSEMBLY
    CM.GG63= 0.01*CM.GSN51
#*
#****   COVER
    if(BB07): CM.GSN71 = GCOVER
    if(not BB07): CM.GSN71  = CA[KTAN79-1] * ACOV**CB[KTAN79-1]
    CM.GG71  = 0.02 *CM.GSN71
#*
#****   MANUFACORING DETAILS EXCLUDING HEAVY PART
    CM.GSN72= 0.04 * CM.GSN71
    CM.GG72 = 0.02 * CM.GSN72
##*
#****   GOODS, COVER ASSEMBLY
    CM.GG74 = 0.01 * CM.GSN72
    return
