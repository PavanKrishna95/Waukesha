from fprint import FPRINT
from fbb import FBB
from omf013 import OMF013
def WX146():
    print("START OF WX146")
    import com as C
    import cominp as CI
       
    BB79=None
    KCON1=[0 for i in range(4)]
    KGROUP=[0 for i in range(9)]
    KCODE=[0 for i in range(9)]
    CTAN=""
    
    CRAZY=1.e-20
    TEST2='    '
    CWDG=['A','B','C','D','E','F','G','H','I']
   
    for I in range(1,11):
        C.BBHELP[I]=False
    C.BBERR=False
    KEY3='       1'
    
    C.NWILI=CI.RWILI

#    GET(CI.XSTRRD)

#. Initialise the indata

#*SBBL Start of the initialisation block
#For each winding
    for IWDG in range(1,10):
        if(CI.ACOND0[IWDG-1]==CRAZY):
            CI.ACOND0[IWDG-1]=0
        if(CI.BPART[IWDG-1]==CRAZY):
            CI.BPART[IWDG-1]=0
        if(CI.BWIND[IWDG-1]==CRAZY):
            CI.BWIND[IWDG-1]=0
        if(CI.COVCBL[IWDG-1]==CRAZY):
            CI.COVCBL[IWDG-1]=0
        if(CI.CURD0[IWDG-1]==CRAZY):
            CI.CURD0[IWDG-1]=0
        if(CI.BDUCT[IWDG-1]==CRAZY):
            CI.BDUCT[IWDG-1]=0
        if(CI.DUYOKE[IWDG-1]==CRAZY):
            CI.DUYOKE[IWDG-1]=0
        if(CI.DLYOKE[IWDG-1]==CRAZY):
            CI.DLYOKE[IWDG-1]=0    
        if(CI.FILLF[IWDG-1]==CRAZY):
            CI.FILLF[IWDG-1]=0                            
        if(CI.HPART[IWDG-1]==CRAZY): 
            CI.HPART[IWDG-1]=0
        if(CI.MXCURD[IWDG-1]==CRAZY):
            CI.MXCURD[IWDG-1]=4.5
        if(CI.NCDUCT[IWDG-1]==CRAZY):
            CI.NCDUCT[IWDG-1]=-1
        if(CI.PRESSM[IWDG-1]==CRAZY):
            CI.PRESSM[IWDG-1]=0
        if(CI.TENSM[IWDG-1]==CRAZY):
            CI.TENSM[IWDG-1]=0
        if(CI.XOILGR[IWDG-1]==CRAZY):
            CI.XOILGR[IWDG-1]=-1
        if IWDG <=4:
            if(CI.XREA[IWDG-1]==CRAZY):
                CI.XREA[IWDG-1]=0
        if(CI.XSTRRD[IWDG-1]==CRAZY):
            CI.XSTRRD[IWDG-1]=0
        
    if(CI.BLIMB==CRAZY):  CI.BLIMB=0.
    if(CI.CPUFIX==CRAZY):  CI.CPUFIX=0.
    if(CI.CPUIND==CRAZY):  CI.CPUIND=0.
    if(CI.CPUPT==CRAZY):  CI.CPUPT=0.
    if(CI.DCORE==CRAZY):  CI.DCORE=0.
    if(CI.EVALPK==CRAZY):  CI.EVALPK=0.
    if(CI.EVALP0==CRAZY):  CI.EVALP0=0.
    if(CI.FONAN==CRAZY):  CI.FONAN=0.
    if(CI.HLIMB==CRAZY):  CI.HLIMB=0.
    if(CI.USHORE==CRAZY):  CI.USHORE=0.
    if(CI.BLTOPM==CRAZY):  CI.BLTOPM=0.
    if(CI.BTANK==CRAZY):  CI.BTANK=0.
    if(CI.BTANKM==CRAZY):  CI.BTANKM=0.
    if(CI.CALCT==CRAZY):  CI.CALCT=0.
    if(CI.DCOCOV==CRAZY):  CI.DCOCOV=0.
    if(CI.DLMBMA==CRAZY):  CI.DLMBMA=0.
    if(CI.DLMBMI==CRAZY):  CI.DLMBMI=0.
    if(CI.DPHAS==CRAZY):  CI.DPHAS=0.
    if(CI.DPHSL==CRAZY):  CI.DPHSL=0.
    if(CI.EXTANK==CRAZY):  CI.EXTANK=0.
    if(CI.GTRPM==CRAZY): CI.GTRPM=0
    if(CI.HLIMBM==CRAZY): CI.HLIMBM=0
    if(CI.HLIMBN==CRAZY): CI.HLIMBN=0
    if(CI.HTANK==CRAZY): CI.HTANK=0
    if(CI.HTANKM==CRAZY): CI.HTANKM=0
    if(CI.HYOKAD==CRAZY): CI.HYOKAD=0
    if(CI.LTANK==CRAZY): CI.LTANK=0
    if(CI.MAXPK==CRAZY): CI.MAXPK=0
    if(CI.MAXP0==CRAZY): CI.MAXP0=0
    if(CI.QMONT==CRAZY): CI.QMONT=0
    if(CI.RLTANM==CRAZY): CI.RLTANM=0
    if(CI.SOUNDM==CRAZY): CI.SOUNDM=0
    if(CI.TOPDTO==CRAZY): CI.TOPDTO=0
    if(CI.TTOILM==CRAZY): CI.TTOILM=0
    if(CI.TWINDM==CRAZY): CI.TWINDM=0
    if(CI.UMAXPU==CRAZY): CI.UMAXPU=0
    if(CI.UTURN==CRAZY): CI.UTURN=0
    
    #End of the initialisation block  
         
    # Write indata to vectors : AARR,C.IARR,C.TARR & C.BARR  

    if(C.MNC[1]==' '): C.MNC[1]=TEST2
    C.MNL='        '
    C.MNL=CI.MNLCOD
    
    #Object
    #*SBBL Start of the object block
    # Initialise the Object string
    for I in range(1,1+6):
        C.OBJE[I-1]='  '
    KEY3='  '

    # Read in the object name from the dialog area
#    DMOVC(COBJ,'DSYOBJ ',1,20)
    #for I in range(1,1+5):
     #   C.OBJE[I-1]=COBJ                            #HANDLE FORMAT

    #*SEBL End of the object block
    #CI.IDENTification

#*SBBL Start of the CI.IDENTification block

# Initialise the CI.IDENTification string
        

    for I in range(1,1+18):
        C.IDENTX[I-1]=''

    for I in range(1,1+10):
        C.IDENTX[I-1]=CI.IDENT                         #HANDLE FORMAT

    ''' for I in range(1,1+9):
        C.BBHELP[I-1]=False
    C.BBHELP[10-1]=False '''

#END IF

#SEBL End of the Trace block

    if(CI.MAXP0 > 0): CI.EVALP0=(-1)*CI.MAXP0
    if(CI.MAXPK > 0): CI.EVALPK=(-1)*CI.MAXPK
    C.IARR[0]=CI.NPHAS

#C.IARR(3) = Maximum number of optimisation calculations

    C.IARR[2]=2500
    C.AARR[1]=CI.FREQ
    C.AARR[3]=CI.USHORE
    C.AARR[5]=CI.EVALP0
    C.AARR[6]=CI.EVALPK
    C.TARR[59]=CI.OPERAT
    C.AARR[12]=0
    C.AARR[13]=0

#AARR[24] = Monthly inflation rate for costing purposes    

    C.AARR[24]=1

# AARR[33] = Loss scale factor
    C.AARR[33]=1

#AARR(35) = Cost scale factor    

    C.AARR[35-1]=1

#AARR[59] = Mass-factor  
    C.AARR[59]=1
    
#Determine the No. of terminals    

    ITML=1

#Check upto and including 4 terminals    

#If still less than or equal to 4

    while(ITML<=4):
#Check the terminal data      
# If data has been entered
        if(CI.TNODE[ITML-1]==''):
            break
        C.NG=ITML
        TAPS='NO'
        if(CI.KTYPRW[ITML-1]!='NO'): TAPS='YES'
        KCON1[ITML-1]=CI.KCON[ITML-1]   
        if(CI.KCON[ITML-1]=='YA'): CI.KCON[ITML-1]='Y/A'
        if(CI.KCON[ITML-1]=='IA'): CI.KCON[ITML-1]='I/A'
        if(CI.KCON[ITML-1]=='YN'):  KCON1[ITML-1]='Y'
        if(CI.KCON[ITML-1]=='I/A'): KCON1[ITML-1]='I/AUTO'
        if(CI.KCON[ITML-1]=='Y/A'): KCON1[ITML-1]='Y/AUTO'

        C.AARR[10+ITML-1]=CI.SRATE[ITML-1]
        C.AARR[15+ITML-1]=CI.UNLINE[ITML-1]
        if(ITML<3): C.TARR[5+ITML-1]=TAPS
        C.BBVR[ITML-1]=False
        if(TAPS=='YES'): C.BBVR[ITML-1]=True
#Allocate tapping details    
# If taps    

        if(TAPS=='YES'):
            C.IARR[5+ITML-1]=round(CI.NPSTEP[ITML-1])
            C.IARR[10+ITML-1]=round(CI.NMSTEP[ITML-1])
            C.AARR[20+ITML-1]=CI.PUSTEP[ITML-1]
            C.TARR[10+ITML-1]=CI.KTYPRW[ITML-1]
            C.FARR[52+ITML-1]=CI.CALCT
#IF NO TAPS
        else:
            C.IARR[5+ITML-1]=0
            C.IARR[10+ITML-1]=0
            C.AARR[20+ITML-1]=0
            C.TARR[10+ITML-1]='NO'
            C.FARR[52+ITML-1]=0

        C.TARR[20+ITML-1]=KCON1[ITML-1]
        C.AARR[25+ITML-1]=CI.USURG[ITML-1]
        C.AARR[30+ITML-1]=CI.SLINE[ITML-1]
        ITML=ITML+1 

# Search for a common node for an auto-transformer
# and allocate terminal numbers to each winding           

    KGROUP,KCODE=OMF013(C.NG,C.NWILI,CI.WNOD1,CI.WNOD2,CI.TNODE,CI.KCON,CI.UNLINE,KGROUP,CI.KWIFUN,KCODE)
    print('KGROUP=',KGROUP)
    print('KCODE=',KCODE)
#Automatic CI.LAYOUT specification    

    C.BBLAY=False
    if(CI.LAYOUT[0]=='Y'): C.BBLAY=True
#Allocate winding data    

    YOKDIS=0
    for IWDG in range(1,1+C.NWILI):
        C.WDGFUN[IWDG-1]=CI.KWIFUN[IWDG-1]
        C.IARR[20+IWDG-1]=KGROUP[IWDG-1]
        C.TARR[60+IWDG-1]=CI.CBLTYP[IWDG-1]
        C.TARR[30+IWDG-1]=CI.KWITYP[IWDG-1]
        C.IARR[30+IWDG-1]=KCODE[IWDG-1]
# Allocate current densities, etc.
#optimize
        if(CI.WNDOPT[IWDG-1][0]=='Y'):
            C.AARR[50+IWDG-1]=(-1)*CI.MXCURD[IWDG-1]
            C.AARR[60+IWDG-1]=(-1)*CI.ACOND0[IWDG-1]
#Space factor has not been stated            
            if(CI.FILLF[IWDG-1] < 0.001):
                C.JFC,C.BBERR=FPRINT(2,C.BBERR,'WX146:Space factor is missing for winding :{0}'.format(CWDG[IWDG]))
#WINDING fixed

        else:
            if(CI.ACOND0[IWDG-1] < 10**-8):
                C.AARR[50+IWDG-1]=CI.MXCURD[IWDG-1]
            
            C.AARR[60+IWDG-1]=CI.ACOND0[IWDG-1]
            C.AARR[90+IWDG-1]=CI.BWIND[IWDG-1]    

        C.AARR[70+IWDG-1]=CI.BDUCT[IWDG-1]
        C.AARR[80+IWDG-1]=CI.FILLF[IWDG-1]
        C.AARR[100+IWDG-1]=CI.DUYOKE[IWDG-1]+CI.DLYOKE[IWDG-1]
        if[C.AARR[100+IWDG-1] > YOKDIS-1]: YOKDIS=C.AARR[100+IWDG-1]
        C.DARR[40+IWDG-1]=CI.EXTRAR[IWDG-1]
        C.DARR[50+IWDG-1]=CI.HCLAC[IWDG-1]
     
    NWOULI=3
    if(CI.NPHAS==1): NWOULI=2
    if(CI.CORTYP=='TY-1' and CI.NPHAS==1): NWOULI=3
    if(CI.CORTYP=='EY'): NWOULI=1
    C.IARR[50]=NWOULI   

    #Store the now established No. of wound limbs 
#    PUTR('CORE    ','NWOULI  ',KEY3, FLOAT(NWOULI), 1)        #TBC
    #Sidelimbed core ?
    C.TARR[51-1]='YES'
    if(CI.CORTYP=='T' or CI.CORTYP=='D'): C.TARR[50]='NO'

    C.UARR[21] = CI.CORTYP
    C.TYPCOR=0
    if(CI.CORTYP=='D'): C.TYPCOR=1
    if(CI.CORTYP=='T'): C.TYPCOR=3
    if(CI.CORTYP=='EY'): C.TYPCOR=7
    if(CI.CORTYP=='DY'): C.TYPCOR=8
    if(CI.CORTYP=='TY-1'): C.TYPCOR=9
    if(CI.CORTYP=='TY-3'): C.TYPCOR=10

    C.TYPCOR = round(C.TYPCOR)                    ###
    #Step lap joint in core

    C.UARR[22] = CI.STEPLA

    C.AARR[140]=CI.DPHAS
    C.AARR[141]=CI.DPHSL
    C.BARR[30]=CI.QMONT
    C.BARR[29]=CI.TWSUP
    C.AARR[142]=CI.DCORE
    C.AARR[145]=CI.BLIMB
    # EPS Optimisation constant
    C.BARR[31]=0
    
    #FEPS Optimisation constant
    C.BARR[32]=-1 

    # DRV Optimisation constant
    C.BARR[33]=0
    
    #AF Optimisation constant
    C.BARR[34]=0

    #PARAM[3-1] Optimisation constant
    C.BARR[35]=1.9

    #PARAM[13-1] Optimisation constant
    C.BARR[36]=0

    C.UARR[19]=CI.OPTTNK

    #Allocate tank dimensions
    #If tank dimensions fixed
    if(CI.OPTTNK[0]=='N'):
        CI.EXTANK=CI.LTANK
        CI.DCOCOV=CI.HTANK
        CI.DWITA=CI.BTANK
       
    C.IARR[52]=3
    
    CTAN=CI.CKTANK[:3]
    NHELP=int(CI.CKTANK[3])

    if(NHELP==0): NHELP=2
    if(CTAN=='TMY'): C.IARR[52]=NHELP
    if(CTAN=='TAA'): C.IARR[52]=9+NHELP
    if(CTAN=='TAD'): C.IARR[52]=11
    if(CTAN=='TBA'): C.IARR[52]=11+NHELP
    if(CTAN=='NO'): C.IARR[52]=0
    if(CI.CKTANK==' '): C.IARR[52]=-1

    C.AARR[150]=CI.DWITA
    C.AARR[151]=CI.EXTANK
    C.AARR[152]=CI.DCOCOV
    C.TARR[55]=CI.KCOOL
    C.AARR[154]=65.

    if(CI.TWINDM > 25.): C.AARR[154]=CI.TWINDM
    C.AARR[155]=60
    if(CI.TTOILM > 25.): C.AARR[155]=CI.TTOILM

    #AARR[79] = Core space factor with NO additional varnish
    C.AARR[79]=0.96
    #AARR[89] = Core space factor with additional varnish
    
    C.AARR[89]=0.935
    
    #Booster data
    C.MABOOS = CI.BOOSMA
    C.VOBOOS = CI.BOOSVO
    C.REBOOS = CI.BOOSRE
    C.BBBOOS  =CI.BBBOOS
    C.TRBOOS = CI.BOOSTR

    C.TELOSS = CI.TEMPLO
    C.STKFAC = CI.STACKF
    C.SPFADJ = CI.SPFADU

    C.BBHLI=False
    C.BBHLI=FBB('WX146',C.BBERR,CI.REOPT[0])
    C.BBDLI=False
    C.BBDLI=FBB('WX146',C.BBERR,CI.REOPT[1])
    C.BBFLU=False
    C.BBFLU=FBB('WX146',C.BBERR,CI.REOPT[2])
    C.BBREA=False
    C.BBREA=FBB('WX146',C.BBERR,CI.REOPT[3])

    #Limb height has not been stated
    if(not C.BBHLI and CI.HLIMB < 100):
        C.JFC,C.BBERR=FPRINT(2,C.BBERR,'WX146:Limb height is missing.')
    #Core diameter has not been stated

    if(not C.BBDLI and CI.DCORE < 50):
        C.JFC,C.BBERR=FPRINT(2,C.BBERR,'WX146:Core diameter is missing.')

# Flux density has not been stated

    if( not C.BBFLU and CI.BLIMB < 0.1):
        C.JFC,C.BBERR=FPRINT(2,C.BBERR,'WX146:Flux density is missing.')

# Reactance has not been stated   
    if(not C.BBREA  and CI.USHORE < 0.1 and (C.BBHLI or C.BBDLI)):
        C.JFC,C.BBERR=FPRINT(2,C.BBERR,'WX146:Reactance is missing.')

#Optimisation variables adjusted depending on YES/NO answers

# Start of the YES/NO block 

    if(C.BBHLI): CI.HLIMB=-1*CI.HLIMB
    if(C.BBDLI): C.AARR[142]=-1*CI.DCORE
    if(C.BBFLU): C.AARR[145]=-1*CI.BLIMB
    if(C.BBREA): C.AARR[3]=0

#SEBL End of the YES/NO block    
        
#For each winding
    for IWDG in range(1,1+C.NWILI):
# Switch off the structure analyser (Not all calls need be shown)
        
        C.IARR[40+IWDG-1]=1
        if(CI.NGROUP[IWDG-1] != 1):  C.IARR[40+IWDG-1]=round(CI.NGROUP[IWDG-1])
        C.AARR[40+IWDG-1]=1
        if(CI.FRACT[IWDG-1] != 1):   C.AARR[40+IWDG-1]=CI.FRACT[IWDG-1]
        C.AARR[120+IWDG-1]=120
        if(CI.TENSM[IWDG-1] > 1):   C.AARR[120+IWDG-1]=CI.TENSM[IWDG-1]
        C.AARR[130+IWDG-1]=55
        if(CI.PRESSM[IWDG-1] > 1):  C.AARR[130+IWDG-1]=CI.PRESSM[IWDG-1]
#SON Switch on the structure analyser (Next 3 lines will be analysed)
#Encode a CHARACTER alteration
        C.TARR[40+IWDG-1]='CU'
        if(CI.CONMAT[IWDG-1][0]=='A'): C.TARR[40+IWDG-1]='AL'

        C.BARR[IWDG-1]=-1
        if(CI.NCDUCT[IWDG-1]>=0):  C.BARR[IWDG-1]=round(CI.NCDUCT[IWDG-1])

#Encode a REAL alteration

        C.BARR[10+IWDG-1]=-1
        if(CI.HPART[IWDG-1] > 0):   C.BARR[10+IWDG-1]=CI.HPART[IWDG-1]
#SOFF Switch off the structure analyser (Not all calls need be shown)

        C.AARR[110+IWDG-1]=2.44
        if(CI.BPART[IWDG-1]>0.):    C.AARR[110+IWDG-1]=CI.BPART[IWDG-1]
        C.DARR[30+IWDG-1]=CI.COVSTR[IWDG-1]
        C.DARR[IWDG-1]=0
        if(CI.XOILGR[IWDG-1]>=0):   C.DARR[IWDG-1]=round(CI.XOILGR[IWDG-1])
        COV=CI.COVSTR[IWDG-1]+CI.COVCBL[IWDG-1]
        C.BARR[20+IWDG-1]=-1
        if(COV>0.):            C.BARR[20+IWDG-1]=COV
        CBLTX=CI.CBLTYP[IWDG-1]
        if(CI.CBLTYP[IWDG-1]=='SP'):  C.TARR[60+IWDG-1]='SP'
        if(CI.CBLTYP[IWDG-1]=='OR'):  C.TARR[60+IWDG-1]='OR'
        if(CI.CBLTYP[IWDG-1]=='LR'):  C.TARR[60+IWDG-1]='LR'
        if(CI.CBLTYP[IWDG-1]=='TC'):  C.TARR[60+IWDG-1]='TC'
        C.UARR[IWDG-1]='NO'
        if(CI.COMBWI[IWDG-1][1-1]=='Y'): C.UARR[IWDG-1]='YES'
        C.UARR[10+IWDG-1]='NO'
        if(CI.CBLTYP[IWDG-1]=='TC'):  C.UARR[10+IWDG-1]='YES'
        if(CI.XSTRRD[IWDG-1] > 1.5):    C.DARR[20+IWDG-1]=CI.XSTRRD[IWDG-1]
        C.UARR[30+IWDG-1]=CI.CONVAR[IWDG-1]
        C.UARR[40+IWDG-1]=CI.TCEPOX[IWDG-1]
        
        C.ISAM=1
        
        if(FBB('WX146',C.BBERR,C.UARR[IWDG-1])): C.ISAM=2
        C.NCONDU[IWDG-1]=1
        if(C.TARR[40+IWDG-1]=='AL'): C.NCONDU[IWDG-1]=2
        if(FBB('WX146',C.BBERR,C.UARR[10+IWDG-1])):
            C.NCONDU[IWDG-1]=3
#SON Switch on the structure analyser (Not all calls need be shown)   

#SOFF Switch off the structure analyser (Not all calls need be shown)
    for I in range(1,1+C.NG):
        if(CI.XREA[I-1]>0): 
            C.AARR[35+I-1]=CI.XREA[I-1]
    if(abs(CI.HLIMB) > 100): C.DARR[19]=CI.HLIMB
    C.DARR[9]=5000
    if(CI.HLIMBM > 0):        C.DARR[9]=CI.HLIMBM
    C.DARR[39]=max(600,(YOKDIS+350))
    if(CI.HLIMBN > C.DARR[39]):  C.DARR[40-1]=CI.HLIMBN
    C.AARR[4]=5
    if(CI.UMAXPU >= 0): C.AARR[4]=CI.UMAXPU
    if(CI.BLTOPM != 0): 
        if(not(CI.COREMA=='HI-B' and CI.BLTOPM==1.98)): 
            if(not(CI.COREMA=='ZDKH' and CI.BLTOPM==1.98)): 
                if(not(CI.COREMA=='PLJT'and CI.BLTOPM==1.98)): 
                    if(not(CI.COREMA=='M5'  and CI.BLTOPM == 1.95)):
                        C.AARR[146]=CI.BLTOPM    

    C.AARR[153]=60
    if(CI.FONAN>0):         C.AARR[153]=CI.FONAN
    C.TARR[1]='NO'
    if(CI.TYPREG=='VFR'):     C.TARR[1]='YES'
    if(CI.UTURN>0):          C.AARR[144]=CI.UTURN
    C.TARR[72]='NO'
    
    C.TARR[0]='M5'
    if(CI.COREMA=='HI-B'):    C.TARR[1-1]='HI-B'
    if(CI.COREMA=='ZDKH'):    C.TARR[1-1]='ZDKH'
    if(CI.COREMA=='PLJT'):    C.TARR[1-1]='PLJT'
    if(CI.COREMA=='EXT'):    C.TARR[1-1]= 'EXT'   
    
    C.UARR[21-1]= CI.CORESE
    
    if(CI.CORESE=='TA1'):
        C.LAMTH = CI.LAMTH /1000
        C.LAMSPF = CI.LAMSPF
        C.LAMMW = CI.LAMMW /1000
        C.LAMOVL = CI.LAMOVL/1000
        C.ACCLON = CI.ACCLON
        C.ACCTRA = CI.ACCTRA
        C.ACCVER = CI.ACCVER
        C.AMBTEM = CI.AMBTEM
        C.LAMSTP = CI.LAMSTP/1000
        C.LOSCOR = CI.LOSCOR
        C.TA1HOL = CI.TA1HOL/1000
        C.FLPLMA = CI.FLPLMA
    
    C.NCOOLI = CI.NCOOLI    
    
    C.AARR[172]=500
    if(CI.GTRPM > 0):         C.AARR[172]=CI.GTRPM
    C.AARR[173]=4700
    if(CI.HTANKM >= 0):        C.AARR[173]=CI.HTANKM
    C.AARR[174]=3660
    if(CI.BTANKM >= 0):        C.AARR[174]=CI.BTANKM
    C.AARR[175]=13900
    if(CI.RLTANM >= 0):        C.AARR[175]=CI.RLTANM
    if(CI.SOUNDM >= 0):        C.AARR[176]=CI.SOUNDM
    #CPUMIN=0.03
    #AARR(161)=CPUMIN
    #IF (CI.CPUIND.GE.CPUMIN)    AARR(161)=CI.CPUIND
    C.AARR[160]=CI.CPUIND
    C.AARR[167]=-1
    if(CI.CPUFIX != 0):        C.AARR[167]=CI.CPUFIX
    C.TARR[2]='NO'
    if(CI.ALSHLD[0] == 'Y'):  C.TARR[2]='YES'
    
    #CI.T146AC[0] is spare until further notice
    
    C.TARR[3]='NO'

    if(CI.T146AC[1][0]=='Y'): C.TARR[3]='YES'
    
    # C.TARR(95) was used for double shell windings in ADDTXT
    #as well as C.TARR(4)
    # At a convenient moment check if this is necessary
    
    C.TARR[94]='NO'
    if(CI.T146AC[1][0]=='Y'): C.TARR[94]='YES'
    C.TARR[77]='NO'
    if(CI.DETPRE[0]=='Y'):   C.TARR[77]='YES'
    C.TARR[81]='NO'

    C.TARR[74]='NO'
    if(CI.SNDSCR[0]=='Y'):   C.TARR[74]='YES'
    C.TARR[79]='ASEC'
    if(CI.KBAND[0]=='S'):     C.TARR[79]='STEEL'
    if(CI.KBAND[0]=='G'):     C.TARR[79]='GLUED'
    if(CI.KBAND[0]=='P'):     C.TARR[79]='PRESS'
    C.AARR[139]=2
    if(CI.BLDING=='4/4'):  C.AARR[139]=4
    if(CI.TOPDTO > 0.1):  C.AARR[99]=CI.TOPDTO
    C.DARR[29]=2
    if(CI.CVARN=='YES'):  C.DARR[29]=1
    if(CI.CVARN=='PART'):  C.DARR[29]=0
    if(CI.DLMBMA>0.1):  C.AARR[170]=CI.DLMBMA
    if(CI.DLMBMI>0.1):  C.AARR[169]=CI.DLMBMI

    if(abs(CI.HYOKAD-1)>=1): 
        if(CI.CORESE== 'TBA'):  C.AARR[159]=(-1)*CI.HYOKAD
        if(CI.CORESE== 'TCA'):  C.AARR[149]=CI.HYOKAD
    print("END OF WX146")    
    return
