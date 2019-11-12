
''' Description
    Main routine for the  TA1 Core calculation

    Based on 1ZBA-4650-101 dated 30 Octiber 1990
    Paragraph 8.1: Acceleration Forces
    Paragraph 8.2: Number of Yoke Bolts
    Paragraph 8.3: Number of Flitch Plates '''

def CORTA1(DCORNI,TCORST,RNK,PLIMBI,HLIMBI,FHDI,ifLPMT,
           RMWBL,FAF,ACCLN,ACCVE,ETA,BSTEPI,BPLMAI,BBMECH,
           RLAPSI,BBSTLP,DEWBI,DIWBI,RMAP):

    GFORCE=9.81
    ''' Input in parameter list is in (m).
        All variables named xxI are converted internally in this routine to xx in (mm)

        DCORN  Net Diameter of core, mm
        TCORST Thickness of Core plate material
        RNK    Number of cooling ducts
        PLIMB  Limb pitch, mm
        HLIMB  Limb Height, mm
        FHD    Flitch plate hole diameter, mm
        ifLPMT Flitch plate material, 1 - ST52, 2 OX812
        RMWBL  Mass of winding block, kg
        FAF    Prestressing force winding block, N
        ACCLN  Longitudal transport acceleration , *G
        ACCVE  Vertical transport acceleration, *G
        ETA    Spacefactor of core sheets
        BSTEP  Core Step Width increment, mm
        BPLMAX Maximum  core plate width available, mm
        BPLMAI Maximum  core plate width available, m
        BBMECH Detailed mechanical calculation TRUE FALSE

        The following is required if BBMECH = .TRUE.
        RLAPS  Overlap width in joint, mm
        BBSTLP Type of stepping, FALSE = norm, TRUE = steplap
        DEWB   Outer diameter winding block, mm
        DIWB   Inner diameter winding block, mm
        RMAP   Mass of active part, kg '''

    ''' Output

        ACORE  Area of Core Limb
        RMLMB  Mass of Limb
        RMYK   Mass of Yoke
        RMCRNR Mass of Corner

        NSHT   Number of sheets per packet, array
        SHTWDT Width of sheets (per packet), array, m
        THKPCK Thickness of package (per packet), array, m
        RMXWDT Maximum width of an individual packet, m
        RMNWDT Minimum width of an individual packet, m
        HYOKE  Height of Yoke, m
        HCORE  Height of Core, m
        TKO    Thickness of core, m
        RNFLPL Number of flitch plates
        BBLARM Transmits a warning signal, LOGICAL
        ALARM  Transmits a warning message, CHARACTER '''

    ''' Data Initialisation (ANSI does not permit data initialisation in
        a type declaration statement. '''

    RMAF[0][0]= 400000.
    RMAF[0][1]= 800000.
    RMAF[1][0]= 800000.
    RMAF[1][1]=1700000.
    RMAF[2][0]= 800000.
    RMAF[2][1]=1700000.
    RMAF[3][0]=1300000.
    RMAF[3][1]=2500000.
    RMAF[4][0]=1300000.
    RMAF[4][1]=2500000.

    RMLF[0]=1000000.
    RMLF[1]=1700000.
    RMLF[2]=2600000.
    RMLF[3]=2600000.
    RMLF[4]=3200000.

    RMVF[0]=1000000.
    RMVF[1]=1500000.
    RMVF[2]=2000000.
    RMVF[3]=2000000.
    RMVF[4]=2000000.

    CDR[0][0]= 400.
    CDR[0][1]= 550.
    CDR[1][0]= 500.
    CDR[1][1]= 750.
    CDR[2][0]= 650.
    CDR[2][1]= 900.
    CDR[3][0]= 750.
    CDR[3][1]=1000.
    CDR[4][0]= 750.
    CDR[4][1]=1000.

    TFP[0][0]= 440000.
    TFP[0][1]= 860000.
    TFP[1][0]= 880000.
    TFP[1][1]=1720000.
    TFP[2][0]=1320000.
    TFP[2][1]=2580000.

    RNBRS[0][0]=2.
    RNBRS[0][1]=4.
    RNBRS[0][2]=2.
    RNBRS[0][3]=2.
    RNBRS[1][0]=4.
    RNBRS[1][1]=6.
    RNBRS[1][2]=4.
    RNBRS[1][3]=4.
    RNBRS[2][0]=6.
    RNBRS[2][1]=8.
    RNBRS[2][2]=6.
    RNBRS[2][3]=4.
    RNBRS[3][0]=6.
    RNBRS[3][1]=8.
    RNBRS[3][2]=6.
    RNBRS[3][3]=6.
    RNBRS[4][0]=6.
    RNBRS[4][1]=8.
    RNBRS[4][2]=8.
    RNBRS[4][3]=6.

    CS[0][0]= 4
    CS[1][0]= 8
    CS[2][0]=12
    CS[3][0]=12
    CS[4][0]=16
    CS[0][1]= 4
    CS[1][1]= 8
    CS[2][1]=12
    CS[3][1]=12
    CS[4][1]=12
    CS[0][2]= 8
    CS[1][2]=12
    CS[2][2]=16
    CS[3][2]=16
    CS[4][2]=16
    CS[0][3]=40
    CS[1][3]=56
    CS[2][3]=80
    CS[3][3]=80
    CS[4][3]=88
    CS[0][4]=24
    CS[1][4]=40
    CS[2][4]=56
    CS[3][4]=56
    CS[4][4]=64
    CS[0][5]= 8
    CS[1][5]=16
    CS[2][5]=24
    CS[3][5]=24
    CS[4][5]=24
    CS[0][6]=12
    CS[1][6]=24
    CS[2][6]=24
    CS[3][6]=36
    CS[4][6]=36
    CS[0][7]=24
    CS[1][7]=48
    CS[2][7]=48
    CS[3][7]=72
    CS[4][7]=72
    CS[0][8]= 1
    CS[1][8]= 2
    CS[2][8]= 2
    CS[3][8]= 3
    CS[4][8]= 3
    CS[0][9]=12
    CS[1][9]=20
    CS[2][9]=28
    CS[3][9]=28
    CS[4][9]=32

    for I in range(1,101):
        SHWDT[I-1]=0.
        THKPCK[I-1]=0.

    ''' BBLARM is used to transmit a warning to the designer via the panel '''

    BBLARM=False
    ALARM='                                                  '

    DCORN = DCORNI*1000.
    BSTEP = BSTEPI*1000.
    PLIMB = PLIMBI*1000.
    HLIMB = HLIMBI*1000.
    BPLMAX= BPLMAI*1000.
    FHD = FHDI*1000.
    if(BBMECH):
        RLAPS = RLAPSI*1000.
        DEWB = DEWBI*1000.
        DIWB = DIWBI*1000.
        
    ''' Estimate the core mass '''

    RMCORE=2.27E-5*(PLIMB+0.75*HLIMB+0.49*DCORN)*DCORN**2

    ''' Calculate the forces '''

    FFRF=6670.
    if(ifLPMT == 2): FFRF=13330.

    FAX=((3*RMWBL+2*RMCORE)*GFORCE+3*FAF)/3.+(FHD*FFRF)
    FTL=(RMCORE*GFORCE*ACCLN)
    FTV=(RMCORE*GFORCE*ACCVE)

    ''' Case definition '''

    for I in range(1,6):
        if((RMAF[I-1][ifLPMT-1]) >= FAX) and (RMLF[I-1] >=FTL) and (RMVF[I-1] >=FTV): break

    else:
        ''' WRITE(*,'(1X,//,1X,''Impossible to define a loading case:'',
         &       //,1X,''Axial Force        ='',F8.0,'' N'',
         &        /,1X,''Longitudinal Force ='',F8.0,'' N'',
         &        /,1X,''Vertical Force     ='',F8.0,'' N'')')
         &       FAX,FTL,FTV '''
        BBLARM= True
        ALARM='Acceleration forces exceeded. Cannot proceed.'
        return

    while(DCORN >CDR[I-1][1]):
        I=I+1
        
    else:
        if (DCORN < CDR[I-1][0]):
            ''' WRITE(*,'(1X,//,1X,''The Core Diameter is smaller than '',
            ''the minimum defined for case '',I1)')I '''
            BBLARM= True
            ALARM='Acceleration forces need a larger core diameter.'
            return 


    ICASE=I
    ''' WRITE(*,'(1X,//,1X,''----> FIRST CHOICE, CASE='',I1)')ICASE '''

    ''' Calculate the Flitch Plate geometry '''

    temp=True
    while(temp):
        temp=False
        BFP=60.*CS[ICASE-1][8]+4.*(CS[ICASE-1][8]-1)

        ''' Estimate CM.TK '''

        CM.TK=(numpy.sqrt((DCORN/2.)**2-(BFP/2.)**2)-15.)*2.

        ''' Calculate the Core geometry '''

        BBLARM,ALARM=OPTIM(DCORN,CM.TK,TCORST,RNK,PLIMB,HLIMB,FHD,ETA,BSTEP,BPLMAX)

        if (BBLARM):
            return

        ''' Load case verification '''

        if (BBMECH):
            AD=4.
            RMY=0.2
            ANGI=25.*numpy.pi/180.
            ANGO=45.*numpy.pi/180.
            SINI=numpy.sin(ANGI)
            SINO=numpy.sin(ANGO)
            COSI=numpy.cos(ANGI)
            COSO=numpy.cos(ANGO)
            FBUP1=182000.
            FBUP2=279600.
            FBYP1=121000.
            FBYP2=186000.
            STOT=(RLAPS/numpy.sqrt(2.))*2.
            if (BBSTLP): STOT=(10./6.)*(RLAPS/numpy.sqrt(2.))
            RLFCT=1.5

            tempacc=True
            while(tempacc):
                tempacc=False
                FMYLY=3.*FAF*RLFCT
                RNS=(CM.TK-RNK*AD)/(2.*TCORST)
                FYB=(FMYLY*CM.BSMIN)/(2.*SQRT(2.)*RMY*STOT*RNS)
                RNI=(FYB/COSI)/FBYP1
                RNO=(FYB/COSO)/FBYP1

                temp1=True
                while(temp1):
                    temp1=False
                    for XI in range(2,7,2):
                        if (RNI<=XI):
                            RNI=XI
                            break

                    for XI in range(4,9,2):
                        if (RNO <= XI):
                            RNO=XI
                            break

                    FU=FYB/(RNI*COSI)
                    FL=(RMCORE*GFORCE/2.+FU*(RNO*SINO-
                                 RNI*SINI))/(RNO*SINO-RNI*SINI)
                    if (FL > FBYP1):
                        if (RNI == 6 and RNO == 8.):
                            if (FL <= FBYP2):
                                FBYP=FBYP2
                                FBUP=FBUP2
                            else:
                                ''' WRITE(*,'(1X,//,1X,''The Yoke Bolts will not stand the active forces'')') '''
                                BBLARM=True
                                ALARM='The Yoke Bolts not up to the active forces'
                                return
                        else:        
                            FBYP=FBYP1
                            FBUP=FBUP1
                            RNI=RNI+2.
                            RNO=RNO+2.
                            temp1=True
                    else:
                        FBYP=FBYP1
                        FBUP=FBUP1

                FYBUN=2.*((FL*RNO*SINO+FU*RNI*SINI)-
                      (FU*RNO*SINO+FL*RNI*SINI))
                FMYU=(FU*RNO*COSO+FU*RNI*COSI)*2.*RMY
                FMYL=(FL*RNO*COSO+FL*RNI*COSI)*2.*RMY
                RNR=(FTL-FMYU-FMYL)/(FBUP*2.*SINO)*1.1
                for XI in range(2,9,2):
                    if (RNR <= XI):break
                else:
                    ''' WRITE(*,'(1X,//,1X,''The core needs more than 8 retaining bolts'')') '''
                    BBLARM=True
                    ALARM='The core needs more than 8 retaining bolts'
                    return

                RNR=XI
                FLC=FYBUN+FMYU+FMYL
                SAFETY=FLC/(RMCORE*GFORCE)

                if (SAFETY < 1.6):
                    ''' WRITE(*,'(1X,//,1X,''Warning: The Safety Factor for lifting ='',F4.2)')SAFETY '''

                BK=CM.TK-2.*CM.RLK1
                AWB=0.25*PI*(DEWB**2-DIWB**2)
                AWBY=0.5*(DEWB-DIWB)*BK
                X1=(4.*AWBY)/(3.*AWB)
                FAVYB=2.*((FBYP*RNO*SINO+FBYP*RNI*SINI)-
                    (FU*RNO*SINO+FL*RNI*SINI))
                FAMYU=2.*RMY*(FU*RNO*COSO+FBYP*RNI*COSI)
                FAMYL=2.*RMY*(FBYP*RNO*COSO+FL*RNI*COSI)
                FAT=FAVYB+FAMYU+FAMYL
                FCORE=RMCORE*GFORCE
                FWBY=RMWBL*GFORCE*X1
                FAFY=3.*FAF*X1
                FLYT=FCORE+FWBY+FAFY
                SAFETY=FAT/FLYT

                if (SAFETY <=1.2):
                    ''' WRITE(*,'(1X,//,1X,''Warning: The Safety Factor for PRESTRESSING ='',F4.2)')SAFETY '''

                FLITO=FCORE+FWBY
                SAFETY=FLC/FLITO

                if (SAFETY <= 1.6):
                    ''' WRITE(*,'(1X,//,1X,''Warning: The Safety Factor for LifTING with PRESTRESSING ='',
                 &    F4.2)')SAFETY '''

                FDIRV=FYBUN+2.*(FBUP-FL)*RNO*SINO
                FSTAT=FMYU+FMYL
                FDYNV=RNO*2.*RMY*(FBUP-FL)*COSO
                ACCVEA=(FDIRV+FSTAT+FDYNV)/FCORE
                if (ACCVE > ACCVEA):
                    RLFCT=RLFCT+0.1
                    ''' WRITE(*,'(1X,//,1X,''Recalculating due to Vertical Acceleration.'')') '''
                    tempacc=True
                    continue

                FDIRL=2.*FBUP*RNR*SINO
                FDYNL=2.*RMY*FBUP*RNR*COSO
                ACCLNA=(FDIRL+FSTAT+FDYNL)/FCORE
                if (ACCLN > ACCLNA):
                    RLFCT=RLFCT+0.1
                    ''' WRITE(*,'(1X,//,1X,''Recalculating due to Longitudinal Acceleration.'')') '''
                    tempacc=True
                    continue

                FCOMB1=numpy.sqrt((FDIRV+FSTAT+FDYNV)**2+(FDIRL+FDYNL)**2)
                FCOMB2=numpy.sqrt((FDIRV+FDYNV)**2+(FDIRL+FSTAT+FDYNL)**2)
                FCOMB=min(FCOMB1,FCOMB2)
                ACCCA=FCOMB/FCORE
                ACCCMB=numpy.sqrt(ACCVE**2+ACCLN**2)
                if (ACCCMB > ACCCA):
                    RLFCT=RLFCT+0.1
                    ''' WRITE(*,'(1X,//,1X,''Recalculating due to Combined Acceleration.'')') '''
                    tempacc=True
                    continue

            FFP=1.1*(FYBUN/3.+FAF)+1.4*RMAP*GFORCE/3.
            for XI in range(1,4):
                if (FFP <= (TFP[ifIX[XI-1]][ifLPMT-1]-(FHD*FFRF))): break
 
            else:
                ''' WRITE(*,'(1X,//,1X,''The core needs more than 3 Flitch Plates'')') '''
                BBLARM= True
                ALARM='The core needs more than 3 Flitch Plates'
                return

            ''' Report Number of flitch plates/limb and side '''

            RNFLPL=XI*1.
            for I in range(1,6):
               if (RNI <= RNBRS[I-1][0] and RNO <= RNBRS[I-1][1] and RNR <= RNBRS[I-1][2] and
                   RNFLPL <= RNBRS[I-1][3]): break
            else:
                ''' WRITE(*,'(1X,//,1X,''Impossible to define a loading case'',
                 &       //,1X,''Number of Inner Yoke Bolts     ='',F3.0,
                 &        /,1X,''Number of Outer Yoke Bolts     ='',F3.0,
                 &        /,1X,''Number of Retaining Yoke Bolts ='',F3.0,
                 &        /,1X,''Number of Flitch Plates        ='',F3.0)')
                 &        RNI,RNO,RNR,RNFLPL '''
                BBLARM= True
                ALARM='Loading case problem. (Yoke bolts & Flitch Plates)'
                return

            if (I > ICASE):
                ''' WRITE(*,'(1X,//,1X,''-> SECOND CHOICE, CASE='',I1)')ICASE '''
                if (CS[ICASE-1][8]!= CS[I-1][8]):
                   ICASE=I
                   temp=True
                   continue
                ICASE=I

    ACORE  = CM.ARE/1.E6
    RMLMB  = RMLIMB
    RMYK   = RMYOKE
    RMCRNR = RMCORN

    RMXWDT = 0.
    RMNWDT = 5000.
    TKO = 0.
       
    for I in range(1,CM.NPKTS+1):
        NSHT [I-1]  = round(RNS1[I-1])
        SHWDT[I-1]  = SW[I-1]/1000.
        THKPCK[I-1] = TPKT[I-1]/1000.
        TKO = TKO + THKPCK[I-1]
        if (RMXWDT < SHWDT[I-1]): RMXWDT = SHWDT[I-1]
        if (RMNWDT > SHWDT[I-1]): RMNWDT = SHWDT[I-1]

    HYOKE = RMXWDT
    HCORE = HLIMBI + 2.*HYOKE
    TKO = 2.* TKO + RNK*(AD/1000.)
    NPACK = CM.NPKTS

    return (ACORE,RMLMB,RMYK,
           RMCRNR,NPACK,NSHT,SHWDT,THKPCK,RMXWDT,RMNWDT,HYOKE,
           HCORE,TKO,RNFLPL,BBLARM,ALARM)
