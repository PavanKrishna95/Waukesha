#Title:  Total cost calculation in MNL79

def COST79():
    import com as C
    import common as CM
    from ccoret import CCORET
    from ctank import CTANK
    from cpipe import CPIPE
    from cfin import CFIN
    from cclle import CCLLE
    from cactp import CACTP
    from cwind import CWIND
    #DECLARATIONS
    BBREAC=False
    BBLNX=False
    FACTOR=1.E+3
    IHTAN=[1,3,5,6,7,8]
    EFKV=[0,0,0,0]
    ACONDA=[0,0,0,0]
    RCONN=[0,0,0,0]
    CURTML=[0,0,0,0]
    NCOND=[0,0,0,0]
    NGATE=[0,0,0,0]
    ZCABEL=[0 for i in range(9)]
    ZCOIAR=[0 for i in range(9)]
    CONVAR=[0 for i in range(9)]
    TCEPOX=[0 for i in range(9)]
    #END OF DECLARATIONS

    #SET CERTAIN VARIABLES
    BBPRNT=False
    if(C.BBEND and C.BBHELP[5]): BBPRNT=True
    CM.GSN24=CM.GSN241+CM.GSN242

    #CORE

    CCORET(BBPRNT,C.JFC,round(C.TYPCOR),C.ISTGRD,C.NCLA,CM.GSN211,CM.GSN212,CM.GG21,CM.GSN241,CM.GSN242,CM.GG24,CM.GSN25,C.DCORE*FACTOR)

    #WINDINCM.GSN

    for IWDG in range(1,1+C.NWILI):
        CCOV1=(C.HPART[IWDG-1]+C.BPART[IWDG-1]+C.TCOV1[IWDG-1])*FACTOR
        CCOV2=CCOV1+(C.TCOV2[IWDG-1]+(C.RPART[IWDG-1]-1.)*C.BPART[IWDG-1])*FACTOR
        WCLS=C.HPART[IWDG-1]*FACTOR
        NTAPP=2*C.NWOULI
        IT=C.IARR[20+IWDG-1]

        if(C.IARR[30+IWDG-1]==4):
            NTAPP=C.IARR[40+IWDG-1]*(C.IARR[5+IT-1]+C.IARR[10+IT-1]+2)*C.NWOULI
        XBUNCH=C.ZWIND[IWDG-1]*C.DWIND[IWDG-1]*C.IARR[40+IWDG-1]*C.PI*C.NWOULI
        ABUNCH=FACTOR*FACTOR*C.ACOND[IWDG-1]/C.IARR[40+IWDG-1]
        CBUNCH=XBUNCH*C.ACOND[IWDG-1]/(C.BPART[IWDG-1]*C.HPART[IWDG-1])
    #C... Calculate some auxiliary variables
#*
#C,,, Depending on winding type    
        if(C.KWITYP[IWDG-1] > 5):
            XBUNCH=XBUNCH/float(C.NLOOP[IWDG-1])
            ABUNCH=ABUNCH*float(C.NLOOP[IWDG-1])
       
        APARTX=FACTOR*FACTOR*C.HPART[IWDG-1]*C.BPART[IWDG-1]
        ACONDX=C.RPART[IWDG-1]*APARTX
        if(C.NCONDU[IWDG-1]==3): ACONDX=FACTOR*FACTOR*C.ACOND[IWDG-1]
        RGUID=C.DARR[IWDG-1]
        XPART=0.5+ABUNCH/APARTX
        CONVAR[IWDG-1]=C.UARR[30+IWDG-1]
        TCEPOX[IWDG-1]=C.UARR[40+IWDG-1]

        #WINDING COSTS
    
        CWIND(BBPRNT,C.JFC,IWDG,C.NCONDU[IWDG-1],C.KWITYP[IWDG-1],RGUID,
              CM.GSN11[IWDG-1],CM.GSN121[IWDG-1],CM.GSN122[IWDG-1],CM.GSN131[IWDG-1],
              CM.GSN132[IWDG-1],CM.GSN133[IWDG-1],CM.GSN134[IWDG-1],CM.GSN1351[IWDG-1],
              CM.GSN1352[IWDG-1],CM.GSN136[IWDG-1],APARTX,C.TCOV1[IWDG-1]*FACTOR,
              C.TCOV2[IWDG-1]*FACTOR,CCOV1,CCOV2,C.NWOULI,
              C.DWIND[IWDG-1]*FACTOR,C.RRWDG[IWDG-1]*FACTOR,WCLS,
              C.BDUCT[IWDG-1]*FACTOR,NTAPP,ACONDX,
              XBUNCH,ABUNCH,C.ZCODU[IWDG-1],C.NOUCO[IWDG-1],XPART,C.BBEXAC,
              C.BPART[IWDG-1]*FACTOR,ZCABEL[IWDG-1],ZCOIAR[IWDG-1],
              C.ZLAG[IWDG-1],BBLNX,C.RPART[IWDG-1],
              C.ZWIND[IWDG-1],C.IPISOL[IWDG-1],C.HPART[IWDG-1]*FACTOR,CBUNCH,
              CONVAR[IWDG-1],TCEPOX[IWDG-1])

    #Calculations for cleats & leads
    for ITML in range(1,1+C.NG):
        NCOND[ITML-1]=3
        NGATE[ITML-1]=1
        UNX=C.UN[ITML-1][1-1]
        if(C.BBVR[ITML-1]): UNX=C.UN[ITML-1][3-1]
        CURTML[ITML-1]==C.SRATEP[ITML-1]/UNX
        if(CURTML[ITML-1]>3150): NCOND[ITML-1]=1
        if(C.USURG[ITML-1]>=750E+3): NGATE[ITML-1]=2
        EFKV[ITML-1]=C.UN[ITML-1][1-1]/FACTOR

        #Cleats & leads costs
    CCLLE(BBPRNT,C.JFC,NCOND,NGATE,CM.GSN31,CM.GSN32,CM.GG32,EFKV)
    SUM41=0
    for I in range(1,1+9):
        
        SUM41=SUM41+CM.GSN41[I-1]

## Number of connections in each terminal
    for ITML in range(1,1+4):
        ACONDA[ITML-1]=0
        RCONN[ITML-1]=2
    # For each terminal
#*
#C,,, In the actual transformer
        if(ITML<=C.NG):
    #Assume 2.5 A/mm2 in cleats & leads
            ACONDA[ITML-1]=CURTML[ITML-1]/2.5
    #For each terminal
    #if regulated
            if(C.BBVR[ITML-1]):
                if(C.KTYPRW[ITML-1]==1):
                    RCONN[ITML-1]=2+2*(C.NPSTEP[ITML-1]+C.NMSTEP[ITML-1])
                if(C.KTYPRW[ITML-1]==2):
                    RCONN[ITML-1]=2+2*(C.NPSTEP[ITML-1]+C.NMSTEP[ITML-1])
                if(C.KTYPRW[ITML-1]==3):
                    RCONN[ITML-1]=2+2*(C.NPSTEP[ITML-1]+C.NMSTEP[ITML-1])
#C... Initialise CM.GSN48=0.
#*
#CC*SBBL
    CM.GSN48=0
   # Active part cost
    CACTP(BBPRNT,C.JFC,SUM41,CM.GSN42,CM.GSN45,CM.GSN46,CM.GSN47,CM.GSN48,C.NWOULI,\
    C.DCORE*FACTOR,CM.GSN24,CM.GG49,RCONN,ACONDA,EFKV,C.NG,BBREAC)
#SBBL

    NTANK=IHTAN[C.KTAN79-1]

    if(C.BBLT10): NTANK=NTANK+1
#CC*SEBL
#*
#C... Set a code for the radiators
#*
#C,,, NOT an exact calculation    
    if(not C.BBEXAC):
        KODRAD=4
     # Exact calculation
    else:
        KODRAD=1
        if(C.HTANK>2.1): KODRAD=2
        if(C.HTANK>2.5): KODRAD=3
        if(C.HTANK>2.8): KODRAD=4
        if(C.HTANK>3.3): KODRAD=5
    RSEK=32

    #Cooling equipment on direct on tank : NCEQ = 1
    NCEQ=1

    #IDUM is set to 0 - the corresponding NRAD in CTANK is not used
    IDUM=0

    #TANK COST
    CTANK(BBPRNT,C.JFC,NTANK,C.ACOVER,C.TANKDI,KODRAD,IDUM,RSEK,NCEQ,\
    CM.GSN51,CM.GSN52,CM.GSN53,CM.GSN61,CM.GSN71,CM.GSN72,CM.GG151,CM.GG152,\
    CM.GG51,CM.GG52,CM.GG54,CM.GG55,CM.GG61,CM.GG63,CM.GG71,CM.GG72,CM.GG74)

    #Pipe-work cost

    CPIPE(BBPRNT,C.JFC,CM.GSN81,CM.GSN91,CM.GSN92,CM.GSN102,
          CM.GG81, CM.GG83,CM.GG91,CM.GG92,CM.GG94,CM.GG101,CM.GG102)

#    Final assembly cost
    CFIN (BBPRNT,C.JFC,CM.GSN24, CM.GSN111,CM.GSN112,CM.GSN141,CM.GSN142,CM.GN1210,\
    CM.GG111, CM.GG1210, CM.GG151, CM.GG152)



















