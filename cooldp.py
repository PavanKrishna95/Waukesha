#Title:  Estimate a preliminary price
#        for the coolers if required.
#        The following types can be handled:
#        (CODE = Cooling type) :
#        1=ONAN,  2=ONAF,  3=OFAF,  4=ONAN/F
def COOLDP():
    import com as C

    print("start of COOLDP")

    #Cooling

    if(C.KCOOL != 0):
        PK=C.URC[0][0][0]
        if(C.BBVR[0]): PK=max(PK,C.URC[1][0][0],C.URC[2][0][0])
        if(C.BBVR[1]): PK=max(PK,C.URC[0][1][0],C.URC[0][2][0])

        PK=PK*C.NWOULI

    #Mean oil temperature rises (C.DTSNN,C.DTSNF,C.DTSFF)
    #calculated in 'PKL75'

    #ONAN
        if(C.KCOOL==1):
            AONAN=C.P00[1]+PK
            C.GRAD=AONAN/22*(40/C.DTSNN)**1.33
    #OFAF
        elif(C.KCOOL==3):
            AOFAF=C.P00[1]+PK
            C.GVVAH=AOFAF/(C.DTSFF*9267)*2500

    #ONAF
        elif((C.KCOOL==2)or(C.KCOOL==4)):
            if(C.FONAN<=1):
                AONAF=C.P00[1]+PK
                AONAN=C.P00[1]+PK*C.FONAN*C.FONAN
            else:
                AONAF=C.P00[1]+PK*C.FONAN*C.FONAN
                AONAN=C.P00[1]+PK

            GRADNN=AONAN/22*(40/C.DTSNN)**1.33
            GRADNF=AONAF/2.22/C.DTSNF    
    
            C.GRAD=max(GRADNN,GRADNF)
            PF=AONAF/(C.GRAD*0.111)*(40/C.DTSNF)
            VTOT=0.0185*C.GRAD*(1.81/(2-(PF/1.E+3))-1)
            C.GFAN=13.07*VTOT
   
    print("end of COOLDP")        
    return



