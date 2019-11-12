import numpy,math
def SOUNDP(TYP,DCORI,PLIMBI,HLIMBI,ISTGRD,BLIMB,FREQ,JFC):
    print("Starting of SOUNDP")
    
    C=[-2,0,0,0,0,0,-2,-2,0,0]

    #Check the coretype TYP

    if((round(TYP)<1)or(round(TYP)>10)):
        TYP=3
        JFC='WARNING (SOUNDP): Illegal core type code,'
        JFC='                : Core type T assigned.'
        print('WARNING (SOUNDP): Illegal core type code,')
        print('                : Core type T assigned.')

    #Size variable
    CS = 20*math.log10(HLIMBI * PLIMBI * numpy.sqrt(DCORI))

    #Flux variable
    if(BLIMB >=1.6 ):
        CB = 0.061*BLIMB**9
    else:
        CB = 23.6*BLIMB - 33.6

    #Frequency variable
    CF = 45*math.log10(FREQ/50.)

    #Quality variable

    if(ISTGRD==2):
        CQ=0.8
    elif(ISTGRD==3):
        CQ=0
    elif(ISTGRD==4):
        CQ=3
    else:
        CQ=7

    SOUNDP = 68.4+CS+CB+CF+CQ+C[round(TYP)-1]  
    print("ending of SOUNDP")

    return SOUNDP
