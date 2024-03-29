def MASS04(BBPRNT,JFC,DBW,DWINDY,DUMMY,RJH,NWOLI,NCLA,
           CORLAN,CORLAX,NCOR,DCORE,DWOL,BH,TWSUP,BB048):
    import common as CM
    # ACTIVE PART
#      ###########
#
#      BBPRNT =   IF TRUE PRINTOUT OF INPUT/OUTPUT DATA
#      JFC        FILECODE FOR PRINTOUT
#      DBW =      FOR EY-CORES: DISTANCE BETWEEN WINDING AND SIDELIMB.
#                 FOR OTHER CORE TYPES:  DISTANCE BETWEEN PHASES   (MM)
#      DWINDY =   OUTER DIAMETER OF OUTER WINDING           (MM)
#      RJH =      ADJUSTMENT HEIGHT OF THE WINDINGS         (MM)
#      NWOLI =    NUMBER OF WOUND LIMBS
#
#
#      NCLA =     CORE CLAMP CODE
#                 1 = CORE CLAMPS OF WOOD
#                 2 = CORE CLAMPS OF STEEL PROFILE
#                 3 = CORE CLAMPS OF STEEL PLATE
#
#      CORLAN =   MASS OF CORE LAMINATION WITHOUT EXTRA VARNISH (KG)
#      CORLAX =   MASS OF CORE LAMINATION WITH    EXTRA VARNISH (KG)
#
#      NCOR =     CORE-CODE
#                 1 = D     1-PHASE WITH 2 WOUND LIMBS
#                 3 = T     3-PHASE WITH 3 WOUND LIMBS
#                 7 = EY    1-PHASE WITH 1 WOUND LIMB,  SIDELIMBS
#                 8 = DY    1-PHASE WITH 2 WOUND LIMBS, SIDELIMBS
#                 9 = TY-1  1-PHASE WITH 3 WOUND LIMBS, SIDELIMBS
#                 10= TY-3  3-PHASE WITH 3 WOUND LIMBS, SIDELIMBS
#
#      DCORE =    CORE DIAMETER      (MM)
#      DWOL =     DISTANCE FROM WINDING TO SIDE LIMB IF APPLICABLE,
#                 ELSE =0.
#      BH =       LIMBHEIGHT         (MM)
#      TWSUP =    THICKNESS OF WINDING SUPPORT   (MM)
#      BB48 =     LOGICAL VARIABLE = TRUE IF ELECTROSTATIC SHIELDS ON
#                                    REACTOR CORE LIMBS.
#---------------------------------------------------------------------
#      IMPLICIT DOUBLE PRECISION(A-H,O-Z)

    #INSULATION DETAILS IN THE MAIN DUCT (CM.GSN41) IS
#*      CALCULATED IN ROUTINE 'MASS02'.
    if(BBPRNT):
        #PMASS4(BBPRNT,JFC,DBW,DWINDY,DUMMY,RJH,NWOLI,NCLA,\
    #CORLAN,CORLAX,NCOR,DCORE,DWOL,BH,TWSUP,BB048)
        #INSULATION DETAILS OUTSIDE THE OUTER WINDING
        pass
        #STANDARD VALUES:
#*      WIDTH OF THE RIBS (MM):
    RIB=20
    #    WITH OF DUCT INSIDE SPLIT CYLINDERS, OUTSIDE OUTER WINDING
    CANALY=DBW-45
    if(CANALY<0): CANALY=0

    #NUMBER OF CLACK ROWS IN OUTER WINDING
    PCLACY = DWINDY* 0.02474
    #NUMBER OF SPLIT CYLINDERS OUTSIDE OUTER WINDING:
    RCYLY  = CANALY/14.
    CM.GSN42  = 1.22E-6*RJH*NWOLI* (RIB*PCLACY*(CANALY-RCYLY) +
                                    3.1415*(RCYLY*(DWINDY+CANALY) ) )

    #INSULATION AND SUPPORTING DETAILS AGAINST THE YOKES
    HELP=0.68
    if(NCLA==1): HELP=0.38
    CM.GSN46 = HELP* (CORLAN + CORLAX)** 0.63

    #INSULATION OF SIDE LIMBS
    CM.GSN45=0
    if(NCOR > 3): CM.GSN45=2.E-7*(DCORE+400)*DWOL*BH

    #WINDING SUPPORTS
    CM.GSN47= 237.E-7*NWOLI*TWSUP*(DWINDY-DCORE)**2

    #ELECTROSTATIC SHIELDING OF REACOR CORE LIMBS
    if(BB048): CM.GSN48 = 1.9E-5 *DCORE*BH*NWOLI

    #NET MASS OF GOODS FOR ACTIVE PART
    CM.GG49=  0.047*(CORLAN + CORLAX)** 0.7


