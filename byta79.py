#Title:  Calculation of comparison price in MNL79
def BYTA79():
    import com as C
    import common as CM
    print("\n")
    print("start of BYTA79")
    
    GS=[0]*500
    CS=[0]*500
    
    #Local Functions

    #Start of the functions block.
    for I in range(1,242):
        GS[I-1]=CM.RES79[I-1][1-1]+CM.RES79[I-1][4-1]
        CS[I-1]=CM.RES79[I-1][3-1]+CM.RES79[I-1][5-1]+CM.RES79[I-1][6-1]

    #End of the functions block.

    #MNL79 preparation of costs

    #Windings

    #Start of the windings block.

    SUMWIN=0

    #Summations for all windings

    for IWDG in range(1,1+C.NWILI):
        SUMWIN=SUMWIN+GS[IWDG*19-1]

    # End of the windings block.    

    #Calculations

    #Start of the calculations block.
    C.GACTP=SUMWIN+GS[166]+GS[178]+GS[195]+GS[235]
#C... (166) = Core Subtotal
#C... (178) = Cleats & leads Subtotal
#C... (195) = Active part others Subtotal
#C... (235) = Oil absorbed
#*
#C... Transport mass calculation changed 88-02-04
    C.GTRP=C.GACTP+GS[199]+GS[212]

#C... (199) = Tank manuf. + field screen
#C... (212) = Cover subtotal
#*
#C... (202) = Tank Subtotal
#C... (206) = Cooling equipment Subtotal
#C... (221) = Pipe connections
#C... (225) = Control cabling
#C... (229) = Sound screens
#C... (232) = Final Assembly excluding oil
#C... (200) = Radiators
#C... (222) = Fans
#*
#CCCCC  C.GTRP=C.GACTP+GS(203)+GS(213)+GS(207)+GS(222)+
#CCCCC&           GS(226)+GS(230)+GS(233)-GS(201)-GS(223)

    C.GTANK=GS[199]
    C.GCOVER=GS[210]
    C.GCONS=GS[216]
    C.CTROVN=CS[234]-CS[200]-CS[222]

#CMANUF = Manufacturing C.COST in comparison price

    CM.RES79[241-1][3-1]=CM.RES79[241-1][3-1]
    CMANUF=CS[241-1]

    C.COST=CMANUF
    C.COST=C.COST+C.CPUPT*C.CTROVN

#C... MNL87 modification :
#C... Packing costs CPACK = 0 : they are now included in 'Dismantling'
#C... as per Memo of 88-06-06 Seppo Ylikoski COMP/K
    
    C.COST=(C.COST)*(1+C.CPUFIX)
    print("end of BYTA79")

    # End of the functions block.
    return


    
