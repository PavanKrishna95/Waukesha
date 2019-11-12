
'''   Title:  Search for a common node for an auto-transformer
              and allocate terminal numbers to each winding '''

def OMF013(NG,NWILI,WNOD1,WNOD2,TNODE,KCON,UNLINE,
           KGROUP,KWIFUN,KCODE):

    ITEST=['M','R','RC','MV','S','R1','R2','RB','RCB']
    IFTYPE=[1   , 2   , 3   , 4   , 5   , 2   , 2   , 2   , 3]
    INDEX =[1,2,3,4 ]

    WNOD=' '
    KHELP=[0 for i in range(9)]
    KGROUP=[0 for i in range(9)]
    KCODE =[0 for i in range(9)]
   
    if not((KCON[0] != 'I/A' and KCON[0]!='Y/A') or
       (KCON[1] != 'I/A' and KCON[1]!='Y/A')):
        for IWDG in range(1,NWILI+1):
            IEND1=0
            IEND2=0
            if(WNOD1[IWDG-1]==TNODE[0] or
               WNOD1[IWDG-1]==TNODE[1]):IEND1=1
            if(WNOD2[IWDG-1]==TNODE[0] or
               WNOD2[IWDG-1]==TNODE[1]):IEND2=1
            for JWDG in range(1,NWILI+1):
                if(JWDG!=IWDG):
                    if not(WNOD1[IWDG-1]!=WNOD1[JWDG-1] and
                       WNOD1[IWDG-1]!=WNOD2[JWDG-1]):
                        IEND1=IEND1+1
                        WNODS1=WNOD1[IWDG-1]
                    if not(WNOD2[IWDG-1]!=WNOD1[JWDG-1] and
                           WNOD2[IWDG-1]!=WNOD2[JWDG-1]):
                        IEND2=IEND2+1
                        WNODS2=WNOD2[IWDG-1]
            if(IEND1==2):WNOD=WNODS1
            if(IEND2==2):WNOD=WNODS2
            if(IEND1==2 or IEND2==2):break

        ''' Sort terminal nodes 1 & 2 so the series winding is treated first '''
        if(UNLINE[1]<UNLINE[0]):pass
        else:
            INDEX[0]=2
            INDEX[1]=1

    NWIT=0
    for IGROUP in range(1,NG+1):
        ITERML=INDEX[IGROUP-1]

        for JWDG in range(1,NWILI+1):
            JJ=JWDG
            if(KGROUP[JWDG-1]!=0):continue
            if(WNOD1[JWDG-1]==TNODE[ITERML-1]):break 
            if(WNOD2[JWDG-1]==TNODE[ITERML-1]):break
        NWIT=1
        KHELP[0]=JJ
        KGROUP[JJ-1]=ITERML
        if(IGROUP==1 and(WNOD1[JJ-1]==WNOD or
                         WNOD2[JJ-1]==WNOD)):continue
        NWNG=NWILI-NG
        for JITEM in range(1,NWNG+1):
            for KWDG in range(1,NWILI+1):
                if(KGROUP[KWDG-1]!=0):continue
                IND=KHELP[JITEM-1]
                KK=KWDG
                if(WNOD1[IND-1]==WNOD1[KWDG-1] or
                   WNOD1[IND-1]==WNOD2[KWDG-1]):
                    NWIT=NWIT+1
                    KHELP[NWIT-1]=KK
                    KGROUP[KK-1]=ITERML
                    break
                
                if(WNOD2[IND-1]==WNOD2[KWDG-1] or
                   WNOD2[IND-1]==WNOD1[KWDG-1]):
                    NWIT=NWIT+1
                    KHELP[NWIT-1]=KK
                    KGROUP[KK-1]=ITERML
                    break
                
            if(NWIT==JITEM):break
            if(IGROUP==1 and(WNOD1[KK-1]==WNOD or
                             WNOD2[KK-1]==WNOD)):break

    for LWDG in range(1,NWILI+1):
        KCODE[LWDG-1]=0
        for JTYPE in range(1,10):
            
            if(KWIFUN[LWDG-1]==ITEST[JTYPE-1]):
                
                KCODE[LWDG-1]=IFTYPE[JTYPE-1]
    print('KGROUP',KGROUP)
    return KGROUP,KCODE
