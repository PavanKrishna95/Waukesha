def MASS06(BBPRNT,JFC,BB08,KCOOL1,PLOSS,KCOOL2,GFAN):
    import common as CM
    #CONSERVATOR, PIPES, CONTROL CABLING
#      ###################################
#
#      BBPRNT     PRINTOUT OF INPUT/OUTPUT IF TRUE
#      JFC        FILECODE FOR PRINTOUT
#      BB08 =     LOGICAL VARIABLE = TRUE IF THE CONSERVATOR IS
#                                    MOUNTED ON THE TANK
#      KCOOL1 =   CODE FOR COOLING EQUIPMENT
#                 1 = BUILT-ON RADIATORS
#                 2 = BUILT-ON RADIATOR BATTERIES
#                 3 = SEPARATE RADIATOR BATTERIES
#                 4 = BUILT-ON HEAT EXCHANGERS (OFAF)
#                 5 = SEPARATE HEAT EXCHANGERS (OFAF)
#                 6 = BUILT-ON HEAT EXCHANGERS (OFWF)
#
#      PLOSS =    MAX TRANSFORMER LOSSES AT ANY TAP  (W)
#
#      KCOOL2 =   CODE FOR COOLING EQUIPMENT CONTROL CABLING
#                 1 = SELF-COOLED TRANSFORMER OR NO COOLING EQUIPMENT.
#                 2 = ONAF - COOLED TRANSFORMERS
#                 3 = OFAF OR OFWF - COOLED TRANSFORMERS
#
#       GFAN =     FAN MASS ESTIMATED IN THE TECHNICAL ROUTINES (KG)
#
#
#---------------------------------------------------------------------
#      IMPLICIT DOUBLE PRECISION(A-H,O-Z)
    if(BBPRNT):
        #PMASS6(BBPRNT,JFC,BB08,KCOOL1,PLOSS,KCOOL2,GFAN)
        pass
    #CONSERVATOR#####   BB08  = .TRUE. IF THE CONSERVATOR IS MOUNTED ON THE TRANSFORMER
    if(BB08):  CM.GSN81 = 0.123 * CM.GSN142*0.9
    if(not BB08):  CM.GSN81 = 0.07 *CM.GSN142
    CM.GG81  = 0.05 * CM.GSN81
##
#####   GOODS, CONSERVATOR ASSEMBLY
    CM.GG83 = 0.01 * CM.GSN81
##
#####   PIPES
#####   PIPES  TO THE CONSERVATOR
    
    CM.GSN91  = 1.1E-5 * CM.GSN142**1.5
    CM.GG91  = 0.1 *CM.GSN91
##---------------------------------------------------------------------
#####   PIPES TO THE COOLING EQUIPMENT

    if(KCOOL1>0):
        if(KCOOL1==1):
            #BUILT ON RADIATORS
            CM.GSN92=0

        elif(KCOOL1==2):
            #BUILT ON RADIATOR BATTERIES
            CM.GSN92=3.01E-5*PLOSS**1.2
    

        elif(KCOOL1==3):
            #SEPARATE RADIATOR BATTERIES
            CM.GSN92=0.146*PLOSS**0.7
           

        elif(KCOOL1==4 or KCOOL1==6):
            CM.GSN92=3.01E-5*PLOSS**1.2
            
        elif(KCOOL1==5):
            CM.GSN92=0.088*PLOSS**0.7
    ####   COMMON PART - PIPE CONNECTIONS TO THE COOLING EQUIPMENT
    CM.GG92 = 0.1 *CM.GSN92
    #---------------------------------------------------------------------
    ####   MASS OF FANS
    CM.GG101= GFAN
    #
    ####   GOODS, COOLING EQUIPMENT ASSEMBLY
    CM.GG94= 0.01* (CM.GSN92 + CM.GSN91)
    #---------------------------------------------------------------------
    ####   CONTROL CABLING
    if(KCOOL2>0):
        if(KCOOL2==1):
            CM.GSN102=9.13E-3 *PLOSS**0.7
            #GOODS,CONTROL CABLING ASSEMBLY
            CM.GG102=0.30*CM.GSN102
           
        elif(KCOOL2==2 or KCOOL2==3):
            CM.GSN102  = 0.0135  *PLOSS**0.7
            #GOODS,CONTROL CABLING ASSEMBLY
            CM.GG102=0.30*CM.GSN102
    return
