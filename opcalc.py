#Title:Calculation of the physical No. OF turns,
 #winding dimensions, reactances & losses
from winddi import WINDDI
from ukx import UKX
from loss import LOSS 
from goto import with_goto
from losspr import LOSSPR
@with_goto
def OPCALC(BBOUT):
    
    import com as C
    print("START OF OPCALC")
    #start of declarations
    
    CDIM=[0 for i in range(4)]
    CDIR=[0 for i in range(4)]
    IWDG1=0
    LTML=0
    ITAP=0
    
    JTAP=0
    BBUT1=False
    BBUT2=False
    KTML=0
    UK=0
    JTAP2=0

    #end of declarations
    
    #Start of the taps block

    NTAPS=4

    #for each terminal
    for ITML in range(1,1+min(C.NG,3)):

    #Adjust the number of taps
        if(C.BBVR[ITML-1]):
            if((C.NXSTEP[ITML-1]==C.NPSTEP[ITML-1]) or(C.NXSTEP[ITML-1]==C.NMSTEP[ITML-1])or(C.NXSTEP[ITML-1]==0) ):
                NTAPS=3

    #End of taps block
        #Calculation of physical No. of turns
    for IWDG in range(1,1+C.NWILI):
        C.ZWIND[IWDG-1]=C.ZWINDW[IWDG-1]*C.TURNRA*C.FABOOS[IWDG-1]
        if(not C.BBRR[IWDG-1]):
            C.AWIND[IWDG-1]=C.ACOND[IWDG-1]*C.ZWIND[IWDG-1]/C.FILLF[IWDG-1]

        C.FLUXMD[IWDG-1]=0
        C.FLUXMW[IWDG-1]=0
        C.PCUW[IWDG-1]=0
        C.PEDW[IWDG-1]=0
        C.CURDEN[IWDG-1]=0
        C.WLOSS[IWDG-1]=0
        C.WLOSSE[IWDG-1]=0
        C.WLOSSM[IWDG-1]=0
        C.WLOSSR[IWDG-1]=0
        if(C.KGROUP[IWDG-1]==4): C.CURDEN[IWDG-1]=C.SRATEP[3]/C.ACOND[IWDG-1]/C.UN[3][0]
    C.PLOMAX=0
    #KTML = First terminal , LTML = Second terminal
    KTML=1
    label ._300
    if(KTML>2 or (KTML==2 and C.NG==2)):
        print("END OF OPCALC")  
        return
    KTML2=KTML

    LTML=KTML+1

    label ._400
    if(LTML>C.NG or LTML>3): goto ._499
    LTML2=LTML
#*
    SRED=min(C.SRATEP[LTML-1],C.SRATEP[KTML-1])/C.SNOML
#*
#C... ITAP = Tap position on the first  terminal
#C... JTAP = Tap position on the second terminal
#*
    ITAP=1
    BBUT1=False

    label ._500
    if(ITAP>NTAPS or BBUT1): goto ._599
    ITAP2=ITAP
    CDIM[KTML-1]=C.SNOML/C.UN[KTML-1][ITAP2-1]
    CDIR[KTML-1]=CDIM[KTML-1]
    if(KTML==C.NPG): RINPG=CDIM[KTML-1]
    JTAP=1
    BBUT2=False

    label ._600
    if(JTAP>NTAPS or BBUT2): goto ._699

    JTAP2=JTAP
#   Calculation of 'CDIM' and 'CDIR' = Rated current at base power
    #for terminal LTML

    if(C.BBVFR and KTML2==2): JTAP2=ITAP2
    CDIM[LTML-1]=C.SNOML/C.UN[LTML-1][JTAP2-1]
    CDIR[LTML-1]=CDIM[LTML-1]
    if(LTML==C.NPG):RINPG=CDIM[LTML-1]

    if(C.BBAUTO):
        if(LTML==2):CDIM[C.NPG-1]=RINPG-CDIM[C.NSG-1]
        if(LTML>2 and KTML == C.NSG): CDIM[C.NPG-1]=CDIM[C.NSG-1]
        if(C.BBVFR): CDIR[C.NPG-1]=CDIM[C.NPG-1]
    #For each winding
    for IWDG1 in range(1,1+C.NWILI):
        KTML1=C.KGROUP[IWDG1-1]
    #Calculation of C.FACT = Sign of the current for a given 2-wdg case
        C.FACT[IWDG1-1]=0
        C.FWIND[IWDG1-1]=0
        C.CUR[IWDG1-1]=0
        #For the first three terminals
        if(KTML1!= 4):
            if(KTML1==KTML): C.FACT[IWDG1-1]=1
            if(KTML1==LTML): C.FACT[IWDG1-1]=-1
        
        # For an auto connected transformer
        #for terminal 3
            if(C.BBAUTO):
                if(LTML==3 and KTML1==C.NPG):
                    if(C.BBVFR or not(C.BBRW[IWDG1-1])): C.FACT[IWDG1-1]=1

        #C.FRACTW = The connected portion of each winding is given a value            

    
            ITAPP=ITAP2
            if(C.FACT[IWDG1-1]<0): ITAPP=JTAP2
            if(C.BBVFR): ITAPP=max(ITAP2,JTAP2)
            C.FRACTW[IWDG1-1]=C.POSIT[IWDG1-1][ITAPP-1]
        #Calculation of C.CUR, C.FWIND & C.CURDEN
        #C.FWIND is used for the reactance calculation
        # C.CUR   is used for the loss      calculation    
            if(C.FACT[IWDG1-1]!=0):
                CURX=CDIM[KTML1-1]
                if(C.BBRW[IWDG1-1]): CURX=CDIR[KTML1-1]
                C.FWIND[IWDG1-1]=C.ZWIND[IWDG1-1]*C.FACT[IWDG1-1]*C.FRACTW[IWDG1-1]*CURX/C.FABOOS[IWDG1-1]
                C.CUR[IWDG1-1]=CURX/C.FABOOS[IWDG1-1]*SRED*C.FACT[IWDG1-1]
                XX=SRED
                if(KTML+LTML==3): XX=C.SRATEP[LTML-1]/C.SNOML
                
                C.CURDEN[IWDG1-1]=max(C.CURDEN[IWDG-1],CURX/C.FABOOS[IWDG1-1]*XX/C.ACOND[IWDG1-1])

    MTML=KTML+LTML-2
    #Calculation of the winding dimensions
    
    if(((ITAP+JTAP+MTML)==3) and ( not BBOUT)):
        print("OPCALC calling WINDDI")
        WINDDI()
        if(C.ISTOP ==1):return

    #Calculation of reactances
    print("OPCALC calling UKX")
    UK=UKX(UK)
    C.UXC[ITAP2-1][JTAP2-1][MTML-1]=UK 

    #Calculation of losses
    print("OPCALC calling LOSS")
    LOSS()
    PLOSS=C.PCU+C.PED+C.POED

    #Preparing of database-variables.
    C.PCUT[ITAP2-1][MTML-1]=C.PCU
    C.PEDT[ITAP2-1][MTML-1]=C.PED
    C.POEDT[ITAP2-1][MTML-1]=C.POED
    C.PCEOT[ITAP2-1][MTML-1]=PLOSS
    C.URC[ITAP2-1][JTAP2-1][MTML-1]=PLOSS
    
    #Calculation of maximum losses

    #If an exact calculation
    if(C.BBEXAC):
        BBLOSS=False
        if(PLOSS>C.PLOMAX): BBLOSS=True
        if(BBLOSS): C.PLOMAX=PLOSS

    #For each winding
        for IWDG3 in range(1,1+C.NWILI):
            PCUEDW=C.PCUW[IWDG3-1]+C.PEDW[IWDG3-1]
            #Find the maximum value
            if(C.WLOSS[IWDG3-1]<PCUEDW):
                C.WLOSSM[IWDG3-1]=PCUEDW
                C.WLOSSR[IWDG3-1]=C.PCUW[IWDG3-1]
                C.WLOSSE[IWDG3-1]=C.PEDW[IWDG3-1]
            if(BBLOSS): C.WLOSS[IWDG3-1]=PCUEDW  

    #Print the losses
    if(BBOUT): LOSSPR(ITAP2,JTAP2,KTML2,LTML2,MTML)    
    BBUT2=False

    if(not(C.BBVR[LTML-1]or(C.BBVFR and MTML ==2))):BBUT2=True
    JTAP=JTAP+1
    goto ._600  

    label ._699
    BBUT1=False
    if(not C.BBVR[KTML-1]): BBUT1=True
    ITAP=ITAP+1
    goto ._500

    label ._599
    LTML=LTML+1
    goto ._400

    label ._499
    KTML=KTML+1
    goto ._300
    print("END OF OPCALC")  

    return 
