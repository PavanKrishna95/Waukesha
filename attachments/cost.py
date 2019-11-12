def COST(N,LC,LM,GS,BGSG,BCS,GG,BCG,BCM1,BCM2,BCM3,BCM4):
    import common as CM
    import math
    import numpy
    if(LC!=0):
        #print("Start of cost")
        AGSG=BGSG
        if(AGSG==0.): AGSG=1
        ACS  = BCS
        if(ACS  == 0.): ACS  = 1
        ACG  = BCG
        if(ACG  == 0.): ACG  = 1
        ACM1 = BCM1
        if(ACM1 == 0.): ACM1 = 1
        ACM2 = BCM2
        if(ACM2 == 0.): ACM2 = 1
        ACM3 = BCM3
        if(ACM3 == 0.): ACM3 = 1
        ACM4 = BCM4
        if(ACM4 == 0.): ACM4 = 1

        #NET. WEIGHT  SHAPED MATERIAL
        CM.R4[0]=GS

        #GROSS WEIGHT SHAPED MATERIAL
        CM.R4[1] =  CM.R79[0][LC-1]*GS* AGSG**CM.R79[1][LC-1]

        #SHAPED MATERIAL COSTS
        CM.R4[2] = CM.R79[2][LC-1]*CM.R4[1]*ACS**CM.R79[3][LC-1]

        #GOODS WEIGHT
        CM.R4[3] = GG

        #GOODS COSTS
        CM.R4[4] =CM.R79[4][LC-1]*GG*ACG**CM.R79[5][LC-1]
        print("ACM1={0} ACM2={1} ACM3={2}".format(ACM1,ACM2,ACM3))
        #MANUFACTURING   COSTS
        CM.R4[5] = CM.R79[6][LC-1]*CM.R79[7][LC-1] *math.exp(CM.R79[8][LC-1]*math.log(ACM1)  + CM.R79[9][LC-1]*numpy.log(ACM2) +\
    CM.R79[10][LC-1]*numpy.log(ACM3) + CM.R79[11][LC-1]*numpy.log(ACM4))
        if(BCM1< 1.E-6): CM.R4[5]=0

        #COST ACCUMULATION
        for I in range(1,7):
            CM.RES79[LM-1][I-1] = CM.RES79[LM-1][I-1] + CM.R4[I-1]
            CM.R3[I-1]   = CM.R3[I-1]   + CM.R4[I-1]
            CM.R2[I-1]   = CM.R2[I-1]   + CM.R4[I-1]
            if(LM<=235): CM.RES79[235-1][I-1]=CM.RES79[235-1][I-1]+CM.R4[I-1]

        CM.RES79[240][2] = CM.RES79[240][2] + CM.R79[12][LC-1] * CM.R4[2]
        CM.RES79[240][4] = CM.RES79[240][4] + CM.R79[13][LC-1] * CM.R4[4]
        CM.RES79[240][5] = CM.RES79[240][5] + CM.R79[14][LC-1] * CM.R4[5]    

    if(N==1 or N==4 or N==5):
        return
    elif(N==3):
        for I in range(1,7):
            CM.RES79[LM-1][I-1]=CM.R3[I-1]
            CM.R3[I-1]=0
        return        
    elif(N==2):
        for I in range(1,7):
            CM.RES79[LM-1][I-1]=CM.R2[I-1]
            CM.R3[I-1]=0
            CM.R2[I-1]=0
        return    
    return
