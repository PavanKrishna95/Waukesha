from cost import COST
def CCLLE(BBPRNT,JFC,NCOND,NGATE,GS31,GS32,GG32,EFKV):
    
    IHLP=[72, 63, 65, 67]
    SP1='       '
    SP='          '

    if(BBPRNT):
        #WRITE(JFC,*) '===== INPUT DATA TO CCLLE                    ====='
        #WRITE(JFC,*) SP1,'NCOND ',SP,'NGATE ',SP,'GS31 ',SP,'GS32 '
        #WRITE(JFC,*) NCOND,NGATE,GS31,GS32
        #WRITE(JFC,*) SP1,'GG32  ',SP,'EFKV  '
        #WRITE(JFC,*) GG32,EFKV
        pass

    for I in range(1,5):
        if((GS31[I-1]<= 1.E-5)): continue
        IX=69+NCOND[I-1]
        COST (4,IX,167+I ,GS31[I-1],1.,1.,0.,1.,GS31[I-1],1.,1.,1.)

    COST (3,0,172,0.,1.,1.,0.,1.,1.,1.,1.,1.)


    for I in range(1,5):
        if(not(GS32[I-1]<= 1.E-4)):continue
        IX=IHLP[I-1] +NGATE[I-1]
        COST(4,IX,172+I,GS32[I-1],1.,1.,GG32[I-1],1.,GS32[I-1]+GG32[I-1],1., 1., 1.  )

    COST (3,0,177,0.,1.,1.,0.,1.,1.,1.,1.,1.)

    for I in range(1,5):
        GS3 = GS31[I-1] + GS32[I-1] + GG32[I-1]
        COST(4,75,178,0.,1.,1.,0.,1.,EFKV[I-1],GS3,1.,1.)

    COST (3,0,178,0.,1.,1.,0.,1.,1.,1.,1.,1.)
    COST (2,0,179,0.,1.,1.,0.,1.,1.,1.,1.,1.)    

