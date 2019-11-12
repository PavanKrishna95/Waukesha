
def MASS03(BBPRNT,JFC,J,KCON,UPHAS,RIPHAS,BH,NWOLI,
           NCON,RLCON,BOOST):
    import common as CM
    #CLEATS AND LEADS
#      ################
#      BBPRNT    IF TRUE PRINTOUT OF INPUT/OUTPUT DATA
#      JFC       FILECODE FOR PRINTOUT
#      J =       TERMINAL NUMBER (1,2,3 OR 4)
#      KCON =    CODE FOR CLEATS AND LEADS
#                1 = 1-PHASE  1 WOUND LIMB
#                2 = 1-PHASE  2 WOUND LIMBS
#                3 = 1-PHASE  3 WOUND LIMBS
#                4 = 1-PHASE  4 WOUND LIMBS
#                5 = 3-PHASE  Y CONNECTED
#                6 = 3-PHASE  Y/AUTO  CONNECTED
#                7 = 3-PHASE  Z CONNECTED
#                8 = 3-PHASE  D CONNECTED
#      UPHAS =   PHASE VOLTAGE (=MAIN VOLTAGE/SQRT(3) )      (V)
#      RIPHAS =  MAX WINDING CURRENT                         (A)
#      BH    =   LIMB HEIGHT                                 (MM)
#      NWOLI =   NUMBER OF WOUND LIMBS
#      NCON =    NUMBER OF REGULATING LOOPS.
#                (=0 FOR NOT REGULATED TERMINALS)
#      RLCON =   MEAN DISTANCE FROM REG. WINDING TO TAP CHANGER  (MM)
#      BOOST =   BOOSTER FACTOR. THE CURRENT IN THE REG.WINDING IS
#                REDUCED WITH THE BOOST.FACTOR.(NORMALLY  BOOST = 1)
#-------------------------------------------------------------------
#      IMPLICIT DOUBLE PRECISION(A-H,O-Z)
    X31=[82.E-7,123.E-7,164.E-7,205.E-7,205.E-7,164.E-7,246.E-7,271.E-7]

    if(BBPRNT):
        #PMASS3(BBPRNT,JFC,J,KCON,UPHAS,RIPHAS,BH,NWOLI,NCON,RLCON,BOOST)
        pass
    if(BOOST<=0): BOOST=1

    #CONDUCTORS  IN CLEATS AND LEADS
    CM.GSN31[J-1] = (X31[KCON-1]*RIPHAS*BH*(1+0.0056*UPHAS**0.3)+
                     10.E-8*NWOLI*NCON**1.2*RLCON*(RIPHAS/BOOST)**1.485*(1+0.0056*UPHAS**0.3))
        
        #MOUNTING, SUPPORTING AND INSULATION DETAILS
    CM.GSN32[J-1] = 5.3 * CM.GSN31[J-1]**0.7
    CM.GG32[J-1] = 0.05 *(CM.GSN31[J-1] +CM.GSN32[J-1] )



