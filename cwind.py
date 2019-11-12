from goto import with_goto
from cost import COST

@with_goto
def CWIND(BBPRNT,JFC,NUMBER,NCOND,LTYPE,RGUID,GS11,\
                   GS121,GS122,GS131,GS132,GS133,GS134,\
                   GN1351,GN1352,GS136,APART,TCOV1,TCOV2,\
                   CCOV1,CCOV2,NLIMB,DWIND,WWIND,WCLS,WDUCT,\
                   NTAPP,ACOND,XBUNCH,ABUNCH,ZCOOL,NOUCO,\
                   ZPART,BBEXAC,BPART,ZCABEL,ZCOIAR,ZLAG,BBLNX,\
                   RPRTRR,ZWIND,IPISOL,HPART,CBUNCH,CONVAR,TCEPOX):
    import common as CM
    SP1='       '
    SP='          '
    IX=19*(NUMBER-1)
    XTAPP=0
    if( BBPRNT):
        #WRITE(JFC,*) '===== INPUT DATA TO C#WIND ====='
        #WRITE(JFC,*) SP1,'NUMBER',SP,'NCOND ',SP,'LTYPE ',SP,'RGUID '
        #WRITE(JFC,*) NUMBER,NCOND,LTYPE,RGUID
        #WRITE(JFC,*) SP1,'GS11  ',SP,'GS121 ',SP,'GS122 ',SP,'GS131 '
        #WRITE(JFC,*) GS11,GS121,GS122,GS131
        #WRITE(JFC,*) SP1,'GS132 ',SP,'GS133 ',SP,'GS134 ',SP,'GN1351'
        #WRITE(JFC,*) GS132,GS133,GS134,GN1351
        #WRITE(JFC,*) SP1,'GN1352',SP,'GS136 ',SP,'APART ',SP,'TCOV1 '
        #WRITE(JFC,*) GN1352,GS136,APART,TCOV1
        #WRITE(JFC,*) SP1,'TCON2 ',SP,'CCOV1 ',SP,'CCOV2 ',SP,'NLIMB '
        #WRITE(JFC,*) TCOV2,CCOV1,CCOV2,NLIMB
        #WRITE(JFC,*) SP1,'D#WIND ',SP,'#W#WIND ',SP,'#WCLS  ',SP,'#WDUCT '
        #WRITE(JFC,*) D#WIND,#W#WIND,#WCLS,#WDUCT
        #WRITE(JFC,*) SP1,'NTAPP ',SP,'ACOND ',SP,'XBUNCH',SP,'ABUNCH'
        #WRITE(JFC,*) NTAPP,ACOND,XBUNCH,ABUNCH
        #WRITE(JFC,*) SP1,'ZCOOL ',SP,'NOUCO ',SP,'ZPART ',SP,'BBEXAC'
        #WRITE(JFC,*) ZCOOL,NOUCO,ZPART,BBEXAC
        #WRITE(JFC,*) SP1,'BPART ',SP,'ZCABEL',SP,'ZCOIAR',SP,'ZLAG  '
        #WRITE(JFC,*) BPART,ZCABEL,ZCOIAR,ZLAG
        #WRITE(JFC,*) SP1,'BBLNX ',SP,'RPRTRR',SP,'Z#WIND ',SP,'IPISOL'
        #WRITE(JFC,*) BBLNX,RPRTRR,Z#WIND,IPISOL
        #WRITE(JFC,*) SP1,'HPART ',SP,'CBUNCH'
        #WRITE(JFC,*) HPART,CBUNCH
        #WRITE(JFC,*) SP1,'CM.LC(1)-CM.LC(4)'
        #WRITE(JFC,*) (CM.LC(I),I=1,4)
        #WRITE(JFC,*) SP1,'CM.LC(5)-CM.LC(8)'
        #WRITE(JFC,*) (CM.LC(I),I=5,8)
        pass

    if(BBEXAC):
        #Setting the correct BLOCK number in cost file.
        if(CONVAR=='YES'):
            CM.LC[0]=24
            if(APART>20): CM.LC[0]=34
        else:
            CM.LC[0]=1
            if(APART>20): CM.LC[0]=2

        CM.LC[1]=3
        if(APART>30): CM.LC[1]=4

        if(TCEPOX=='YES'):
            CM.LC[2]=21
            if(ACOND>300): CM.LC[2]=38
        else:
            CM.LC[2]=5
            if(ACOND>300): CM.LC[2]=6

        CM.LC[3]=10
        if(WWIND>26): CM.LC[3]=11
        CM.LC[4]=0
        HLP=DWIND+WWIND
        if((LTYPE==3 or LTYPE==4) and HLP >=700 and HLP<=1400):
            CM.LC[4]=1

    if(not(LTYPE==8)):
        if(NCOND==1):
            COST (3,CM.LC[0],IX+1,GS11,1.,APART,0.,1.,1.,1.,1.,1.)

        if(NCOND==2):
            COST (3,CM.LC[1],IX+2,GS11,1.,APART,0.,1.,1.,1.,1.,1.)

        if(NCOND==3):
            COST (3,CM.LC[2],IX+3,GS11,1.,ACOND,0.,1.,1.,1.,1.,1.)
            goto ._20

    else:
        if(NCOND==2):
            COST(3,6,IX+2,GS11,1.,BPART,0.,1.,1.,1.,1.,1.)
        COST(3,5,IX+1,GS11,1.,BPART,0.,1.,1.,1.,1.,1.)

    if(0<LTYPE<=7 ):
        IU=7
        if(LTYPE==2 or LTYPE>=6): IU=8

        if(IPISOL==1):
            if(abs(GS121)>= 1.E-6):
                COST (4,IU,IX+4,GS121,1.,1.,0.,1.,GS121,TCOV1,CCOV1,1.)   
            COST (3,IU,IX+4,GS122,1.,1.,0.,1.,GS122,TCOV2,CCOV2,1.)
 
        elif(IPISOL==2 or IPISOL==3):
            COST(4,126+IPISOL,IX+4,GS121,1.,1.,0.,1.,0.,0.,0.,0.)
            COST(3,IU,IX+4,GS122,1.,1.,0.,1.,GS122,TCOV2,CCOV2,1.) 

    elif(LTYPE==8):       
        COST(3,7,IX+4,GS121,1.,TCOV1,0.,1.,GS121,1.,1.,1.)

    elif(LTYPE==9):
        ACM2 = DWIND*3.1416E-3
        ACM4 = 0.38 + 0.37*(RPRTRR-1.)
        COST(4,8,IX+4,GS122,1.,1.,0.,1.,ZWIND,ACM2,ZCABEL,ACM4)
        COST(3,9,IX+4,GS121,1.,1.,0.,1.,1.,1.,1.,1.)

    label ._20
    XLIMB=NLIMB
    GS=GS131/XLIMB
    
    if(LTYPE==1 or LTYPE==3 or LTYPE==4 or LTYPE==5):
        COST (4,17,IX+5,GS131,DWIND,1.,0.,1.,XLIMB,GS,1.,1.)
    
    elif(LTYPE == 2 or LTYPE==6 or LTYPE==7):
        COST (4,18,IX+5,GS131,DWIND,1.,0.,1.,XLIMB,GS,1.,1.)
    
    elif(LTYPE== 8):
        COST(4,11,IX+5,GS131,1.,1.,0.,1.,XLIMB,1.,1.,1.)
        COST(4,23,IX+5,GN1352,1.,1.,0.,1.,1.,1.,1.,1.)
    
    elif(LTYPE==9):
        COST(4,12,IX+5,GS131,1.,1.,0.,1.,1.,1.,1.,1.)
    

    GS=GS132/XLIMB
    if(LTYPE== 1 or LTYPE==3 or LTYPE==4 or LTYPE==5):
        COST (4,9,IX+6,GS132,DWIND,1.,0.,1.,XLIMB,GS,1.,1.)
        
    elif(LTYPE == 2 or 6 or 7):
        COST (4,CM.LC[3],IX+6,GS132,DWIND,1.,0.,1.,XLIMB,GS,1.,1.)
    
    elif(LTYPE== 8 or LTYPE==9):
        GS = GS132+ GS136
        COST(4,13,IX+6,GS,1.,1.,0.,1.,GS,1.,1.,1.)
    
    if(not(abs(GS133)<1.E-6)):
        COST (4,12,IX+7,GS133,1.,1.,0.,1.,GS133,1.,1.,1.)

    if(not(abs(GS134)<1.E-6)):
        if(0<LTYPE<=7):
            COST (4,13,IX+8,GS134,1.,1.,0.,1.,GS134,WCLS,1.,1.)
        elif(LTYPE==8 or LTYPE==9):
            ACM4 = 1. + 10./(ZCOOL+ZCOIAR+XLIMB)
            COST(4,14,IX+8,GS134,1.,1.,0.,1.,ZCOOL,ZCOIAR,XLIMB,ACM4)

    if(0<LTYPE<=7 ):
        COST (4,14,IX+9,GN1351,1.,1.,0.,1.,GN1351,1.,1.,1.)
        COST (4,15,IX+10,GN1352,1.,1.,0.,1.,GN1352,1.,1.,1.)
    
    elif(LTYPE==9):
        COST(4,10,IX+9,GN1351,1.,1.,0.,1.,1.,1.,1.,1.)

    GS=GS136/XLIMB
    if(not(abs(GS136)<1.E-6 or LTYPE>7)):
        COST (4,16,IX+11,GS136,DWIND,1.,0.,1.,XLIMB,GS,1.,1.)

    COST (3,0,IX+12,0.,1.,1.,0.,1.,1.,1.,1.,1.) 
    XCOOLD=ZCOOL+1   

    XOGUR=RGUID/2. * DWIND * 0.0248
    
    if(LTYPE==1):
        IA= 19
        IB= 138
        IC= 25
        ID= 22
            
    elif(LTYPE==2):
        IA= 20
        IB= 139
        IC= 26
        ID= 23
        
    elif(LTYPE==3):
        IA= 19
        IB= 140
        IC= 25
        ID= 22

    elif(LTYPE==4):
        IA= 19
        IB= 140
        IC= 25
        ID= 22

    elif(LTYPE==5):
        IA= 19
        IB= 141
        IC= 27
        ID= 22

    elif(LTYPE==6):
        IA= 19
        IB= 142
        IC= 25
        ID= 23

    elif(LTYPE==7):
        IA= 20
        IB= 143
        IC= 26
        ID= 23

    elif(LTYPE==8):
        COST(3,15,18+IX,0.,0.,0.,0.,1.,XLIMB,1.,1.,1.)
        COST (2,0,19*NUMBER,0.,1.,1.,0.,1.,1.,1.,1.,1.)
        return
    elif(LTYPE==9):
        COST(4,16,15+IX,0.,0.,0.,0.,1.,ZWIND,XLIMB,1.,1.)
        ACM1 = ZLAG - 1
        IY = 17
        if(BBLNX): IY=18
        COST(4,IY,15+IX,0.,0.,0.,0.,1.,ACM1,ZCABEL,XLIMB,ZCOIAR)
        ACM1= RPRTRR -1
        COST(4,19,15+IX,0.,0.,0.,0.,1.,ACM1,ZCABEL,XLIMB,ZCOIAR)
        COST(4,20,14+IX,0.,0.,0.,0.,1.,XTAPP,1.,1.,1.)
        ACM2 = 1. + WDUCT/15
        COST(4,21,13+IX,0.,0.,0.,0.,1.,XLIMB,ACM2,1.,1.)
        ACM2 = 1.+ 1.154/ZCOIAR
        COST(4,22,16+IX,0.,0.,0.,0.,1.,ZCOIAR,ACM2,1.,1.)
        COST(3, 0 ,18+IX,0.,0.,0.,0.,0.,0.,0.,0.,0.)
        COST (2,0,19*NUMBER,0.,1.,1.,0.,1.,1.,1.,1.,1.)
        return
               
    COST (4,IA   ,IX+13,0.,1.,1.,0.,1.,XLIMB,DWIND,WDUCT,1.)
    COST (5,IB,IX+15,0.,1.,1.,0.,1.,XBUNCH,ABUNCH,XCOOLD,1.)
    COST (4,144,IX+15,0.,1.,1.,0.,1.,XOGUR,1.,1.,1.)
    HLP = DWIND + WWIND
    if(CM.LC[5-1]==1):
        COST(4,30,IX+15,0.,1.,1.,0.,1.,XBUNCH,ABUNCH,XCOOLD,1.)
    COST (5,IC   ,IX+16,0.,1.,1.,0.,1.,XLIMB,DWIND,WDUCT,1.)    
    COST (4,28,IX+16,0.,1.,1.,0.,1.,XOGUR,1.,1.,1.)
    XTAPP=NTAPP
    XOUCO=NOUCO
    COST (4,ID,IX+14,0.,1.,1.,0.,1.,XTAPP,ACOND,1.,1.)
    if(abs(XOUCO)< 1.E-6):
        COST (3,0,IX+18,0.,1.,1.,0.,1.,1.,1.,1.,1.)
        COST (2,0,19*NUMBER,0.,1.,1.,0.,1.,1.,1.,1.,1.)
        return
    ZPAR2 = ZPART/2
    COST (4,29,IX+17,0.,1.,1.,0.,1.,XOUCO,ZPAR2,1.,1.)
    COST (3,0,IX+18,0.,1.,1.,0.,1.,1.,1.,1.,1.)
    COST (2,0,19*NUMBER,0.,1.,1.,0.,1.,1.,1.,1.,1.)
    return

