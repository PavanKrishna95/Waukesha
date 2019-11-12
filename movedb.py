from ukpk import UKPK
def MOVEDB():
    import com as C
    import cominp as CI
    import common as CM

    U1=[0. for i in range(4)]
    U2=[0. for i in range(4)]
    U3=[0. for i in range(4)]
    UX12=[0. for i in range(4)]
    UX13=[0. for i in range(4)]
    UX23=[0. for i in range(4)]
    UR12=[0. for i in range(4)]
    UR13=[0. for i in range(4)]
    UR23=[0. for i in range(4)]
    '''
    C... Declarations
    *
    CC*SBBL Start of the declarations block.
    
       REAL           RES79 (241,6)
       COMMON/KONSRE/ RES79

       include'com1.h'

       include'cominp.h'

       EQUIVALENCE
     &  (XZ0651(1)    ,  ACONDX (1)    ),
     &  (XZ0701(1)    ,  CURDEX (1)    ),
     &  (XZ0731(1)    ,  CURRUT (1)    ),
     &  (XZ0791(1)    ,  FILLFX (1)    ),
     &  (XZ1001(1)    ,  RRWDGX (1)    )
       EQUIVALENCE
     &  (XZ1041(1)    ,  STRWMX (1)    ),
     &  (XZ1051(1)    ,  STRWPX (1)    ),
     &  (XZ1191(1)    ,  ZWIND  (1)    ),
     &  (XZ1393       ,  BBVFRX        )
       EQUIVALENCE
     &  (XZ1407       ,  BMAXPU        ),
     &  (XZ1410       ,  BTANKX        ),
     &  (XZ1414       ,  CLOSSX        ),
     &  (XZ1415       ,  COSTX         ),
     &  (XZ1422       ,  CTROVX        )
       EQUIVALENCE
     &  (XZ1426       ,  DCOREX        ),
     &  (XZ1466       ,  GTRPX         ),
     &  (XZ1472       ,  HLIMBX        ),
     &  (XZ1474       ,  HTANKX        ),
     &  (XZ1508       ,  NWILI         )
       EQUIVALENCE
     &  (XZ1509       ,  NWOULI        ),
     &  (XZ1515       ,  PLIMB         ),
     &  (XZ1528       ,  RLTANX        ),
     &  (XZ1624       ,  MNLX          ),
     &  (XZ1632(1)    ,  RUBCH  (1)    ),
     &  (XZ1650(1)    ,  P00X   (1)    ),
     &  (XZ1686(1)    ,  SOUNDX( 1)    )
       EQUIVALENCE
     &  (XZ2245(1)    ,  WLOSEX (1)    ),
     &  (XZ2254(1)    ,  WLOSRX (1)    )

       REAL      ACONDX(9),CURDEX(9),FILLFX(9),P00(3),P00X(3),
     &           CURRUT(9),SOUND0(3),SOUNDX(3),RRWDGX(9),ZWIND(9),
     &           STRWMM(9),STRWMP(9),WLOSSR(9),WLOSSE(9),
     &           STRWMX(9),STRWPX(9),WLOSRX(9),WLOSEX(9),
     &           U1(4),U2(4),U3(4),UX12(4),UX13(4),UX23(4),
     &           UR12(4),UR13(4),UR23(4),BMAXPU,BTANKX,
     &           CLOSSX,CMANUF,COSTX,CRAZY,CS,CTROVX,DCOREX,GTRPX,
     &           HLIMBX,HTANKX,PLIMBX,PLIMB,RLTANX,TEST
*
       intEGER   I,IWDG,ND,NWILI,NWOULI
*
       DIMENSION RUBCH(15)
       CHARACTER MNLX*8,RUBCH*4,CURNCY*4
*
       LOGICAL   BBVFRX
*
       DATA CRAZY/1.e-20/
*
CC*SEBL End of the declarations block.
'''
    ''' C... Local function '''

    ''' SBBL Start of the function block '''
    
    CRAZY=1.e-20
    CS=CM.RES79[240][2]+CM.RES79[240][4]+CM.RES79[240][5]
    
    P00=[0 for i in range(3)]
    CMANUF=CS

    ''' SEBL End of the function block '''

    ''' Rewind binaryfile 04. '''

    ''' REWIND(04) '''
    CURNCY=C.RUBCH[13]

    '''Initialisations '''
    SOUND0=[0 for i in range(4)]
    for I in range(1,4):
        SOUND0[I-1]=CRAZY
        if (C.BBVFR): SOUND0[I-1]=C.SOUND0[I-1]
    print('BBVFR',C.BBVFR)
    if (not C.BBVFR): SOUND0[0]=C.SOUND0[0]

    C.HLIMB=1.E+3*C.HLIMB
    C.DCORE=1.E+3*C.DCORE

    ''' For each winding '''

    for IWDG in range(1,C.NWILI+1):
        C.FILLF[IWDG-1]=C.FILLF[IWDG-1]
        CI.BWIND[IWDG-1]=1.E+3*C.RRWDG[IWDG-1]
        C.ACOND[IWDG-1]=1.E+6*C.ACOND[IWDG-1]
        CI.CURD0[IWDG-1]=C.CURRUT[IWDG-1]/C.ACOND[IWDG-1]/1.E+6
        C.WLOSSR[IWDG-1]=C.WLOSSR[IWDG-1]/1.E+3
        C.WLOSSE[IWDG-1]=C.WLOSSE[IWDG-1]/1.E+3
        C.STRWMP[IWDG-1]=C.STRWMP[IWDG-1]/1.E+6
        C.STRWMM[IWDG-1]=abs(C.STRWMM[IWDG-1])/1.E+6
        C.BDUCT[IWDG-1]=C.BDUCT[IWDG-1]*1000
        C.RRWDG[IWDG-1]=C.RRWDG[IWDG-1]*1000

    ''' Output variables '''
    ''' CALL CMOVD(IDENT ,'ID ', 1,40) '''
    C.PLIMB=1.E+3*C.PLIMB
    if (C.NWOULI==1):C.PLIMB=0.
    print(' ------- OUTPUT ------- ')
    print('LIMB PITCH=',C.PLIMB)
    print('LIMB HEIGHT',C.HLIMB)
    print(' CORE DIAMETER',C.DCORE)
    print(' DUCT WIDTH =',C.BDUCT[:C.NWILI])

    print('Winding Width=',C.RRWDG[:C.NWILI])
    print('Limb Flux density=',CI.BLIMB)
    print('Conductor Area=',C.ACOND[:C.NWILI])
    print('Spacef=',C.FILLF[:C.NWILI])
    print('STR+ =',C.STRWMP[:C.NWILI])
    print('STR- =',C.STRWMM[:C.NWILI])
    print('RII=',C.WLOSSR[:C.NWILI])
    print('EDDY=',C.WLOSSE[:C.NWILI])
    print('SOUND0=',SOUND0[0])    
    
    '''CALL RMOVD(PLIMBX ,'X55 ',1,6,0)

    SOFF Switch OFF structure analyser (Not all calls need be shown) 
    
    CALL RMOVD(SOUND0(1)  ,'X56 ',1,6,1)
    CALL RMOVD(SOUND0(2)  ,'X57 ',1,6,1)
    CALL RMOVD(SOUND0(3)  ,'X58 ',1,6,1)

    CALL RMOVD(ZWIND ,'Y*7 ' ,NWILI,6,1)
    CALL RMOVD(STRWMP,'Y*8 ' ,NWILI,4,0)
    CALL RMOVD(STRWMM,'Y*9 ' ,NWILI,4,0)
    CALL RMOVD(WLOSSR,'Y*10 ',NWILI,5,1)
    CALL RMOVD(WLOSSE,'Y*11 ',NWILI,5,1)'''

    ''' SON  Switch ON  structure analyser (Not all calls need be shown)

    Voltage reactances and losses '''

    U1,U2,U3,UX12,UX13,UX23,UR12,UR13,UR23=UKPK(U1,U2,U3,UX12,UX13,UX23,UR12,UR13,UR23)

    ''' For each tap '''

    for I in range(0,3):
        if (U1[I]<0.0001)  : U1[I]  = CRAZY
        if (U2[I]<0.0001)  : U2[I]  = CRAZY
        if (U3[I]<0.0001)  : U3[I]  = CRAZY
        if (UX12[I]<0.0001): UX12[I]= CRAZY
        if (UX13[I]<0.0001): UX13[I]= CRAZY
        if (UX23[I]<0.0001): UX23[I]= CRAZY
        if (UR12[I]<0.0001): UR12[I]= CRAZY
        if (UR13[I]<0.0001): UR13[I]= CRAZY
        if (UR23[I]<0.0001): UR23[I]= CRAZY

    ''' For each tap '''

    for I in range(1,4):
        P00[I-1]=CRAZY
        if (C.BBVFR):P00[I-1]=C.P00[I-1]/1.E+3
    if (not C.BBVFR):P00[0]=C.P00[0]/1.E+3

    ''' SOFF Switch OFF structure analyser (Not all calls need be shown) '''

    
    print('U1=',U1)
    print('U2=',U2)
    print('U3=',U3)

    print('X1-2',UX12)
    print('X1-3',UX13)
    print('X2-3',UX23)
    print('Pk1-2',UR12)
    print('PK1-3',UR13)
    print('Pk2-3',UR23)
       
    print('PoSSES',P00[0] ) 

    ''' Tank dimensions & costs '''

    C.BTANK=1.E+3*C.BTANK
    C.RLTANK=1.E+3*C.RLTANK
    C.HTANK=1.E+3*C.HTANK
    print('TANK W =',C.BTANK)
    print('TANK L =',C.RLTANK)
    print('TANK H =',C.HTANK)
    
    ''' SON  Switch ON  structure analyser (Not all calls need be shown)

        Write on binaryfile the resultmatrix from OPTSUB.

        WRITE(04) RES79

        RETURN
        END '''
