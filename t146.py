import json
from wx146 import WX146
from sub146 import SUB146
#from print import pnt
from movedb import MOVEDB
from pysamp import pysamp
#from sampleprint import SAMPLEPRINT
def T146_TEST(obj_id):
    import com as C
    import cominp as CI
    
    C.BBTS=True
    ''' GET JSON STRING FROM REST API '''
    ''' json_list=getJsonFromOptimizer(obj_id) '''
     
    with open("dat_file_5.json") as json_file:
        json_dict=json.load(json_file)
        
    ''' EXTRACT DATA FROM JSON INTO THE PROGRAM '''
    INX146(json_dict)
    
    '''  Read external variables for calculation of
         no load losses, active and apparent '''

    with open("extcor.json") as ext_file:
        ext_var=json.load(ext_file)
    NLOSSR(ext_var)

    ''' ANALYSE THE DATA '''
    WX146()
    BBRES=False
    SUB146(BBRES)
    pysamp()
    MOVEDB()

def INX146(json_dict):
    
    import cominp as CI
    INP1(json_dict)
    INP2(json_dict)
    INP3(json_dict)
    INP4(json_dict)
    if 'RB' in CI.KWIFUN:
        INP5(json_dict)
    #INP6(json_dict)

def INP1(di):
    import cominp as C  

   #READ INDATA FROM THE DATA BASE FOR PANEL 1 P146-1
    C.IDENT=di["IDENT"]
    
    C.RWILI=GET(di,"RWILI",C.RWILI)

    C.TNODE=GET(di,"TNODE",C.TNODE)
    C.SRATE=GET(di,"SRATE",C.SRATE)
    C.CALCT=GET(di,"CALCT",C.CALCT)#found"Loss calculaton at step no"

    #Read CHARACTER indata from the data base for panel 1 P146-1
    
    C.KCON=GET(di,"KCON",C.KCON)
    C.KTYPRW=GET(di,"KTYPRW",C.KTYPRW)
    C.NPSTEP=GET(di,"NPSTEP",C.NPSTEP)
    C.NMSTEP=GET(di,"NMSTEP",C.NMSTEP)
    C.PUSTEP=GET(di,"PUSTEP",C.PUSTEP)
    C.UNLINE=GET(di,"UNLINE",C.UNLINE)
    C.USURG=GET(di,"USURG",C.USURG)
    C.SLINE=GET(di,"SLINE",C.SLINE)
    C.CGRAD=GET(di,"CGRAD",C.CGRAD)
    C.FREQ=GET(di,"FREQ",C.FREQ)
    C.NPHAS=GET(di,"NPHAS",C.NPHAS)
    C.TYPREG=GET(di,"TYPREG",C.TYPREG)
    C.EVALP0=GET(di,"EVALP0",C.EVALP0)
    C.EVALPK=GET(di,"EVALPK",C.EVALPK)
    C.MNLCOD=GET(di,"MNLCOD",C.MNLCOD)
    C.CPUIND=GET(di,"CPUIND",C.CPUIND)
    C.CPUFIX=GET(di,"CPUFIX",C.CPUFIX)
    C.KCOOL=GET(di,"KCOOL",C.KCOOL)
    C.FONAN=GET(di,"FONAN",C.FONAN)
    C.OPERAT=GET(di,"OPERAT",C.OPERAT)
    C.DETPRE=GET(di,"DETPRE",C.DETPRE)

    C.XREA[0]=di["XREA"]["termL1"]["A"]
    C.XREA[1]=di["XREA"]["termL2"]["A"]
    C.XREA[2]=di["XREA"]["termL2"]["A"]
    C.XREA=C.XREA

def INP2(di):
    import cominp as C     

#Read indata from the data base for panel 2 P146-2
##!!TO BE CHANGED AFTER GETTING OUR DATABASE APIS  
    C.WNOD1=GET(di,"WNOD1",C.WNOD1)
    C.WNOD2=GET(di,"WNOD2",C.WNOD2)
    C.KWIFUN=GET(di,"KWIFUN",C.KWIFUN)
    C.DUYOKE=GET(di,"DUYOKE",C.DUYOKE)
    C.DLYOKE=GET(di,"DLYOKE",C.DLYOKE)
    C.BDUCT=GET(di,"BDUCT",C.BDUCT)
    C.FRACT=GET(di,"FRACT",C.FRACT)
    C.CBLTYP=GET(di,"CBLTYP",C.CBLTYP)
    C.BPART=GET(di,"BPART",C.BPART)
    C.MXCURD=GET(di,"MXCURD",C.MXCURD)
    C.TENSM=GET(di,"TENSM",C.TENSM)
    C.PRESSM=GET(di,"PRESSM",C.PRESSM)
    C.WNDOPT=GET(di,"WNDOPT",C.WNDOPT)
    C.FILLF=GET(di,"FILLF",C.FILLF)
    C.BWIND=GET(di,"BWIND",C.BWIND)
    C.ACOND0=GET(di,"ACOND0",C.ACOND0)
    C.HLIMB=GET(di,"HLIMB",C.HLIMB)
    C.DCORE=GET(di,"DCORE",C.DCORE)
    C.BLIMB=GET(di,"BLIMB",C.BLIMB)
    C.USHORE=GET(di,"USHORE",C.USHORE)
    C.REOPT=GET(di,"REOPT",C.REOPT)
    C.LAYOUT=GET(di,"LAYOUT",C.LAYOUT)
    
def INP3(di):
    import cominp as C      
#Read indata from the data base for panel 3 P146-3

    C.KWITYP=GET(di,"KWITYP",C.KWITYP)
    C.NGROUP=GET(di,"NGROUP",C.NGROUP)
    C.CONMAT=GET(di,"CONMAT",C.CONMAT)
    C.CONVAR=GET(di,"CONVAR",C.CONVAR)
    C.TCEPOX=GET(di,"TCEPOX",C.TCEPOX)

    C.EXTRAR=GET(di,"EXTRAR",C.EXTRAR)
    C.HCLAC=GET(di,"HCLAC",C.HCLAC)

    C.HPART=GET(di,"HPART",C.HPART)

    C.COVSTR=GET(di,"COVSTR",C.COVSTR)
    C.COVCBL=GET(di,"COVCBL",C.COVCBL)

    C.NCDUCT=GET(di,"NCDUCT",C.NCDUCT)
    C.XOILGR=GET(di,"XOILGR",C.XOILGR)

    C.COMBWI=GET(di,"COMBWI",C.COMBWI)

def INP4(di):
    import cominp as C
    INULL= 10e-20
    C.NCOOLX=INULL
      
    C.CKTANK=GET(di,"CKTANK",C.CKTANK)

# Read CHARACTER indata from the data base

    C.OPTTNK=GET(di,"OPTTNK",C.OPTTNK)

#Read REAL indata from the data base
    C.BTANK=GET(di,"BTANK",C.BTANK)

#*SOFF Switch OFF structure analyser (Not all calls need be shown)
    C.HTANK=GET(di,"HTANK",C.HTANK)
    C.LTANK=GET(di,"LTANK",C.LTANK)

    C.DPHAS=GET(di,"DPHAS",C.DPHAS)
    C.DPHSL=GET(di,"DPHSL",C.DPHSL)
    C.DWITA=GET(di,"DWITA",C.DWITA)
    C.DCOCOV= GET(di,"DCOCOV",C.DCOCOV)
    C.EXTANK= GET(di,"EXTANK",C.EXTANK)

    C.SNDSCR =  GET(di,"SNDSCR",C.SNDSCR)
    C.ALSHLD =  GET(di,"ALSHLD",C.ALSHLD)
    C.T146AC[1]=GET(di,"T146AC",C.T146AC[1])

    C.CORESE= GET(di,"CORESE",C.CORESE)
    C.CORTYP= GET(di,"CORTYP",C.CORTYP)
    C.TWSUP=  GET(di,"TWSUP",C.TWSUP)
    C.QMONT=  GET(di,"QMONT",C.QMONT)
    C.COREMA= GET(di,"COREMA",C.COREMA)
    C.KBAND=  GET(di,"KBAND",C.KBAND)
    C.STEPLA= GET(di,"STEPLA",C.STEPLA)

    C.UMAXPU= GET(di,"UMAXPU",C.UMAXPU)
    C.UTURN=  GET(di,"UTURN",C.UTURN)
    C.HYOKAD= GET(di,"HYOKAD",C.HYOKAD)
    C.BLDING= GET(di,"BLDING",C.BLDING)
    C.CVARN=  GET(di,"CVARN",C.CVARN)
    C.TOPDTO= GET(di,"TOPDTO",C.TOPDTO)
    C.NCOOLX= GET(di,"NCOOLX",C.NCOOLX)

    C.TWINDM= GET(di,"TWINDM",C.TWINDM)
    C.TTOILM= GET(di,"TTOILM",C.TTOILM)
    C.BLTOPM= GET(di,"BLTOPM",C.BLTOPM)
    C.HLIMBM= GET(di,"HLIMBM",C.HLIMBM)
    C.HLIMBN= GET(di,"HLIMBN",C.HLIMBN)
    C.MAXP0=  GET(di,"MAXP0",C.MAXP0)
    C.MAXPK=  GET(di,"MAXPK",C.MAXPK)

    C.RLTANM= GET(di,"RLTANM",C.RLTANM)
    C.BTANKM= GET(di,"BTANKM",C.BTANKM)
    C.HTANKM= GET(di,"HTANKM",C.HTANKM)
    C.GTRPM=  GET(di,"GTRPM",C.GTRPM)
    C.SOUNDM= GET(di,"SOUNDM",C.SOUNDM)
    C.DLMBMA= GET(di,"DLMBMA",C.DLMBMA)
    C.DLMBMI= GET(di,"DLMBMI",C.DLMBMI)
    C.STACKF= GET(di,"STACKF",C.STACKF)
    C.TEMPLO= GET(di,"TEMPLO",C.TEMPLO)
    C.SPFADU= GET(di,"SPFADU",C.SPFADU)
        
    if(C.NCOOLX==INULL):
        C.NCOOLI=-1
    else:
        C.NCOOLI=C.NCOOLX    

def INP5(di):
    import cominp as C  
    
    #Read indata from the data base for panel 5 P146-5
  
    C.BOOSMA=GET(di,"BOOSMA",C.BOOSMA)
    C.BOOSVO=GET(di,"BOOSVO",C.BOOSVO)
    C.BOOSRE=GET(di,"BOOSRE",C.BOOSRE)
    C.BOOSTR=GET(di,"BOOSTR",C.BOOSTR)

def INP6(di):
    import cominp as C  
    #Read indata from the data base for panel 6  P146-6
    ##!!TO BE CHANGED AFTER GETTING OUR DATABASE APIS  
    C.LAMTH=GET(di,"LAMTH",C.LAMTH)
    C.LAMSPF=GET(di,"LAMSPF",C.LAMSPF)
    C.LAMMW=GET(di,"LAMMW",C.LAMMW)
    C.LAMOVL=GET(di,"LAMOVL",C.LAMOVL)
    C.ACCLON=GET(di,"ACCLON",C.ACCLON)
    C.ACCTR=GET(di,"ACCTR",C.ACCTR)
    C.ACCVER=GET(di,"ACCVER",C.ACCVER)
    C.AMBTEM=GET(di,"AMBTEM",C.AMBTEM)
    C.LAMSTP=GET(di,"LAMSTP",C.LAMSTP)
    C.LOSCOR=GET(di,"LOSCOR",C.LOSCOR)
    C.TA1HOL=GET(di,"TA1HOL",C.TA1HOL)
    C.FLPLMA=GET(di,"FLPLMA",C.FLPLMA)

def NLOSSR(extcor):
    import com as C
    C.PSPL1=GET(extcor,"PSPL1",C.PSPL1)
    C.PSPL2=GET(extcor,"PSPL2",C.PSPL2)
    C.PSPL3=GET(extcor,"PSPL3",C.PSPL3)
    C.PSPHD1=GET(extcor,"PSPHD1",C.PSPHD1)
    C.PSPHD2=GET(extcor,"PSPHD2",C.PSPHD2)
    C.PSPHD3=GET(extcor,"PSPHD3",C.PSPHD3)
    C.PSPHT1=GET(extcor,"PSPHT1",C.PSPHT1)
    C.PSPHT2=GET(extcor,"PSPHT2",C.PSPHT2)
    C.PSPHT3=GET(extcor,"PSPHT3",C.PSPHT3)
    C.PSPTY1=GET(extcor,"PSPTY1",C.PSPTY1)
    C.PSPTY2=GET(extcor,"PSPTY2",C.PSPTY2)
    C.PSPTY3=GET(extcor,"PSPTY3",C.PSPTY3)
    C.SSPL1=GET(extcor,"SSPL1",C.SSPL1)
    C.SSPL2=GET(extcor,"SSPL2",C.SSPL2)
    C.SSPL3=GET(extcor,"SSPL3",C.SSPL3)
    C.SSPHD1=GET(extcor,"SSPHD1",C.SSPHD1)
    C.SSPHD2=GET(extcor,"SSPHD2",C.SSPHD2)
    C.SSPHD3=GET(extcor,"SSPHD3",C.SSPHD3)
    C.SSPHT1=GET(extcor,"SSPHT1",C.SSPHT1)
    C.SSPHT2=GET(extcor,"SSPHT2",C.SSPHT2)
    C.SSPHT3=GET(extcor,"SSPHT3",C.SSPHT3)
    C.SSPTY1=GET(extcor,"SSPTY1",C.SSPTY1)
    C.SSPTY2=GET(extcor,"SSPTY2",C.SSPTY2)
    C.SSPTY3=GET(extcor,"SSPTY3",C.SSPTY3)
    
def GET(d,key,var):

    try:
        if(list(d[key].keys())[0]=="option"):
            a=d[key]['value']
        
        else:
            a=d[key]

        if type(var) is list:
            for i in 'ABCDEF':
                if i in a:
                    var[ord(i)-65]=a.get(i)
  
        else:
            var=a.get('A')

        print(" received {0} as {1}  ".format(key,var))
 
    except KeyError:
        print(key+' :No Such Key Exists')
        exit()
    except AttributeError:
        var=d[key]
    return var

def update(d,key,var):

    try:
        if(list(d[key].keys())[0]=="option"):
            a=d[key]['value']
        
        else:
            a=d[key]

        if type(var) is list:
            for i in 'ABCDEF':
                if i in a:
                    a[i]=var[ord(i)-65]
  
        else:
            a['A']=var


    except KeyError:
        print(key+' :No Such Key Exists')
        exit()
    return d
    
        
T146_TEST(121212)    
    
