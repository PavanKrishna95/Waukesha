import math
from fprint import FPRINT
def PREP1():
    import com as C
#INITIALIZATIONS

    if(C.BBTS and C.NWILI>7):
        C.JFC,C.BBERR=FPRINT(2,C.BBERR,
                             'PREP1:T146 can handle up to 6 windings only: memory limitation')
        if C.ISTOP==1:
            return
        
    BBSTRT=True
#UK - Short-circuit voltage
#IF BOTH Core diameter AND limb height are given
# then the REACTANCE ( if given ) is ignored
    if(not (C.BBHLI or C.BBDLI)) : C.BBREA=True
    if(not C.BBREA):  C.USHORE=C.AARR[3]/1.E+2

    C.BBOPTI=False
    C.NFREE=0

# Set C.XREL(*) to zero
    for IX in range(1,31):
        C.XREL[IX-1]=0
#Core diameter
    if(C.DCORE<1.E-3):C.DCORE=abs(C.AARR[142])/1.E+3

    #Set core diameter
    # 
    # If not given

    if(C.DCORE<1.E-3):
        BBSTRT=False
        C.DCORE=0.37*math.sqrt(math.sqrt(C.SEQU2W/1.E+3)/C.FREQ)

#Determine core diameter
# If necessary
    if(C.BBDLI):
        C.NFREE=C.NFREE+1
        if(C.DCORE<C.DCOMIN): C.DCORE=C.DCOMIN
        if(C.DCORE>C.DCOMAX): C.DCORE=C.DCOMAX
        C.XREL[0]=0.5*C.DCORE

    C.XA[0]=C.DCORE

    #LIMB HEIGHT
    if(C.HLIMB<0.1): C.HLIMB=abs(C.DARR[19])/1.E+3
    if(abs(C.HLIMB-abs(C.DARR[19]/1.E+3))>1.E-4):
        C.HLIMB=abs(C.DARR[20-1])/1.E+3
    if(C.HLIMB<0.1 and C.BBREA): BBSTRT=False
    if(C.HLIMB<0.1): C.HLIMB=2+2*C.SRATE[0]/1.E+9

    #Determine limb height

    #if necessary
    if(C.BBHLI):
        C.NFREE=C.NFREE+1
        C.XREL[1]=1.0*C.HLIMB

    C.XA[1]=C.HLIMB

    # Flux density
    if(C.BLIMB<0.1): C.BLIMB=abs(C.AARR[145])
    if(C.BBVFR): C.BLIMB=C.BLIMB/C.BMAXPU

    if(C.BLIMB<0.1):
        BBSTRT=False
        C.BLIMB=C.BLTOPM*0.918

    #determine flux density
    if(C.BBFLU):
        C.NFREE=C.NFREE+1
        C.XREL[2]=0.5*C.BLIMB
        BSTART=min(C.BLTOPM-0.01,C.BLIMB)    
        if(BSTART<0.1): BSTART=C.BLTOPM*0.918
        C.BLIMB=BSTART

    C.XA[2]=C.BLIMB

    #No. of turns corresponding to terminal 1 at nominal voltage    
    #start value
    #Exact calculation in CORE1N

    # Start of the C.TURNRA block

    C.TURNRA=C.UDIM[0]/(3.1*C.BLIMB*(C.DCORE**2)*C.AARR[1])

    # End of the C.TURNRA block

    #Windings

    #Determine whether conductor RD for each winding has been given

    for IWDG in range(1,1+C.NWILI):
        C.BBCURD[IWDG-1]=False
        
        if(C.AARR[60+IWDG-1]<1.E-3 and C.AARR[90+IWDG-1]<1.E-3):
            C.BBCURD[IWDG-1]=True

        KGRP=C.KGROUP[IWDG-1]
        RIDI=C.RIDIMW[KGRP-1]
        if(C.BBRW[IWDG-1]):  RIDI=C.RIDIRW[KGRP-1]

        #Determine conductor area and current density        

       #Winding to be optimised
        if(C.BBCURD[IWDG-1]):
            C.NFREE=C.NFREE+1
            C.CURDEN[IWDG-1]=C.CURDM[IWDG-1]*0.6

            if(C.ACOND[IWDG-1]<1.E-8):
                BBSTRT=False
                C.ACOND[IWDG-1]=RIDI/C.CURDEN[IWDG-1]/C.FABOOS[IWDG-1]

            C.XREL[3+IWDG-1]=1*C.ACOND[IWDG-1]
        
        #WINDING DEFINED
        else:
            #Determine area
            #Area given
            if(C.AARR[60+IWDG-1]>1.E-8):
                C.ACOND[IWDG-1]=C.AARR[60+IWDG-1]/1.E+6
            
            #Area not given
            else:
                C.CURDEN[IWDG-1]=1.E+6*C.AARR[50+IWDG-1]
                C.ACOND[IWDG-1]=RIDI/C.CURDEN[IWDG-1]/C.FABOOS[IWDG-1]

        C.XA[3+IWDG-1]=C.ACOND[IWDG-1]
    
    if(C.NFREE>0): C.BBOPTI=True

    #Initialisation of the C.GREL-vector
    for IG in range(1,97):
        C.G[IG-1]=0
        C.GREL[IG-1]=0
    #Allocation of values to the C.GREL-vector
    #Start of the allocation block
    FACTOR=1.E+2
    if(C.PLOADM>0): 
        C.GREL[0]=C.PLOADM/FACTOR
    if(C.PNOLOM>0): 
        C.GREL[1]=C.PNOLOM/FACTOR
    if(C.BBDLI): 
        C.GREL[2]=((C.DCOMIN+C.DCOMAX)/2.)/FACTOR
    C.GREL[3]=0
    C.GREL[4]=C.HTANKM/FACTOR
    if(C.BBHLI):
        C.GREL[5]=C.HLMBMA/FACTOR
    C.GREL[6]=C.BTANKM/FACTOR
    C.GREL[7]=C.RLTNKM/FACTOR
    C.GREL[8]=C.GTRPM/FACTOR   
    if(C.SOUNDM>0): C.GREL[9]=C.SOUNDM/FACTOR

    # Equality needed for fixed reactance

    if(not C.BBREA):
        C.GREL[10]=(-1)*C.USHORE/FACTOR
    C.GREL[11]=C.BLTOPM/FACTOR        

    #End of the allocation block    

    #Allocation of the C.GREL-vector for each winding

    for IWDG in range(1,1+C.NWILI):
    #Allocate the C.GREL-vector   
    
    #If the conductor RD is given  
        if(C.BBCURD[IWDG-1]):
            C.GREL[13+3*(IWDG-1)-1]=C.CURDM[IWDG-1]/FACTOR
            C.GREL[14+3*(IWDG-1)-1]=(-1)*C.PRESSM[IWDG-1]/FACTOR
            C.GREL[15+3*(IWDG-1)-1]=C.TENSM[IWDG-1]/FACTOR

    #Allocation of optimisation parameters to LMIN

    # Start of the optimisation parameter block
    C.IOPT=1
    if(BBSTRT):  C.IOPT=2
    EX=float(-C.IOPT-2)
    if(C.IOPT>2): C.FEPS=0
    C.FEPS=0.001
    EX=float(1-C.IOPT)
    C.AF=0.1
    C.DRV=0.01
    
    EX=float(-C.IOPT)
    if(C.EPS==0): C.EPS=min(0.001,10**(EX))
    return
