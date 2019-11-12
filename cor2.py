
''' Title:  Calculation of side-limb cores '''
from drag1 import DRAG1
from ncool import NCOOL
from precor import PRECOR
from core2 import CORE2

def COR2(BLIMB,BMAXPU,CORBND,DCORE,DOUTW,DPHSL,FEXTV,
         FNEXTV,FREQ,GACTP,HLIMB,ILACK,JFC,KCOOL,
         KCORE,NPHAS,PLIMB,PLSL,QFINAL,TTOILM,
         TTOILC,TWSUP,TYPCOR,YHADD,CORESE,
         BBSTLA,ISTGRD,NCOOLI):


    BBFALS=False
    FACTOR=1.E+3
    TASEC=0
    NCOOLW=0
    COM=[0. for i in range(110)]
    RNP =[0. for i in range(110)]
    B2=[0. for i in range(110)]
    B3=[0. for i in range(110)]
    RK1=[0. for i in range(110)]
    RK2=[0. for i in range(110)]
    TS=[0. for i in range(110)]
    B1=[0. for i in range(111)]
    TP=[0. for i in range(111)]

    KBAND=1
    if(HLIMB >4): KBAND=2
    if(CORBND[0] =='S'): KBAND=2
    if(KCORE == 1 or KCORE ==6): KBAND=0
    COM[96]=KBAND

    ''' Choose calculation based on core type '''

    ''' KCORE not equal to 4 '''

    if(KCORE != 4):
        COM[6]=5.
        COM[33]=24.
        if(ISTGRD == 3): COM[33]=32.
        if(ISTGRD == 4): COM[33]=32.

        ''' Calculate flitch plates '''

        (RDRAG,BDRAG,TDRAG,ALT,
         BEL,PRMAX)=DRAG1(TYPCOR,QFINAL/FACTOR,GACTP)

        ''' Calculate flitch plates '''

        ''' Repeat until PRMAX.LT.0.01 '''

        while(PRMAX >= 0.01):
            QFINAL=PRMAX*0.999E+3
            ''' WRITE(*  ,80) QFINAL/1.E+6 '''
            ''' WRITE(JFC,80) QFINAL/1.E+6 '''

            ''' Calculate flitch plates '''

            (RDRAG,BDRAG,TDRAG,ALT,
             BEL,PRMAX)=DRAG1(TYPCOR,QFINAL/FACTOR,GACTP)
  
        ''' KCORE.EQ.4 '''

    else:
        TEMP=TTOILM+20.
        if(KCOOL == 3): TEMP=10.+TTOILM
        if(TTOILC > 0.1): TEMP=30.+TTOILC
        NCOOLW=NCOOL(CORESE,TYPCOR,DCORE,TEMP,BLIMB*BMAXPU,FREQ,
                     BBSTLA,JFC,ISTGRD)
        if(NCOOLI < 0):NCOOLC = NCOOLW
        else:NCOOLC = NCOOLI

        T1=0.
        TKAN=0.
        if(TYPCOR > 6.): TKAN=6.

        ''' Indata to CORE '''

        (DN,B1MAX,B1MIN,BT,TT,RDRAG,BDRAG,
         TDRAG)=PRECOR(round(DCORE*FACTOR),round(HLIMB*FACTOR),KCORE,
                       0.8,T1,T2,BBFALS,KBAND,2000.,10.,TYPCOR,TKAN)

        TASEC=T1/FACTOR
        COM[6]=4.
        COM[7]=NCOOLC
        COM[8]=round(YHADD*FACTOR)
        COM[10]=DN
        COM[11]=B1MIN
        COM[12]=B1MAX
        COM[33]=24.
        if(ISTGRD == 3 ): COM[33]=32.
        if(ISTGRD == 4 ): COM[33]=32.

    ''' LTB & TCA-cores '''

    COM[0]=1.
    COM[1]=round(TYPCOR)
    COM[2]=round(DCORE*FACTOR)
    COM[3]=round(PLIMB*FACTOR)
    COM[4]=round(PLSL*FACTOR)
    COM[5]=round(HLIMB*FACTOR)
    COM[13]=FEXTV
    COM[14]=ILACK
    COM[15]=1.732
    COM[20]=ALT
    COM[21]=round(TWSUP*FACTOR)
    COM[32]=10.
    COM[35]=RDRAG
    COM[36]=BDRAG
    COM[37]=TDRAG
    COM[40]=6.
    COM[42]=FNEXTV
    TJPL=0.3
    if(ISTGRD == 3 ): TJPL=0.23
    if(ISTGRD == 4 ): TJPL=0.23
    COM[41]=TJPL*COM[42]
    COM[47]=0.
    COM[70]=0.
    COM[94]=0.8
    COM[98]=0.

    ''' Calculate the core section '''

    COM,RNP,B1,B2,B3,RK1,RK2,TP,TS=CORE2(COM,RNP,B1,B2,B3,RK1,RK2,TP,TS)
    DKSL=COM[49]/FACTOR
    PLSL=(DOUTW+DKSL)/2.+DPHSL+TASEC
    COM[4]=round(PLSL*FACTOR)

    ''' Calculate the core section '''

    COM,RNP,B1,B2,B3,RK1,RK2,TP,TS=CORE2(COM,RNP,B1,B2,B3,RK1,RK2,TP,TS)
    NPKT=round(COM[52])

    ''' Calculate the proportion of varnished laminations '''
    ''' This is always zero as we no longer use varnished core steel '''

    ''' LANDEL(TYPCOR,round(DCORE*FACTOR),ILACK,NPKT,B1,TP,ANDEL) '''
    ANDEL=0.

    UTURN0=COM[43]
    U0=UTURN0*FREQ/50.
    ACORE=COM[45]/1.E+4
    RLYOKE=COM[92]/FACTOR
    HYOKE=COM[90]/FACTOR
    GYOKE=RLYOKE*FACTOR*COM[56]+COM[57]
    TASEC=COM[70]/FACTOR
    TCORE=COM[91]/FACTOR
    SBF=COM[75]
    GLIMBM=COM[76]
    GLIMBY=COM[77]
    GCORN=COM[89]
    NCOOLC=COM[86]
    YOKAMP=COM[46]
    BDRAG=BDRAG/FACTOR
    TDRAG=TDRAG/FACTOR

    return (PLSL,QFINAL,ACORE,ANDEL,BDRAG,DKSL,GCORN,GLIMBM,GLIMBY,
         GYOKE,HYOKE,KBAND,NCOOLC,RDRAG,RLYOKE,SBF,
         TASEC,TCORE,TDRAG,U0,YOKAMP,NCOOLW)
    ''' 80  FORMAT('0',70('=')/'0',' Assy press reduced to',
     &        F8.2,' MN'/'0',70('='))
       END '''
