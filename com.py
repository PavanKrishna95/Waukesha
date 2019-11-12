#FROM WX146
LAMTH=0
LAMSPF=0
LAMMW=0
LAMOVL=0
ACCLON=0
ACCTRA=0
ACCVER=0
AMBTEM=0
LAMSTP=0
LOSCOR=0
TA1HOL=0
FLPLMA=0
NOOLI=0
IDENT=0
#FROM WX146
AARR=[0 for i in range(200)]
BARR=[0 for i in range(200)]
DARR=[0 for i in range(200)]
IARR=[0 for i in range(200)]
TARR=[0 for i in range(200)]
UARR=[['' for i in range(4)] for j in range(200)]
NCONDU=[0 for i in range(9)]
IDENTX=[0 for i in range(18)]
OBJE=[0 for i in range(6)]
FARR=[0 for i in range(200)]
WDGFUN=['' for i in range(9)]
MNC=[0 for i in range(2)]
BBHELP=[False for i in range(11)]
BBVR=[False for i in range(4)]
BBDLI=False
BBERR=False
BBFLU=False
BBHLI=False
BBREA=False
BBTS=False
ISAM=0
MNLY=0
JFC=0
NG=0
NWILI=0
TYPCOR=0
FILECH=''
MNL=''
BBLAY=0
MABOOS=0
VOBOOS=0
REBOOS=0
TRBOOS=1
BBOOS=False
TELOSS=0
STKFAC=0
SPFADJ=0

#FROM DIMCUR
RIDIMW=[0 for i in range(4)]
RIDIRW=[0 for i in range(4)]
SRATEP=[0 for i in range(4)]
UDIM=[0 for i in range(4)]
UN=[[0 for i in range(4)] for j in range(4)]
BBAUTO=False
BBVFR=False
NPG=0
NSG=0
SEQU2W=0
SNOML=0

#FROM SUB146
FNEXTV=0
FEXTV=0
U0IN=0
SLINE=[0 for i in range(4)]
BBSCI=[False for i in range(4)]
BBSCJ=[False for i in range(4)]
BBSCK=[False for i in range(4)]
ISTOP=0
BBSCL=[False for i in range(4)]
BBOPTI=False
BBSLIM=False
BLTOPM=0
BMAXPU=0
DCOMAX=0
DCOMIN=0
DTSNN=0
DTSNF=0
DTSFF=0
F1TANK=0
F2TANK=0
F3TANK=0
IPAGE=0
KCORE=0
KTAN79=0
KTANK=0
NCLA=0
NPHAS=0
ZWOULI=0
NWOULI=0
ISTGRD=0
UMAXPU=0
YHADD=0
YHRED=0
CHCORE=''
ACOND=[0 for i in range(9)]
CURDEN=[0 for i in range(9)]
CURDM=[0 for i in range(9)]
KGROUP=[0 for i in range(9)]
PRESSM=[0 for i in range(9)]
TENSM=[0 for i in range(9)]
SRATE=[0 for i in range(4)]
BBCURD=[False for i in range(9)]
BBRW=[False for i in range(9)]
BLIMB=0
BTANKM=0
DCORE=0
DRV=0
EPS=0
FEPS=0
AF=0
FREQ=0
GTRPM=0
HLIMB=0
HLIMBMA=0
HTANKM=0
HLMBMI=0
NFREE=0
PLOADM=0
IOPT=0
PNOLOM=0
RLTNKM=0
SOUNDM=0
TURNRA=0
GREL=[0 for i in range(96)]
G=[0 for i in range(96)]
FABOOS=[1. for i in range(9)]
XREL=[0 for i in range(30)]
XA=[0 for i in range(30)]
HLMBMA=0

#FROM PKL79
CPUFIX=0

#FROM HEAD1
BBERR1=False
IVERS=0
DATE=0
DVERS=''
EXTCOR=False

#FROM SITERM
KCON=[0 for i in range(4)]
KTYPRW=[0 for i in range(4)]
NMSTEP=[0 for i in range(4)]
NPSTEP=[0 for i in range(4)]
PUSTEP=[0 for i in range(4)]
UNLINE=[0 for i in range(4)]
USURG=[0 for i in range(4)]
XRINT=[0 for i in range(4)]
BBUPTR=False
NXSTEP=[0 for i in range(3)]

#FROM SIWIND
BDUCT=[0 for i in range(9)]
BPART=[0 for i in range(9)]
IPISOL=[0 for i in range(9)]
DYOKE=[0 for i in range(9)]
FILLF=[0 for i in range(9)]
FRACT=[0 for i in range(9)]
HPART=[0 for i in range(9)]
KCODE=[0 for i in range(9)]
KWITYP=[0 for i in range(9)]
NGROUP=[0 for i in range(9)]
RAACON=[0 for i in range(9)]
RRWDG=[0 for i in range(9)]
SIGM=[0 for i in range(9)]
TCOV1=[0 for i in range(9)]
TCOV2=[0 for i in range(9)]
TSPIN=[0 for i in range(9)]
BBRR=[False for i in range(9)]
FONAN=0
RAAAL=2700
RAACU=8900
SIGMAL=0.287356E+8
SIGMCU=0.467879E+8
EXTRAR=[0 for i in range(9)]
HCLAC=[0 for i in range(9)]
ZRR=[0 for i in range(9)]
ZPART=[0 for i in range(9)]
BBOOSW=[False for i in range(9)]

#FROM SITANK
BTANK=0
DCOCOV=0
DWITA=0
EXTANK=0
HTANK=0
RLTANK=0

#FROM PREPAR
EDDCO1=[0 for i in range(9)]
EXTX=[0 for i in range(4)]
BBSCR=[False for i in range(4)]
BBDSHE=False
BBFLDS=False
BBWISU=False
APOED=0
BPOED=0
DOUTW=0
GACTP=0
ITR=0
NFMX=0
PI=3.1415926
RMY0=1.2566E-6
SQR3=1.73205080



#FROM NLOSSR
PSPL1=[0 for i in range(3)]
PSPL2=[0 for i in range(5)]
PSPL3=[0 for i in range(3)]
PSPHD1=[0 for i in range(3)]
PSPHD2=[0 for i in range(5)]
PSPHD3=[0 for i in range(3)]
PSPHT1=[0 for i in range(3)]
PSPHT2=[0 for i in range(5)]
PSPHT3=[0 for i in range(3)]
PSPTY1=[0 for i in range(3)]
PSPTY2=[0 for i in range(5)]
PSPTY3=[0 for i in range(3)]
SSPL1=[0 for i in range(3)]
SSPL2=[0 for i in range(5)]
SSPL3=[0 for i in range(3)]
SSPHD1=[0 for i in range(3)]
SSPHD2=[0 for i in range(5)]
SSPHD3=[0 for i in range(3)]
SSPHT1=[0 for i in range(3)]
SSPHT2=[0 for i in range(5)]
SSPHT3=[0 for i in range(3)]
SSPTY1=[0 for i in range(3)]
SSPTY2=[0 for i in range(5)]
SSPTY3=[0 for i in range(3)]
LAMID=''

#FROM VOLTAG
FRMPOS=[0 for i in range(9)]
FRPPOS=[0 for i in range(9)]
FRZPOS=[0 for i in range(9)]
ZTALMW=[0 for i in range(9)]
ZTALRW=[0 for i in range(9)]
BMINPU=0
FRXPOS=[0 for i in range(9)]

#FROM PRESET
KWIND=[0 for i in range(9)]
ZCOIAR=[0 for i in range(9)]
ZAR=[0 for i in range(9)]
ZDISC=[0 for i in range(9)]
ZTULO=[0 for i in range(9)]
NLORR=[0 for i in range(9)]
NLOOP=[0 for i in range(9)]
ZTUDI=[0 for i in range(9)]
ZLAG=[0 for i in range(9)]
ZNLAG=[0 for i in range(9)]
HPRTMN=[0 for i in range(9)]
HPRTMX=[0 for i in range(9)]
BPRTMN=[0 for i in range(9)]
BPRTMX=[0 for i in range(9)]

#FROM TURNCA
EXTPOS=[0 for i in range(3)]
ZTALWG=[[0 for i in range(4)] for j in range(3)]
ZERPOS=[0 for i in range(3)]
RMIPOS=[0 for i in range(4)]
PLSPOS=[0 for i in range(4)]
NLOOPG=[0 for i in range(4)]

#FROM CURDIM

#FROM SIACTP

CPUIND=0
TWINDM=0
KCOOL1=0
KCOOL2=0
AFIELD=0
BB132=0
BB03=False
BB08=False

NCOL=['A','B','C','D','E','F','G','H','I']

#FROM HEAD2
HWIND=[0 for i in range(9)]
BBEND=False
BBEXAC=False
AVALUE=0
CHCOST=''
RUBCH=[['' for i in range(4)] for j in range(15)]
BBFREQ=False

#FROM FUNK
BBOUT=False
ACORE=0
ANDEL=0
ASECL=0
BDRAG=0
CLOSSV=0
COST=0
DKSL=0
DPHAS=0
DPHSL=0
GCORLA=0
GCORN=0
GLIMBM=0
GLIMBY=0
GYOKE=0
HCORE=0
HYOKE=0
ILACK=0
KCOOL=0
NCOOLC=0
P0LOSS=0
PKLOSS=0
PLIMB=0
PLSL=0
QFINAL=0
RDRAG=0
RLTRAN=0
RLYOKE=0
SBF=0
TASEC=0
TCORE=0
TDRAG=0
TTOILC=0
TTOILM=0
TWSUP=0
U0=0
YOKAMP=0
P00=[0 for i in range(3)]
URC=[[[0 for i in range(3)]for j in range(4)]for j in range(4)]
CORBND="0"*8
BBOOVN=False
VALUEM=0
VALUEO=0
BBEXON=False
NCOOLI=0
NCOOLW=0

#FROM OPCALC
AWIND=[0 for i in range(9)]
CUR=[0 for i in range(9)]
FACT=[0 for i in range(9)]
FRACTW=[0 for i in range(9)]
FWIND=[0 for i in range(9)]
PCUW=[0 for i in range(9)]
PEDW=[0 for i in range(9)]
WLOSS=[0 for i in range(9)]
WLOOSM=[0 for i in range(9)]
ZWIND=[0 for i in range(9)]
ZWINDW=[0 for i in range(9)]
PCU=0
PED=0
PLOMAX=0
POED=0
PCUT=[[0 for i in range(4)] for j in range(4)]
PEDT=[[0 for i in range(4)]for j in range(4)]
POEDT=[[0 for i in range(4)] for j in range(4)]
PCEOT=[[0 for i in range(4)] for j in range(4)]
POSIT=[[0 for i in range(4)]for j in range(9)]
UXC=[[[0 for i in range(3)]for j in range(4)]for j in range(4)]
WLOSSE=[0 for i in range(9)]
WLOSSR=[0 for i in range(9)]
FLUXMD=[0 for i in range(9)]
FLUXMW=[0 for i in range(9)]
WLOSSM=[0 for i in range(9)]

#FROM WINDDI
USHORE=0
DWIND=[0 for i in range(9)]
GWINCO=[0 for i in range(9)]
RWIND=[0 for i in range(9)]
EDDCON=[0 for i in range(9)]

#FROM UKX
HWINDM=0

#FROM LOSS
SQR2=1.41421356
FLUXI=[0 for i in range(9)]
FLUXO=[0 for i in range(9)]

#FROM NLOADN
BMINPU=0
Q00=[0 for i in range(3)]
SOUND0=[0 for i in range(3)]
BB132=False

#FROM COOLDP
CCOOL=0
GCOOL=0
GFAN=0
GOFWF=0
GRAD=0
GVVAH=0

#FROM SCDIME
STRWMM=[0 for i in range(9)]
STRWMP=[0 for i in range(9)]

#FROM SCSTRE
NPERM=[0 for i in range(3)]
SCCONS=1.30E-6
X10=[0 for i in range(9)]
X20=[0 for i in range(9)]
X30=[0 for i in range(9)]
SHTCUR=[0 for i in range(9)]

#FROM PENLTY
GTRP=0

#FROM BYTA79
CPUPT=0

#FROM MASS92
GPBLK=0
GTANK=0
GCOVER=0
TANKDI=0
BBLT10=False

#FROM COST92
GOIL=0

#FROM MASS79
ZCODU=[0 for i in range(9)]
BB051=False
KCOOL2=0
RPART=[0 for i in range(9)]
NOUCO=[0 for i in range(9)]
ZLAG=[0 for i in range(9)]
NLOOP=[0 for i in range(9)]
VACTP=0.

CURRUT=[0. for i in range(9)]
VOLTUT=[0. for i in range(9)]

PNOLO=[0. for i in range(5)]
SOUND=[0 for i in range(5)]
RINOLO=[0. for i in range(5)]

UNTAP=[0. for i in range(24)]
CURPRT=[[0. for i in range(3)] for j in range(9)]
CURMNT=[[0. for i in range(3)] for j in range(9)]
CURMXT=[[0. for i in range(3)] for j in range(9)]
CURSPT=[[0. for i in range(3)] for j in range(9)]

ACOVER=0.
ASHELL=0.
COSTTP=0.
CTROVN=0.
PKLPRM=0.
FLUXM=0.
GCONS=0.
NCONST=0.
NUMN=0.
NUYR=0.
DN=0.
VTANK=0.
ZTRANS=0.
SAVE1=['' for i in range(50)]
KODL=0.
KODP=0.
CSTPSW=0.
PG=0.
PK=0.
VALUEF=0.
BBADJU=False
BBISGR=False
SWIND=[0. for i in range(9)]
RINNER=[0. for i in range(9)]
TSPIN1=[0. for i in range(9)]
CTRCMP=0.
CUCOS=0.
CUCOSP=0.
FECOS=0.
FECOSP=0.
OLCOS=0.
GCONDU=0.
OLCOSP=0.0
PNFDUC=0.0
PNFWIN=0.0
PNFYOK=0.0
PNDUCT=0.0
PNWIND=0.0
PNYOKE=0.0
SPRED=0.0
'''
#COMMON VARIABLES
#CST92
CM.CM.FEC92=[0 for i in range(4)]
CM.CM.FEC92=[0 for i in range(4)]
CM.CM.OLC92=0
CM.CM.OLC92P=0
CM.CUC92P=[0 for i in range(3)]
CM.CUC92P=[0 for i in range(3)]

#STANK7
CM.XTANKS=0
CM.YTANKS=0
CM.ZTANKS=0
CM.TTANKS=0

#SPBALK
CM.IPBALK=0
CM.SBALK1=0
CM.SBALK2=0
CM.SBALK3=0
CM.SBALK4=0
CM.TBALK=0

#KONSRE
RES79=[[0]*241]*241

#V79
GS11=[0 for i in range(9)]
GS23=0
GS25=0
GS31=[0 for i in range(4)]
GS32=[0 for i in range(4)]
GS41=[0 for i in range(4)]
GS42=0
GS45=0
GS46=0
GS47=0
GS48=0
GS51=0
GS52=0
GS53=0
GS054=0
GS61=0
GS71=0
GS72=0
GS81=0
GS91=0
GS92= 0      
GS102= 0      
GS111= 0     
GS112=0
GS121=[0 for i in range(9)]   
GS122=   [0 for i in range(9)]
GS131= [0 for i in range(9)]   
GS132=[0 for i in range(9)]
GS133= [0 for i in range(9)]  
GS134=  [0 for i in range(9)] 
GS1351= [0 for i in range(9)]  
GS1352=[0 for i in range(9)]
GS136=[0 for i in range(9)]
GS141=0      
GS142= 0     
GS143= 0      
GS211= 0     
GS212= 0
GS221= 0     
GS222= 0     
GS241= 0      
GS242= 0     
GS1210=0

#VG79
CM.GG21=0        
CM.GG22=0        
CM.GG23=0         
CM.GG24=0        
CM.GG32=[0 for i in range(9)]
CM.GG49=0        
CM.GG51=0        
CM.GG52=0         
CM.GG53=0        
CM.GG054=0
CM.GG54=0        
CM.GG55=0        
CM.GG61=0         
CM.GG63=0        
CM.GG71=0
CM.GG72=0        
CM.GG74=0        
CM.GG81=0         
CM.GG83=0
CM.GG91=0        
CM.GG92=0        
CM.CM.GG94=0         
CM.GG101=0       
CM.GG102=0
CM.GG111=0       
CM.GG1210=0     
CM.GG151=0        
CM.GG152=0
'''
def print_data():
  file1 = open("com_data.txt","a")
  print\
  (LAMTH,\
LAMSPF,\
LAMMW,\
LAMOVL,\
ACCLON,\
ACCTRA,\
ACCVER,\
AMBTEM,\
LAMSTP,\
LOSCOR,\
TA1HOL,\
FLPLMA,\
NOOLI,\
AARR,\
BARR,\
DARR,\
IARR,\
TARR,\
UARR,\
NCONDU,\
IDENTX,\
OBJE,\
FARR,\
WDGFUN,\
MNC,\
BBHELP,\
BBVR,\
BBDLI,\
BBERR,\
BBFLU,\
BBHLI,\
BBREA,\
BBTS,\
ISAM,\
MNLY,\
JFC,\
NG,\
NWILI,\
TYPCOR,\
FILECH,\
MNL,\
BBLAY,\
MABOOS,\
VOBOOS,\
REBOOS,\
TRBOOS,\
BBOOS,\
TELOSS,\
STKFAC,\
SPFADJ,\
RIDIMW,\
RIDIRW,\
SRATEP,\
UDIM,\
UN,\
BBAUTO,\
BBVFR,\
NPG,\
NSG,\
SEQU2W,\
SNOML,\
FNEXTV,\
FEXTV,\

SLINE,\
BBSCI,\
BBSCJ,\
BBSCK,\
ISTOP,\
BBSCL,\
BBOPTI,\
BBSLIM,\
BLTOPM,\
BMAXPU,\
DCOMAX,\
DCOMIN,\
DTSNN,\
DTSNF,\
DTSFF,\
F1TANK,\
F2TANK,\
F3TANK,\
IPAGE,\
KCORE,\
KTAN79,\
KTANK,\
NCLA,\
NPHAS,\
ZWOULI,\
NWOULI,\
ISTGRD,\
UMAXPU,\
YHADD,\
YHRED,\
CHCORE,\
ACOND,\
CURDEN,\
CURDM,\
KGROUP,\
PRESSM,\
TENSM,\
SRATE,\
BBCURD,\
BBRW,\
BLIMB,\
BTANKM,\
DCORE,\
DRV,\
EPS,\
FEPS,\
AF,\
FREQ,\
GTRPM,\
HLIMB,\
HLIMBMA,\
HTANKM,\
HLMBMI,\
NFREE,\
PLOADM,\
IOPT,\
PNOLOM,\
RLTNKM,\
SOUNDM,\
TURNRA,\
GREL,\
G,\
FABOOS,\
XREL,\
XA,\
HLMBMA,\
CPUFIX,\
BBERR1,\
IVERS,\
DATE,\
DVERS,\
EXTCOR,\
KCON,\
KTYPRW,\
NMSTEP,\
NPSTEP,\
PUSTEP,\
UNLINE,\
USURG,\
XRINT,\
BBUPTR,\
NXSTEP,\
FARR,\
BDUCT,\
BPART,\
IPISOL,\
DYOKE,\
FILLF,\
FRACT,\
HPART,\
KCODE,\
KWITYP,\
NGROUP,\
RAACON,\
RRWDG,\
SIGM,\
TCOV1,\
TCOV2,\
TSPIN,\
BBRR,\
FONAN,\
RAAAL,\
RAACU,\
SIGMAL,\
SIGMCU,\
EXTRAR,\
HCLAC,\
ZRR,\
ZPART,\
BBOOSW,\
BTANK,\
DCOCOV,\
DWITA,\
EXTANK,\
HTANK,\
RLTANK,\
EDDCO1,\
EXTX,\
BBSCR,\
BBDSHE,\
BBFLDS,\
BBWISU,\
APOED,\
BPOED,\
DOUTW,\
GACTP,\
ITR,\
NFMX,\
PI,\

SQR3,\
PSPL1,\
PSPL2,\
PSPL3,\
PSPHD1,\
PSPHD2,\
PSPHD3,\
PSPHT1,\
PSPHT2,\
PSPHT3,\
PSPTY1,\
PSPTY2,\
PSPTY3,\
SSPL1,\
SSPL2,\
SSPL3,\
SSPHD1,\
SSPHD2,\
SSPHD3,\
SSPHT1,\
SSPHT2,\
SSPHT3,\
SSPTY1,\
SSPTY2,\
SSPTY3,\
LAMID
)

















































































#QUIVAL#NC#
     #  (XZ0001(1)    ,  AARR   (1)    ),
     #  (XZ0181(1)    ,  BARR   (1)    ),
     #  (XZ0231(1)    ,  DARR   (1)    ),
     #  (XZ0301(1)    ,  IARR   (1)    ),
     #  (XZ0401(1)    ,  TARR   (1)    )
       #QUIVAL#NC#
     #  (XZ1299       ,  BB03          ),
     #  (XZ1300       ,  BB051         ),
     #  (XZ1370       ,  BB08          ),
     #  (XZ1378       ,  BB#RR         ),
     #  (XZ1311(1)    ,  BBH#LP (1)    ),
     #  (XZ1391       ,  BBTS          ),
     #  (XZ1371       ,  BB132         ),
     #  (XZ1376       ,  BBDSH#        )
       #QUIVAL#NC#
     #  (XZ1381       ,  BBFLDS        ),
     #  (XZ1390       ,  BBSLIM        ),
     #  (XZ1395       ,  BBWISU        ),
     #  (XZ1398       ,  AFI#LD        )
       #QUIVAL#NC#
     #  (XZ1405       ,  BLIMB         ),
     #  (XZ1426       ,  DCOR#         ),
     #  (XZ1429       ,  DPHAS         ),
     #  (XZ1430       ,  DPHSL         )
       #QUIVAL#NC#
     #  (XZ1446       ,  FR#Q          ),
     #  (XZ1467       ,  GTRPM         ),
     #  (XZ1473       ,  HLMBMA        ),
     #  (XZ1478       ,  HLMBMI        ),
     #  (XZ1480       ,  ILACK         ),
     #  (XZ1486       ,  JFC           ),
     #  (XZ1488       ,  KCOOL         )
       #QUIVAL#NC#
     #  (XZ1489       ,  KCOOL1        ),
     #  (XZ1490       ,  KCOOL2        ),
     #  (XZ1501       ,  NPHAS         ),
     #  (XZ1509       ,  NWOULI        ),
     #  (XZ1510       ,  P0LOSS        )
       #QUIVAL#NC#
     #  (XZ1514       ,  PKLOSS        ),
     #  (XZ1516       ,  PLOADM        ),
     #  (XZ1520       ,  PNOLOM        ),
     #  (XZ1523       ,  QFINAL        ),
     #  (XZ1543       ,  SOUNDM        )
       #QUIVAL#NC#
     #  (XZ1553       ,  TTOILC        ),
     #  (XZ1554       ,  TTOILM        ),
     #  (XZ1556       ,  TWINDM        ),
     #  (XZ1557       ,  TWSUP         ),
     #  (XZ2782       ,  ISTOP         ),
     #  (XZ1560       ,  UMAXPU        )
       #QUIVAL#NC#
     #  (XZ1571       ,  ZWOULI        ),
     #  (XZ2295       ,  CORBND        ),
     #  (XZ2701       ,  #XTCOR        ),
     #  (XZ1419       ,  CPUIND        )



#QUIVAL#NC#
     #  (XZ0651(1)    ,  ACOND  (1)    ),
     #  (XZ0741(1)    ,  DWIND  (1)    ),
     #  (XZ0901(1)    ,  KGROUP (1)    ),
     #  (XZ1021(1)    ,  SHTCUR (1)    ),
     #  (XZ1041(1)    ,  STRWMM (1)    )
       #QUIVAL#NC#
     #  (XZ1051(1)    ,  STRWMP (1)    ),
     #  (XZ1131(1)    ,  X10    (1)    ),
     #  (XZ1141(1)    ,  X20    (1)    ),
     #  (XZ1151(1)    ,  X30    (1)    ),
     #  (XZ1191(1)    ,  ZWIND  (1)    )
       #QUIVAL#NC#
     #  (XZ1211(1)    ,  #XTX   (1)    ),
     #  (XZ1271(1,1)  ,  UN     (1,1)  ),
     #  (XZ1291(1)    ,  XRINT  (1)    ),
     #  (XZ1341(1)    ,  BBRW   (1)    ),
     #  (XZ1360(1)    ,  BBSCL  (1)    )
       #QUIVAL#NC#
     #  (XZ1363(1)    ,  BBSCR  (1)    ),
     #  (XZ1373       ,  BBAUTO        ),
     #  (XZ1393       ,  BBVFR         ),
     #  (XZ1476       ,  HWINDM        ),
     #  (XZ1499       ,  NG            )
       #QUIVAL#NC#
     #  (XZ1500       ,  NPG           ),
     #  (XZ1504       ,  NSG           ),
     #  (XZ1508       ,  NWILI         ),
     #  (XZ1513       ,  PI            ),
     #  (XZ1538       ,  SCCONS        )
       #QUIVAL#NC#
     #  (XZ1542       ,  SNOML         ),
     #  (XZ1647(1)    ,  NP#RM  (1)    ),
     #  (XZ1656(1,1)  ,  POSIT  (1,1)  ),
     #  (XZ1690(1,1,1),  UXC    (1,1,1)),
     #  (XZ2733(1)    ,  BBOOSW (1)    ),
     #  (XZ2730       ,  TRBOOS     





#QUIVAL#NC#
     #  (XZ0801(1)    ,  FRACT  (1)    ),
     #  (XZ0821(1)    ,  FRMPOS (1)    ),
     #  (XZ0831(1)    ,  FRPPOS (1)    ),
     #  (XZ0841(1)    ,  FRZPOS (1)    ),
     #  (XZ0891(1)    ,  KCOD#  (1)    )
       #QUIVAL#NC#
     #  (XZ0901(1)    ,  KGROUP (1)    ),
     #  (XZ0931(1)    ,  NLOOP  (1)    ),
     #  (XZ1171(1)    ,  ZTALMW (1)    ),
     #  (XZ1181(1)    ,  ZTALRW (1)    )
       #QUIVAL#NC#
     #  (XZ1219(1)    ,  KTYPRW (1)    ),
     #  (XZ1223(1)    ,  NLOOPG (1)    ),
     #  (XZ1227(1)    ,  NMST#P (1)    ),
     #  (XZ1231(1)    ,  NPST#P (1)    ),
     #  (XZ1235(1)    ,  PLSPOS (1)    )
       #QUIVAL#NC#
     #  (XZ1239(1)    ,  PUST#P (1)    ),
     #  (XZ1251(1)    ,  RMIPOS (1)    ),
     #  (XZ1267(1)    ,  UDIM   (1)    ),
     #  (XZ1295(1)    ,  Z#RPOS (1)    ),
     #  (XZ1366(1)    ,  BBVR   (1)    )
       #QUIVAL#NC#
     #  (XZ1373       ,  BBAUTO        ),
     #  (XZ1392       ,  BBUPTR        ),
     #  (XZ1393       ,  BBVFR         ),
     #  (XZ1499       ,  NG            ),
     #  (XZ1508       ,  NWILI         )
       #QUIVAL#NC#
     #  (XZ1656(1,1)  ,  POSIT  (1,1)  ),
     #  (XZ1767(1)    ,  ZTALWG (1,1)  ),
     #  (XZ3001(1)    ,  #XTPOS (1)    ),
     #  (XZ3004(1)    ,  FRXPOS (1)    ),
     #  (XZ3010(1)    ,  NXST#P (1)    )

#QUIVAL#NC#
     #  (XZ0821(1)    ,  FRMPOS (1)    ),
     #  (XZ0831(1)    ,  FRPPOS (1)    ),
     #  (XZ0841(1)    ,  FRZPOS (1)    ),
     #  (XZ0901(1)    ,  KGROUP (1)    ),
     #  (XZ1171(1)    ,  ZTALMW (1)    )
       #QUIVAL#NC#
     #  (XZ1181(1)    ,  ZTALRW (1)    ),
     #  (XZ1267(1)    ,  UDIM   (1)    ),
     #  (XZ1271(1,1)  ,  UN     (1,1)  ),
     #  (XZ1373       ,  BBAUTO        ),
     #  (XZ1392       ,  BBUPTR        )
       #QUIVAL#NC#
     #  (XZ1393       ,  BBVFR         ),
     #  (XZ1407       ,  BMAXPU        ),
     #  (XZ1408       ,  BMINPU        ),
     #  (XZ1499       ,  NG            ),
     #  (XZ1500       ,  NPG           )
       #QUIVAL#NC#
     #  (XZ1504       ,  NSG           ),
     #  (XZ1508       ,  NWILI         ),
     #  (XZ3004(1)    ,  FRXPOS (1)    )

#QUIVAL#NC#
     #  (XZ1508       ,  NWILI         ),
     #  (XZ0901(1)    ,  KGROUP (1)    ),
     #  (XZ1191(1)    ,  ZWIND  (1)    ),
     #  (XZ0401(1)    ,  TARR   (1)    ),
     #  (XZ1472       ,  HLIMB         ),
     #  (XZ0751(1)    ,  DYOK#  (1)    )
       #QUIVAL#NC#
     #  (XZ1331(1)    ,  BBRR   (1)    ),
     #  (XZ0921(1)    ,  NGROUP (1)    ),
     #  (XZ2555(1)    ,  KWIND  (1)    ),
     #  (XZ2583(1)    ,  ZCOIAR (1)    ),
     #  (XZ2584(1)    ,  #XTRAR (1)    ),
     #  (XZ2585(1)    ,  HCLAC  (1)    )
       #QUIVAL#NC#
     #  (XZ1091(1)    ,  TSPIN  (1)    ),
     #  (XZ2591(1)    ,  ZAR    (1)    ),
     #  (XZ2592(1)    ,  ZRR    (1)    ),
     #  (XZ2593(1)    ,  ZPART  (1)    ),
     #  (XZ0871(1)    ,  HPART  (1)    )
       #QUIVAL#NC#
     #  (XZ0681(1)    ,  BPART  (1)    ),
     #  (XZ2586(1)    ,  ZDISC  (1)    ),
     #  (XZ0651(1)    ,  ACOND  (1)    ),
     #  (XZ2595(1)    ,  ZTULO  (1)    ),
     #  (XZ2554(1)    ,  NLORR  (1)    )
       #QUIVAL#NC#
     #  (XZ0931(1)    ,  NLOOP  (1)    ),
     #  (XZ2594(1)    ,  ZTUDI  (1)    ),
     #  (XZ0891(1)    ,  KCOD#  (1)    ),
     #  (XZ2581(1)    ,  ZLAG   (1)    ),
     #  (XZ2582(1)    ,  ZNLAG  (1)    )
       #QUIVAL#NC#
     #  (XZ2597(1)    ,  HPRTMN (1)    ),
     #  (XZ2598(1)    ,  HPRTMX (1)    ),
     #  (XZ2599(1)    ,  BPRTMN (1)    ),
     #  (XZ2600(1)    ,  BPRTMX (1)    )





 #EQUIVALENCE
     #  (XZ0691(1)    ,  CUR    (1)    ),
     #  (XZ0741(1)    ,  DWIND  (1)    ),
     #  (XZ0771(1)    ,  EDDCON (1)    ),
     #  (XZ0811(1)    ,  FRACTW (1)    ),
     #  (XZ0911(1)    ,  KWITYP (1)    ),
     #  (XZ0951(1)    ,  PCUW   (1)    )
       #EQUIVALENCE
     #  (XZ0961(1)    ,  PEDW   (1)    ),
     #  (XZ1001(1)    ,  RRWDG  (1)    ),
     #  (XZ1011(1)    ,  RWIND  (1)    ),
     #  (XZ1191(1)    ,  ZWIND  (1)    ),
     #  (XZ1401       ,  APOED         )
       #EQUIVALENCE
     #  (XZ1409       ,  BPOED         ),
     #  (XZ1443       ,  FLUXM         ),
     #  (XZ1446       ,  FREQ          ),
     #  (XZ1476       ,  HWINDM        ),
     #  (XZ1508       ,  NWILI         )
       #EQUIVALENCE
     #  (XZ1511       ,  PCU           ),
     #  (XZ1512       ,  PED           ),
     #  (XZ1513       ,  PI            ),
     #  (XZ1521       ,  POED          ),
     #  (XZ1532       ,  RMY0          )
       #EQUIVALENCE
     #  (XZ1544       ,  SQR2          ),
     #  (XZ2271(1)    ,  FLUXMD (1)    ),
     #  (XZ2281(1)    ,  FLUXMW (1)    ),
     #  (XZ2401(1)    ,  FLUXI  (1)    ),
     #  (XZ2411(1)    ,  FLUXO  (1)    ),
     #  (XZ2729       ,  REBOOS        ),
     #  (XZ2730       ,  TRBOOS        ),
     #  (XZ2733(1)    ,  BBOOSW(1)     )
#EQUIVALENCE
     #  (XZ0651(1)    ,  ACOND  (1)    ),
     #  (XZ0661(1)    ,  AWIND  (1)    ),
     #  (XZ0671(1)    ,  BDUCT  (1)    ),
     #  (XZ0681(1)    ,  BPART  (1)    )
 #      EQUIVALENCE
     #  (XZ0741(1)    ,  DWIND  (1)    ),
     #  (XZ0751(1)    ,  DYOKE  (1)    ),
     #  (XZ0761(1)    ,  EDDCO1 (1)    ),
     #  (XZ0771(1)    ,  EDDCON (1)    ),
   #  #  (XZ0791(1)    ,  FILLF  (1)    )
    #   EQUIVALENCE
     #  (XZ0851(1)    ,  FWIND  (1)    ),
     #  (XZ0861(1)    ,  GWINCO (1)    ),
  #   #  (XZ0881(1)    ,  HWIND  (1)    ),
     #  (XZ0981(1)    ,  RAACON (1)    ),
     #  (XZ1001(1)    ,  RRWDG  (1)    )
      # EQUIVALENCE
     #  (XZ1011(1)    ,  RWIND  (1)    ),
     ##  (XZ1031(1)    ,  SIGM   (1)    ),
     #  (XZ1191(1)    ,  ZWIND  (1)    ),
     #  (XZ1311(1)    ,  BBHELP (1)    ),
     #  (XZ1378       ,  BBERR         ),
     #  (XZ1391       ,  BBTS          ),
     #  (XZ1486       ,  JFC           ),
     #  (XZ1331(1)    ,  BBRR   (1)    )
       #EQUIVALENCE
     #  (XZ1380       ,  BBEXAC        ),
     #  (XZ1384       ,  BBHLI         ),
     #  (XZ1389       ,  BBREA         ),
     #  (XZ1426       ,  DCORE         ),
     #  (XZ1428       ,  DOUTW         )
       #EQUIVALENCE
     #  (XZ1472       ,  HLIMB         ),
     #  (XZ1476       ,  HWINDM        ),
     #  (XZ1508       ,  NWILI         ),
     #  (XZ2782       ,  ISTOP         ),
     #  (XZ1513       ,  PI            )
      # EQUIVALENCE
     #  (XZ1555       ,  TURNRA        ),
     #  (XZ1561       ,  USHORE        )
#EQUIVALENCE
     #  (XZ0741(1)    ,  DWIND  (1)    ),
     #  (XZ0781(1)    ,  FACT   (1)    ),
     #  (XZ0851(1)    ,  FWIND  (1)    ),
     #  (XZ1001(1)    ,  RRWDG  (1)    ),
     #  (XZ1446       ,  FREQ          )
 #      EQUIVALENCE
     #  (XZ1476       ,  HWINDM        ),
     #  (XZ1508       ,  NWILI         ),
     #  (XZ1513       ,  PI            ),
     #  (XZ1542       ,  SNOML         )
    #EQUIVALENCE
     #  (XZ0651(1)    ,  ACOND  (1)    ),
     #  (XZ0661(1)    ,  AWIND  (1)    ),
     #  (XZ0691(1)    ,  CUR    (1)    ),
     #  (XZ0701(1)    ,  CURDEN (1)    ),
     #  (XZ0781(1)    ,  FACT   (1)    )
       #EQUIVALENCE
     #  (XZ0791(1)    ,  FILLF  (1)    ),
     #  (XZ0811(1)    ,  FRACTW (1)    ),
     #  (XZ0851(1)    ,  FWIND  (1)    ),
     #  (XZ0901(1)    ,  KGROUP (1)    ),
     #  (XZ0951(1)    ,  PCUW   (1)    )
       #EQUIVALENCE
     #  (XZ0961(1)    ,  PEDW   (1)    ),
     #  (XZ1111(1)    ,  WLOSS  (1)    ),
     #  (XZ1121(1)    ,  WLOSSM (1)    ),
     #  (XZ1191(1)    ,  ZWIND  (1)    ),
     #  (XZ1201(1)    ,  ZWINDW (1)    )
       #EQUIVALENCE
     #  (XZ1227(1)    ,  NMSTEP (1)    ),
     #  (XZ1231(1)    ,  NPSTEP (1)    ),
     #  (XZ1263(1)    ,  SRATEP (1)    ),
     #  (XZ1271(1,1)  ,  UN     (1,1)  )
       #EQUIVALENCE
     #  (XZ1331(1)    ,  BBRR   (1)    ),
     #  (XZ1341(1)    ,  BBRW   (1)    ),
     #  (XZ1366(1)    ,  BBVR   (1)    ),
     #  (XZ1373       ,  BBAUTO        ),
     #  (XZ1380       ,  BBEXAC        )
       #EQUIVALENCE
     #  (XZ1393       ,  BBVFR         ),
     #  (XZ1499       ,  NG            ),
     #  (XZ1500       ,  NPG           ),
     #  (XZ1504       ,  NSG           ),
     #  (XZ1508       ,  NWILI         )
       #EQUIVALENCE
     #  (XZ1511       ,  PCU           ),
     #  (XZ1512       ,  PED           ),
     #  (XZ1517       ,  PLOMAX        ),
     #  (XZ1521       ,  POED          ),
     #  (XZ2782       ,  ISTOP         ),
     #  (XZ1542       ,  SNOML         ),
     #  (XZ1555       ,  TURNRA        )
       #EQUIVALENCE
     #  (XZ1574(1,1)  ,  PCUT   (1,1)  ),
     #  (XZ1575(1,1)  ,  PEDT   (1,1)  ),
     #  (XZ1576(1,1)  ,  POEDT  (1,1)  ),
     #  (XZ1577(1,1)  ,  PCEOT  (1,1)  )
       #EQUIVALENCE
     #  (XZ1656(1,1)  ,  POSIT  (1,1)  ),
     #  (XZ1689(1,1,1),  URC    (1,1,1)),
     #  (XZ1690(1,1,1),  UXC    (1,1,1)),
     #  (XZ2245(1)    ,  WLOSSE (1)    ),
     #  (XZ2254(1)    ,  WLOSSR (1)    )
       #EQUIVALENCE
     #  (XZ2271(1)    ,  FLUXMD (1)    ),
     #  (XZ2281(1)    ,  FLUXMW (1)    ),
     #  (XZ3010(1)    ,  NXSTEP (1)    ),
     #  (XZ2731(1)    ,  FABOOS (1)    )
 #EQUIVALENCE
     #  (XZ0080       ,  FNEXTV        ),
     #  (XZ0090       ,  FEXTV         ),
     #  (XZ0145       ,  U0IN          ),
     #  (XZ0651(1)    ,  ACOND  (1)    ),
     #  (XZ1267(1)    ,  UDIM   (1)    ),
     #  (XZ1301(1)    ,  BBCURD (1)    ),
     #  (XZ1311(1)    ,  BBHELP (1)    )
  #     EQUIVALENCE
     #  (XZ1375       ,  BBDLI         ),
     #  (XZ1382       ,  BBFLU         ),
     #  (XZ1384       ,  BBHLI         ),
     #  (XZ1379       ,  BBERR1        ),
     #  (XZ1380       ,  BBEXAC        )
   #    EQUIVALENCE
     #  (XZ1387       ,  BBOUT         ),
     #  (XZ1390       ,  BBSLIM        ),
     #  (XZ1396       ,  ACORE         ),
     #  (XZ1399       ,  AVALUE        ),
     #  (XZ1400       ,  ANDEL         )
    #   EQUIVALENCE
     #  (XZ1402       ,  ASECL         ),
     #  (XZ1404       ,  BDRAG         ),
     #  (XZ1405       ,  BLIMB         ),
     #  (XZ1407       ,  BMAXPU        ),
     #  (XZ1414       ,  CLOSSV        )
     #  EQUIVALENCE
     #  (XZ1415       ,  COST          ),
     #  (XZ1426       ,  DCORE         ),
     #  (XZ1427       ,  DKSL          ),
     #  (XZ1428       ,  DOUTW         ),
     #  (XZ1429       ,  DPHAS         )
      # EQUIVALENCE
     #  (XZ1430       ,  DPHSL         ),
     #  (XZ1431       ,  DRV           ),
     #  (XZ1446       ,  FREQ          ),
     #  (XZ1452       ,  GACTP         ),
     #  (XZ1455       ,  GCORLA        ),
     #  (XZ1456       ,  GCORN         )
       #EQUIVALENCE
     #  (XZ1459       ,  GLIMBM        ),
     #  (XZ1460       ,  GLIMBY        ),
     #  (XZ1470       ,  GYOKE         ),
     #  (XZ1471       ,  HCORE         ),
     #  (XZ1472       ,  HLIMB         )
       #EQUIVALENCE
     #  (XZ1477       ,  HYOKE         ),
     #  (XZ1480       ,  ILACK         ),
     #  (XZ1483       ,  MNLY          ),
     #  (XZ1486       ,  JFC           ),
     #  (XZ1488       ,  KCOOL         ),
     #  (XZ1491       ,  KCORE         ),
     #  (XZ0581(21)   ,  CORESE        ),  CORESE=UARR(21)
     #  (XZ0581(22)   ,  CORTYP        )   CORTYP=UARR(22)      
       #EQUIVALENCE
     #  (XZ1496       ,  NCOOLC        ),
     #  (XZ1501       ,  NPHAS         ),
     #  (XZ1508       ,  NWILI         ),
     #  (XZ1509       ,  NWOULI        ),
     #  (XZ1510       ,  P0LOSS        ),
     #  (XZ1514       ,  PKLOSS        )
       #EQUIVALENCE
     #  (XZ1515       ,  PLIMB         ),
     #  (XZ1518       ,  PLSL          ),
     #  (XZ1523       ,  QFINAL        ),
     #  (XZ1526       ,  RDRAG         ),
     #  (XZ1527       ,  ISTGRD        ),
     #  (XZ1530       ,  RLTRAN        )
     #  EQUIVALENCE
     #  (XZ1531       ,  RLYOKE        ),
     #  (XZ1537       ,  SBF           ),
     #  (XZ1548       ,  TASEC         ),
     #  (XZ1550       ,  TCORE         ),
     #  (XZ1551       ,  TDRAG         )
     #  EQUIVALENCE
     #  (XZ1553       ,  TTOILC        ),
     #  (XZ1554       ,  TTOILM        ),
     #  (XZ1555       ,  TURNRA        ),
     #  (XZ1557       ,  TWSUP         ),
     #  (XZ1558       ,  TYPCOR        )
     #  EQUIVALENCE
     #  (XZ1559       ,  U0            ),
     #  (XZ1560       ,  UMAXPU        ),
     #  (XZ1565       ,  YHADD         ),
     #  (XZ1566       ,  YHRED         ),
     #  (XZ1567       ,  YOKAMP        )
     #  EQUIVALENCE
     #  (XZ1571       ,  ZWOULI        ),
     #  (XZ1626(1)    ,  OBJ    (1)    ),
     #  (XZ1650(1)    ,  P00    (1)    ),
     #  (XZ1689(1,1,1),  URC    (1,1,1)),
     #  (XZ2295       ,  CORBND        ),
     #  (XZ2307(1)    ,  GREL   (1)    ),
     #  (XZ2500       ,  BBOOVN        )
      # EQUIVALENCE
     #  (XZ2501       ,  VALUEM        ),
     #  (XZ2502       ,  VALUEO        ),
     #  (XZ2566       ,  BBEXON        ),
     #  (XZ2735       ,  STKFAC        ),
     #  (XZ2780       ,  NCOOLI        ),
     #  (XZ2782       ,  ISTOP         ),
     #  (XZ2781       ,  NCOOLW        ),
     #  (XZ2799       ,  SPFADJ        )
 #EQUIVALENCE
     #&  (XZ0001(1)    ,  AARR   (1)    ),
     #&  (XZ0401(1)    ,  TARR   (1)    ),
     #&  (XZ0651(1)    ,  ACOND  (1)    ),
     #&  (XZ0881(1)    ,  HWIND  (1)    ),
     #&  (XZ1001(1)    ,  RRWDG  (1)    )
  #     EQUIVALENCE
     #&  (XZ1375       ,  BBDLI         ),
     #&  (XZ1377       ,  BBEND         ),
     #&  (XZ1379       ,  BBERR1        ),
     #&  (XZ1380       ,  BBEXAC        )
   #    EQUIVALENCE
     #&  (XZ1382       ,  BBFLU         ),
     #&  (XZ1384       ,  BBHLI         ),
     #&  (XZ1386       ,  BBOPTI        ),
     #&  (XZ1389       ,  BBREA         ),
     #&  (XZ1399       ,  AVALUE        ),
     #&  (XZ1426       ,  DCORE         ),
     #&  (XZ1446       ,  FREQ          )
    #   EQUIVALENCE
     #&  (XZ1472       ,  HLIMB         ),
     #&  (XZ1483       ,  MNLY          ),
     #&  (XZ1486       ,  JFC           ),
     #&  (XZ1508       ,  NWILI         ),
     #&  (XZ1519       ,  IOPT          ),
     #&  (XZ1587       ,  CHCOST        )
  #     EQUIVALENCE
     #&  (XZ1596       ,  FILECH        ),
     #&  (XZ1624       ,  MNL           ),
     #&  (XZ1632(1)    ,  RUBCH  (1)    ),
     #&  (XZ1743(1)    ,  XA     (1)    ),
     #&  (XZ2346(1)    ,  G      (1)    )
  #     EQUIVALENCE
     #&  (XZ2562       ,  BBFREQ        ),
     #&  (XZ2782       ,  ISTOP         ),
     #&  (XZ2567       ,  BBLAY         )
  #EQUIVALENCE
     #&  (XZ1378       ,  BBERR         ),
     #&  (XZ1311(1)    ,  BBHELP(1)    ),
     #&  (XZ1391       ,  BBTS          ),
     #&  (XZ1486       ,  JFC           ),
     #&  (XZ2701       ,  EXTCOR        ),
     #&  (XZ2702(1)    ,  PSPL1(1)      ),
     #&  (XZ2703(1)    ,  PSPL2(1)      ),
     #&  (XZ2704(1)    ,  PSPL3(1)      ),
     #&  (XZ2705(1)    ,  PSPHD1(1)     ),
     #&  (XZ2706(1)    ,  PSPHD2(1)     ),
     #&  (XZ2707(1)    ,  PSPHD3(1)     ),
     #&  (XZ2708(1)    ,  PSPHT1(1)     ),
     #&  (XZ2709(1)    ,  PSPHT2(1)     ),
     #&  (XZ2710(1)    ,  PSPHT3(1)     ),
     #&  (XZ2711(1)    ,  PSPTY1(1)     ),
     #&  (XZ2712(1)    ,  PSPTY2(1)     ),
     #&  (XZ2713(1)    ,  PSPTY3(1)     )
   #    EQUIVALENCE
     #&  (XZ2714(1)    ,  SSPL1(1)      ),
     #&  (XZ2715(1)    ,  SSPL2(1)      ),
     #&  (XZ2716(1)    ,  SSPL3(1)      ),
     #&  (XZ2717(1)    ,  SSPHD1(1)     ),
     #&  (XZ2718(1)    ,  SSPHD2(1)     ),
     #&  (XZ2719(1)    ,  SSPHD3(1)     ),
     #&  (XZ2720(1)    ,  SSPHT1(1)     ),
     #&  (XZ2721(1)    ,  SSPHT2(1)     ),
     #&  (XZ2722(1)    ,  SSPHT3(1)     ),
     #&  (XZ2723(1)    ,  SSPTY1(1)     ),
     #&  (XZ2724(1)    ,  SSPTY2(1)     ),
     #&  (XZ2725(1)    ,  SSPTY3(1)     ),
     #&  (XZ2726       ,  LAMID         )
     #&  (XZ0001(1)    ,  AARR   (1)    ),
     #&  (XZ0181(1)    ,  BARR   (1)    ),
     #&  (XZ0301(1)    ,  IARR   (1)    ),
     #&  (XZ0761(1)    ,  EDDCO1 (1)    ),
     #&  (XZ0981(1)    ,  RAACON (1)    )
 
     #&  (XZ1031(1)    ,  SIGM   (1)    ),
     #&  (XZ1211(1)    ,  EXTX   (1)    ),
     #&  (XZ1215(1)    ,  KCON   (1)    ),
     #&  (XZ1255(1)    ,  SLINE  (1)    ),
     #&  (XZ1259(1)    ,  SRATE  (1)    )
 
     #&  (XZ1263(1)    ,  SRATEP (1)    ),
     #&  (XZ1267(1)    ,  UDIM   (1)    ),
     #&  (XZ1283(1)    ,  UNLINE (1)    ),
     #&  (XZ1311(1)    ,  BBHELP (1)    ),
     #&  (XZ1378       ,  BBERR         ),
     #&  (XZ1391       ,  BBTS          ),
     #&  (XZ1363(1)    ,  BBSCR  (1)    )
      #&  (XZ1376       ,  BBDSHE        ),
     #&  (XZ1381       ,  BBFLDS        ),
     #&  (XZ1395       ,  BBWISU        ),
     #&  (XZ1401       ,  APOED         )
 
     #&  (XZ1409       ,  BPOED         ),
     #&  (XZ1428       ,  DOUTW         ),
     #&  (XZ1431       ,  DRV           ),
     #&  (XZ1437       ,  EPS           ),
     #&  (XZ1442       ,  FEPS          )
 
     #&  (XZ1444       ,  AF            ),
     #&  (XZ1446       ,  FREQ          ),
     #&  (XZ1452       ,  GACTP         ),
     #&  (XZ1484       ,  ITR           ),
     #&  (XZ1486       ,  JFC           ),
     #&  (XZ1497       ,  NFMX          )
 
     #&  (XZ1499       ,  NG            ),
     #&  (XZ1501       ,  NPHAS         ),
     #&  (XZ1508       ,  NWILI         ),
     #&  (XZ1509       ,  NWOULI        ),
     #&  (XZ1513       ,  PI            )
 
     #&  (XZ1532       ,  RMY0          ),
     #&  (XZ1542       ,  SNOML         ),
     #&  (XZ1545       ,  SQR3          ),
     #&  (XZ1571       ,  ZWOULI        )
     #EQUIVALENCE
     #&  (XZ0001(1)    ,  AARR   (1)    ),
     #&  (XZ0301(1)    ,  IARR   (1)    ),
     #&  (XZ0581(1)    ,  UARR   (1)    ),
     #&  (XZ1378       ,  BBERR         ),
     #&  (XZ1311(1)    ,  BBHELP (1)    ),
     #&  (XZ1390       ,  BBSLIM        ),
     #&  (XZ1391       ,  BBTS          ),
     #&  (XZ1410       ,  BTANK         )
     #  EQUIVALENCE
     #&  (XZ1411       ,  BTANKM        ),
     #&  (XZ1423       ,  DCOCOV        ),
     #&  (XZ1435       ,  DWITA         ),
     #&  (XZ1438       ,  EXTANK        ),
     #&  (XZ1474       ,  HTANK         )
     #  EQUIVALENCE
     #&  (XZ1475       ,  HTANKM        ),
     #&  (XZ1486       ,  JFC           ),
     #&  (XZ1493       ,  KTANK         ),
     #&  (XZ2782       ,  ISTOP         ),
     #&  (XZ1528       ,  RLTANK        ),
     #&  (XZ1529       ,  RLTNKM        )

#   EQUIVALENCE
     ##&  (XZ0001(1)    ,  AARR   (1)    ),
     ##&  (XZ0181(1)    ,  BARR   (1)    ),
     ##&  (XZ0231(1)    ,  DARR   (1)    ),
     ##&  (XZ0301(1)    ,  IARR   (1)    ),
     ##&  (XZ0401(1)    ,  TARR   (1)    ),
     ##&  (XZ0671(1)    ,  BDUCT  (1)    )
      # EQUIVALENCE
     ##&  (XZ0681(1)    ,  BPART  (1)    ),
     ##&  (XZ0711(1)    ,  CURDM  (1)    ),
     ##&  (XZ0721(1)    ,  IPISOL (1)    ),
     ##&  (XZ0751(1)    ,  DYOKE  (1)    )
      # EQUIVALENCE
     ##&  (XZ0791(1)    ,  FILLF  (1)    ),
     ##&  (XZ0801(1)    ,  FRACT  (1)    ),
     ##&  (XZ0871(1)    ,  HPART  (1)    ),
     ##&  (XZ0891(1)    ,  KCODE  (1)    ),
     ##&  (XZ0901(1)    ,  KGROUP (1)    )
      # EQUIVALENCE
     ##&  (XZ0911(1)    ,  KWITYP (1)    ),
     ##&  (XZ0921(1)    ,  NGROUP (1)    ),
     ##&  (XZ0971(1)    ,  PRESSM (1)    ),
     ##&  (XZ0981(1)    ,  RAACON (1)    ),
     ##&  (XZ1001(1)    ,  RRWDG  (1)    )
      # EQUIVALENCE
     ##&  (XZ1031(1)    ,  SIGM   (1)    ),
     ##&  (XZ1061(1)    ,  TCOV1  (1)    ),
     ##&  (XZ1071(1)    ,  TCOV2  (1)    ),
     ##&  (XZ1081(1)    ,  TENSM  (1)    ),
     ##&  (XZ1091(1)    ,  TSPIN  (1)    )
      # EQUIVALENCE
     ##&  (XZ1287(1)    ,  USURG  (1)    ),
     ##&  (XZ1331(1)    ,  BBRR   (1)    ),
     ##&  (XZ1378       ,  BBERR         ),
     ##&  (XZ1311(1)    ,  BBHELP (1)    ),
     ##&  (XZ1391       ,  BBTS          ),
     ##&  (XZ1445       ,  FONAN         ),
     ##&  (XZ1486       ,  JFC           )
      # EQUIVALENCE
     ##&  (XZ1341(1)    ,  BBRW   (1)    ),
     ##&  (XZ1499       ,  NG            ),
     ##&  (XZ1508       ,  NWILI         ),
     ##&  (XZ1524       ,  RAAAL         ),
     ##&  (XZ1525       ,  RAACU         )
      # EQUIVALENCE
     ##&  (XZ1540       ,  SIGMAL        ),
     ##&  (XZ1541       ,  SIGMCU        ),
     ##&  (XZ2584(1)    ,  EXTRAR (1)    ),
     ##&  (XZ2585(1)    ,  HCLAC  (1)    ),
     ##&  (XZ2592(1)    ,  ZRR    (1)    ),
     ##&  (XZ2593(1)    ,  ZPART  (1)    ),
     ##&  (XZ3390(1)    ,  WDGFUN (1)    ),
     ##&  (XZ2731(1)    ,  FABOOS (1)    ),
     ##&  (XZ2733(1)    ,  BBOOSW (1)    ),
     ##&  (XZ2730       ,  TRBOOS        ),
     ##&  (XZ2734       ,  TELOSS        )

##&  (XZ0671(1)    ,  BDUCT  (1)    )
#       EQUIVALENCE
 #    #&  (XZ0681(1)    ,  BPART  (1)    ),
#     #&  (XZ3010(1)    ,  NXSTEP (1)    ),
#     #&  (XZ3289(1)    ,  FARR   (1)    )
#    #&  (XZ1392       ,  BBUPTR        ),
#     #&  (XZ1291(1)    ,  XRINT  (1)    ),
#     #&  (XZ1287(1)    ,  USURG  (1)    ),
#     #&  (XZ1283(1)    ,  UNLINE (1)    ),
#     #&  (XZ1227(1)    ,  NMSTEP (1)    ),
#     #&  (XZ1231(1)    ,  NPSTEP (1)    ),
#     #&  (XZ1239(1)    ,  PUSTEP (1)    ),
# #&  (XZ1219(1)    ,  KTYPRW (1)    )
# #&  (XZ1215(1)    ,  KCON   (1)    ),
#    #&  (XZ2701       ,  EXTCOR        ),
#   #&  (XZ2551       ,  DVERS         ),
#  #&  (XZ1589       ,  DATE          ),
# #&  (XZ1485       ,  IVERS         ),
# #&  (XZ1379       ,  BBERR1        ),
##(XZ0181#(1)    ,  BARR   #(1)    ),
##(XZ0231#(1)    ,  DARR   #(1)    ),
#(XZ0301#(1)    ,  IARR   #(1)    ),
#(XZ0401#(1)    ,  TARR   #(1)    ),
#(XZ0581#(1)    ,  UARR   #(1)    )
#EQUIVALENCE
#(XZ1311#(1)    ,  BBHELP #(1)    ),
#(XZ1366#(1)    ,  BBVR   #(1)    ),
#(XZ1375       ,  BBDLI         ),
#(XZ1378       ,  BBERR         )
#EQUIVALENCE
#(XZ1382       ,  BBFLU         ),
#(XZ1384       ,  BBHLI         ),
#(XZ1389       ,  BBREA         ),
#(XZ1391       ,  BBTS          )
#EQUIVALENCE
#(XZ1479       ,  ISAM          ),
#(XZ1481#(1)    ,  NCONDU #(1)    ),
#(XZ1483       ,  MNLY          ),
#(XZ1486       ,  JFC           ),
#(XZ1499       ,  NG            ),
#(XZ1508       ,  NWILI         )
#EQUIVALENCE
#(XZ1558       ,  TYPCOR        ),
#(XZ1596       ,  FILECH        ),
#(XZ1604#(1)    ,  IDENTX #(1)    ),
#(XZ1624       ,  MNL           ),
#(XZ1626#(1)    ,  OBJE   #(1)    )
#EQUIVALENCE
#(XZ2567       ,  BBLAY         ),
#(XZ3289#(1)    ,  FARR   #(1)    ),
#(XZ3390#(1)    ,  WDGFUN #(1)    )

#EQUIVALENCE
#(XZ2727       ,  MABOOS        ),
#(XZ2728       ,  VOBOOS        ),
#(XZ2729       ,  REBOOS        ),
#(XZ2730       ,  TRBOOS        ),
#(XZ2732       ,  BBOOS         ),
#(XZ2734       ,  TELOSS        ),
#(XZ2735       ,  STKFAC        ),
#(XZ2799       ,  SPFADJ        ),
#(MNLCOD       ,  MNC    #(1)    )
#     #&  (XZ1243(1)    ,  RIDIMW (1)    ),
#     #&  (XZ1247(1)    ,  RIDIRW (1)    ),
#     #&  (XZ1263(1)    ,  SRATEP (1)    ),
#     #&  (XZ1267(1)    ,  UDIM   (1)    ),
#     #&  (XZ1271(1,1)  ,  UN     (1,1)  )
#       EQUIVALENCE
#     #&  (XZ1373       ,  BBAUTO        ),
#     #&  (XZ1393       ,  BBVFR         ),
#     #&  (XZ1499       ,  NG            ),
#     #&  (XZ1500       ,  NPG           ),
#     #&  (XZ1504       ,  NSG           )
#       EQUIVALENCE
#     #&  (XZ1539       ,  SEQU2W        ),
#     #&  (XZ1542       ,  SNOML         )
#EQUIVALENCE
#     #&  (XZ0001(1)    ,  AARR   (1)    ),
#     #&  (XZ0080       ,  FNEXTV        ),
#     #&  (XZ0090       ,  FEXTV         ),
#     #&  (XZ0145       ,  U0IN          ),
#     #&  (XZ0401(1)    ,  TARR   (1)    ),
#     #&  (XZ0581(1)    ,  UARR   (1)    )
#       EQUIVALENCE
##     #&  (XZ1255(1)    ,  SLINE  (1)    ),
 #    #&  (XZ1378       ,  BBERR         ),
 #    #&  (XZ1311(1)    ,  BBHELP (1)    ),
 #    #&  (XZ1391       ,  BBTS          ),
 #    #&  (XZ1351(1)    ,  BBSCI  (1)    ),
 #    #&  (XZ1354(1)    ,  BBSCJ  (1)    ),
 #    #&  (XZ1357(1)    ,  BBSCK  (1)    ),
 #    #&  (XZ2782       ,  ISTOP         ),
 #    #&  (XZ1360(1)    ,  BBSCL  (1)    )
 #      EQUIVALENCE
 #    #&  (XZ1366(1)    ,  BBVR   (1)    ),
 #    #&  (XZ1386       ,  BBOPTI        ),
 #    #&  (XZ1390       ,  BBSLIM        ),
 #    #&  (XZ1393       ,  BBVFR         )
 #      EQUIVALENCE
 #    #&  (XZ1406       ,  BLTOPM        ),
 #    #&  (XZ1407       ,  BMAXPU        ),
 #    #&  (XZ1424       ,  DCOMAX        ),
 #    #&  (XZ1425       ,  DCOMIN        )
 #      EQUIVALENCE
 #    #&  (XZ1434       ,  DTSNN         ),
 #    #&  (XZ1433       ,  DTSNF         ),
 #    #&  (XZ1432       ,  DTSFF         ),
 #    #&  (XZ1439       ,  F1TANK        ),
 #    #&  (XZ1440       ,  F2TANK        ),
 #    #&  (XZ1441       ,  F3TANK        ),
 #    #&  (XZ1482       ,  IPAGE         ),
 #    #&  (XZ1486       ,  JFC           )
 #      EQUIVALENCE
 #    #&  (XZ1491       ,  KCORE         ),
 #    #&  (XZ1492       ,  KTAN79        ),
 #    #&  (XZ1493       ,  KTANK         ),
 #    #&  (XZ1494       ,  NCLA          ),
 #    #&  (XZ1499       ,  NG            )
 #      EQUIVALENCE
 #    #&  (XZ1501       ,  NPHAS         ),
 #    #&  (XZ1571       ,  ZWOULI        )
 #      EQUIVALENCE
 #    #&  (XZ1509       ,  NWOULI        ),
 #    #&  (XZ1527       ,  ISTGRD        ),
 #    #&  (XZ1560       ,  UMAXPU        )
 #      EQUIVALENCE
 #    #&  (XZ1565       ,  YHADD         ),
 #    #&  (XZ1566       ,  YHRED         ),
 #    #&  (XZ1572       ,  CHCORE        )

 #EQUIVALENCE
     #   #&  (XZ0001(1)    ,  AARR   (1)    ),
     #   #&  (XZ0231(1)    ,  DARR   (1)    ),
     #   #&  (XZ0651(1)    ,  ACOND  (1)    ),
     #   #&  (XZ0701(1)    ,  CURDEN (1)    ),
     #   #&  (XZ0711(1)    ,  CURDM  (1)    )
  #     EQUIVALENCE
     #   #&  (XZ0901(1)    ,  KGROUP (1)    ),
     #   #&  (XZ0971(1)    ,  PRESSM (1)    ),
     #   #&  (XZ1081(1)    ,  TENSM  (1)    ),
     #   #&  (XZ1243(1)    ,  RIDIMW (1)    ),
     #   #&  (XZ1247(1)    ,  RIDIRW (1)    )
   #    EQUIVALENCE
     #   #&  (XZ1259(1)    ,  SRATE  (1)    ),
     #   #&  (XZ1267(1)    ,  UDIM   (1)    ),
     #   #&  (XZ1301(1)    ,  BBCURD (1)    ),
     #   #&  (XZ1378       ,  BBERR         ),
     #   #&  (XZ1311(1)    ,  BBHELP (1)    ),
     #   #&  (XZ1341(1)    ,  BBRW   (1)    ),
     #   #&  (XZ1375       ,  BBDLI         )
    #   EQUIVALENCE
     #   #&  (XZ1382       ,  BBFLU         ),
     #   #&  (XZ1384       ,  BBHLI         ),
     #   #&  (XZ1386       ,  BBOPTI        ),
     #   #&  (XZ1389       ,  BBREA         ),
     #   #&  (XZ1391       ,  BBTS          )
     #  EQUIVALENCE
     #   #&  (XZ1393       ,  BBVFR         ),
     #   #&  (XZ1405       ,  BLIMB         ),
     #   #&  (XZ1406       ,  BLTOPM        ),
     #   #&  (XZ1407       ,  BMAXPU        ),
     #   #&  (XZ1411       ,  BTANKM        )
      # EQUIVALENCE
     #   #&  (XZ1424       ,  DCOMAX        ),
     #   #&  (XZ1425       ,  DCOMIN        ),
     #   #&  (XZ1426       ,  DCORE         ),
     #   #&  (XZ1431       ,  DRV           ),
     #   #&  (XZ1437       ,  EPS           )
       #EQUIVALENCE
     #   #&  (XZ1442       ,  FEPS          ),
     #   #&  (XZ1444       ,  AF            ),
     #   #&  (XZ1446       ,  FREQ          ),
     #   #&  (XZ1467       ,  GTRPM         ),
     #   #&  (XZ1472       ,  HLIMB         )
     #  EQUIVALENCE
     #   #&  (XZ1473       ,  HLMBMA        ),
     #   #&  (XZ1475       ,  HTANKM        ),
     #   #&  (XZ1478       ,  HLMBMI        ),
     #   #&  (XZ1486       ,  JFC           ),
     #   #&  (XZ1498       ,  NFREE         ),
     #   #&  (XZ1508       ,  NWILI         ),
     #   #&  (XZ1516       ,  PLOADM        )
     #  EQUIVALENCE
     #   #&  (XZ1519       ,  IOPT          ),
     #   #&  (XZ1520       ,  PNOLOM        ),
     #   #&  (XZ1529       ,  RLTNKM        ),
     #   #&  (XZ1539       ,  SEQU2W        ),
     #   #&  (XZ1543       ,  SOUNDM        )
     #  EQUIVALENCE
     #   #&  (XZ1555       ,  TURNRA        ),
     #   #&  (XZ1561       ,  USHORE        ),
     #   #&  (XZ1743(1)    ,  XA     (1)    ),
     #   #&  (XZ1755(1)    ,  XREL   (1)    ),
     #   #&  (XZ2307(1)    ,  GREL   (1)    )
     #  EQUIVALENCE
     #   #&  (XZ2346(1)    ,  G      (1)    ),
     #   #&  (XZ2782       ,  ISTOP         ),
     #   #&  (XZ2731(1)    ,  FABOOS (1)    )
     # #&  (XZ1417       ,  CPUFIX        )
