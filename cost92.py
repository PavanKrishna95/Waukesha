#Title:  Calculation of costs, simplified routines
def COST92():

    import com as C
    import common as CM

    #Copper costs

    C.CUCOS=0
    C.CUCOSP=0
    for IWDG in range(1,1+C.NWILI):
        J=C.NCONDU[IWDG-1]
        X=C.GWINCO[IWDG-1]*CM.CUC92[J-1]* C.ZWOULI
        C.CUCOS=C.CUCOS+X
        C.CUCOSP=C.CUCOSP+X*CM.CUC92P[J-1]


    #Core lamination C.COST
    C.FECOS  = C.GCORLA * CM.FEC92[C.ISTGRD-1]
    C.FECOSP = C.FECOS  * CM.FEC92[C.ISTGRD-1]

    #Free Oil C.COST
    C.OLCOS  = C.GOIL   * CM.OLC92
    C.OLCOSP = C.OLCOS  * CM.OLC92P

    C.CTROVN = C.FECOS  + C.CUCOS  + C.OLCOS
    C.CTRCMP = C.FECOSP + C.CUCOSP + C.OLCOSP
    C.COST   = C.CTRCMP * (1+C.CPUFIX)

    return
