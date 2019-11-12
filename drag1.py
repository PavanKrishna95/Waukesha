
def DRAG1(TYP,PTOT,QAKTIV):
    
    ''' BEST³MNING AV ANTAL DRAGSKENOR OCH DESS DIMENSIONER '''

    BELD=[4755.,9150.,11175.,11175.]

    ''' DIMENSIONERANDE BELASTNING (BEL) '''

    BEL=0.015*QAKTIV+0.9*PTOT

    ''' KONTROLL ATT INTE MAX TILL*TEN BELASTNING öVERSKRIDES '''

    ITYP=TYP-6
    BELA=BELD[ITYP-1]
    PRMAX=0.

    if(BEL >BELA):
        PRMAX=min(BELA,(BELA-QAKTIV*0.01)/0.75)

    ''' BEST³M DRAGSKENEALTERNATIV '''
    
    IDRAG=4
    if ITYP ==1:
        if(BEL <= 3170.): IDRAG=3
        if(BEL <= 1580.): IDRAG=2
        if(BEL <= 1060.): IDRAG=1

    elif ITYP ==2:
        if(BEL <= 6100.): IDRAG=3
        if(BEL <= 3050.): IDRAG=2
        if(BEL <= 2040.): IDRAG=1
    
    elif ITYP ==3 or ITYP==4:
        if(BEL <= 7450.): IDRAG=3
        if(BEL <= 3730.): IDRAG=2
        if(BEL <= 2500.): IDRAG=1
 
    ''' DRAGSKENEDIMENSIONER '''
    

    if IDRAG ==1:
        NDRAG=2
        BDRAG=75.
        TDRAG=10.
        
    elif IDRAG==2:
        NDRAG=2
        BDRAG=75.
        TDRAG=15.
    
    elif IDRAG ==3:
        NDRAG=4
        BDRAG=75.
        TDRAG=15.
      
    elif IDRAG ==4:
        NDRAG=6
        BDRAG=75.
        TDRAG=15.
 
    ALT=IDRAG

    return NDRAG,BDRAG,TDRAG,ALT,BEL,PRMAX
