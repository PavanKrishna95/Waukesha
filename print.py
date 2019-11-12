def pnt():
    import com as C
    import cominp as CI
    IPOS=[[1,1,1,2,1,3,1,4,2,1,2,2,2,3,2,4],\
        [3,1,3,2,3,3,3,4,4,1,4,2,4,3,4,4]]
    URC12X=[0]*16
    URC13X=[0]*16
    URC23X=[0]*16
    UXC12X=[0]*16
    UXC13X=[0]*16
    UXC23X=[0]*16
    URFCTR=C.ZWOULI/1.E+3
    ACONDX=[0]*4
    WLOSSEX=[0]*4
    RRWDGX=[0]*4
    for I in range(1,1+16):
        INDI=IPOS[1-1][I-1]
        INDJ=IPOS[2-1][I-1]
        print(C.URC[INDI-1][INDJ-1][1-1])
        URC12X[I-1]=C.URC[INDI-1][INDJ-1][1-1]*URFCTR
        URC13X[I-1]=C.URC[INDI-1][INDJ-1][2-1]*URFCTR
        URC23X[I-1]=C.URC[INDI-1][INDJ-1][3-1]*URFCTR
        UXC12X[I-1]=C.UXC[INDI-1][INDJ-1][1-1]*100.
        UXC13X[I-1]=C.UXC[INDI-1][INDJ-1][2-1]*100.
        UXC23X[I-1]=C.UXC[INDI-1][INDJ-1][3-1]*100.
    for IWDG in range(1,5):
        ACONDX[IWDG-1]=1.E+6*C.ACOND[IWDG-1]
        WLOSSEX[IWDG-1]=C.WLOSSE[IWDG-1]/1.E+3
        RRWDGX[IWDG-1]=1.E+3*C.RRWDG[IWDG-1]

    
    print("\n")
    print("\n")
    print("OUTPUT")
    print("LIMB HEIGHT=",C.HLIMB*1000)
    print("CORE DIAMETER=",C.DCORE*1000)
    print("LIMB FLUX DENSITY=",C.BLIMB,C.BMAXPU)
    print("REACTANCE(1-2%)=",C.USHORE)
    #print("PK1-2=",URC12X)
    #print("PK1-3=",URC13X)
    #print("PK2-3=",URC23X)
    #print("X1-2=",UXC12X)
    #print("X1-3=",UXC13X)
    #print("X2-3=",UXC23X)
    print("AREA=",ACONDX)
    print("P0=",C.AARR[5])
    print("PK=",C.AARR[6])
    print("tnk W=",C.BTANK*1000)
    print("tnk H=",C.HTANK*1000)
    print("tnk L=",C.RLTANK*1000)
    print("Space F=",C.FILLF)
    print("RII=",C.WLOSSR)
    print("trnsp mass=",C.GTRP)
    print("EDDY=",WLOSSEX)
    print("Wind.wdt=",RRWDGX)
    print("Duct.wdt=",C.BDUCT)
    print("Loss EVALUATION PO=",CI.EVALP0)
    print("Loss EVALUATION PK=",CI.EVALPK)
