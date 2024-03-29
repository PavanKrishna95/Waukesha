
#TITLE=CMASS01   *******MASS01 - CORE DETAILS
def MASS01(BBPRNT,JFC,NCOR,NLAM,NCLA,BH,DCORE,OH,OL,
           COCAN,CORLAN,CORLAX,GASEC ):
    import common as CM

    if(BBPRNT):
        #PMASS1(BBPRNT,JFC,NCOR,NLAM,NCLA,BH,DCORE,OH,OL,COCAN,CORLAN,CORLAX,GASEC)
        pass
    #STANDARD VALUE: 0.666 KG STEATITE SPACERS / M2.
    STEK=0.666

    #CORE LAMINATION
    CM.GSN241=CORLAN
    CM.GSN242=CORLAX

    # NET MASS FOR CORE CLAMPS, DETAILS OF STEEL  (CM.GSN211),
  # IS CALCULATED SEPARATELY IN ROUTINE "PBALK"

  #NET MASS CORE CLAMPS, DETAILS OF NON-STEEL
    CM.GSN212= 0.021*(CM.GSN241+CM.GSN242)**0.825

    # NET MASS CORE CLAMP GOODS.
    CM.GG21 = 0.1* CM.GSN211

    #NET MASS STEATITE SPACERS  (FOR COOLING DUCTS IN THE CORE)
    IHLP=2
    if(NCOR==3 or NCOR==8): IHLP=3
    if(NCOR>=9): IHLP=4
    CM.GG24 = STEK*1.E-6 *COCAN* (IHLP *BH *DCORE +2.*OH*OL )

    # MASS OF ASECOND TAPE
    CM.GSN25= GASEC



