import numpy
def SNOLO(TYP,BLIMBP,FREQ,OKF,SBF,ISTGRD,GB1,GB2,GO,GH,BLADN):
    
    print("Starting of SNOLO")
    
    #DECLARATIONS
    SSP1=[0 for i in range(3)]
    SSP2=[0 for i in range(5)]
    SSP3=[0 for i in range(3)]
    SSPH11=[0 for i in range(3)]
    SSPH12=[0 for i in range(5)]
    SSPH13=[0 for i in range(3)]
    SSPH21=[0 for i in range(3)]
    SSPH22=[0 for i in range(5)]
    SSPH23=[0 for i in range(3)]
    #END OF DECLARATIONS

    #Coefficients for specific magnetising losses [Limb and Yoke]
    # Constant term first
    SSP1[1-1]= 0.88778    
    SSP1[2-1]=-0.92500007 
    SSP1[3-1]= 0.75000003 

    SSP2[1-1]= 355.98739  
    SSP2[2-1]=-975.50703  
    SSP2[3-1]=1004.1630   
    SSP2[4-1]=-459.88116  
    SSP2[5-1]=  79.285748 

    SSP3[1-1]= 1085.6455  
    SSP3[2-1]=-1202.1996  
    SSP3[3-1]=  333.99989 

# Corner losses for 1-phase cores and the T-core

    SSPH11[1-1]= 0.0626    
    SSPH11[2-1]= 1.5333336 
    SSPH11[3-1]=-0.22222236

    SSPH12[1-1]=  463.08928
    SSPH12[2-1]=-1252.4051 
    SSPH12[3-1]= 1302.5710 
    SSPH12[4-1]= -618.75868
    SSPH12[5-1] = 113.71649

    SSPH13[1-1]= 7077.4378 
    SSPH13[2-1]=-7797.5977 
    SSPH13[3-1]= 2151.9994 

# Corner losses for the TY-3 Core

    SSPH21[1-1]=0         
    SSPH21[2-1]=1.95938    
    SSPH21[3-1]=0         

    SSPH22[1-1]=  5640.5044
    SSPH22[2-1]=-15359.5830
    SSPH22[3-1]= 15684.7110
    SSPH22[4-1]= -7123.4939
    SSPH22[5-1] = 1215.8733

    SSPH23[1-1] =18535.248 
    SSPH23[2-1]=-20449.994 
    SSPH23[3-1] = 5649.9984

    RK2     = 1.13     


    SB1=0
    SB2=0
    SO=0
    SH=0  

    if(BLADN==4):
        RK3=1.2
    else:
        RK3=1

    BBSL= (TYP>=7)

    if(BLIMBP>1.8):
        SB1=GB1*numpy.polyval(SSP3[::-1],BLIMBP)
        SO=GO*numpy.polyval(SSP3[::-1],BLIMBP)
        SO=GO*numpy.polyval(SSP3[::-1],BLIMBP/OKF)
        if(BBSL): SB2=GB2*numpy.polyval(SSP3[::-1],BLIMBP/SBF)

        if(TYP==10):
            SH=GH*numpy.polyval(SSPH23[::-1],BLIMBP)
        else:
            SH=GH*numpy.polyval(SSPH13[::-1],BLIMBP)
    elif(BLIMBP>=1.3):
        SB1=GB1*numpy.polyval(SSP2[::-1],BLIMBP)
        SO=GO*numpy.polyval(SSP2[::-1],BLIMBP/OKF)
        if(BBSL):  SB2=GB2*numpy.polyval(SSP2[::-1],BLIMBP/SBF)

        if(TYP==10):
            SH=GH*numpy.polyval(SSPH22[::-1],BLIMBP)
        else:
            SH=GH*numpy.polyval(SSPH12[::-1],BLIMBP)
    else:
        SB1=GB1*numpy.polyval(SSP1[::-1],BLIMBP)
        SO=GO*numpy.polyval(SSP1[::-1],BLIMBP/OKF)
        if(BBSL): SB2=GB2*numpy.polyval(SSP1[::-1],BLIMBP/SBF)

        if(TYP==10):
            SH=GH*numpy.polyval(SSPH21[::-1],BLIMBP)
        else:
            SH=GH*numpy.polyval(SSPH11[::-1],BLIMBP)

    SO=SO*RK2
    SH=SH*RK3
    SNOLO=(SB1+SB2+SO+SH)

    if(FREQ>55):
        SNOLO=SNOLO*1.25
    else:
        SNOLO=SNOLO*1.04

    #Correction for HI-B, ZDKH, PLJT and ARMS    

    if((ISTGRD==2)or(ISTGRD==3)or(ISTGRD==4)or(ISTGRD==5)):
        SNOLO=SNOLO*0.7
    
    print("ending of SNOLO")
    
    return SNOLO    
