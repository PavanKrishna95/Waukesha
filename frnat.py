from brum import BRUM
def FRNAT(TYP,FREQ,DCORI,PLIMBI,HLIMBI):
    print("Starting of FRNAT")
    
    FRNAT1=0
    FRNAT2=0
    
    
    BBLIMT=lambda X,Y:abs(X*FREQ-Y)<=10
    BBRESO=False
    if(TYP != 3):
        FG=2850*DCORI/(HLIMBI+DCORI)**2*(1-0.45*PLIMBI/(HLIMBI+DCORI))
        for I in range(2,7,2):
            R=I
            if(BBLIMT(R,FG)): BBRESO=True
    else:
        FRNAT1,FRNAT2=BRUM(round(DCORI*1000),round(HLIMBI*1000))

        for I in range(2,7,2):
            R=I
            if(I<4):
                if(BBLIMT(R,FRNAT1) or BBLIMT(R,FRNAT2)): BBRESO=True
            else:
                if(BBLIMT(R,FRNAT1)): BBRESO=True   
    print("ending of FRNAT")
                
    return (BBRESO,FRNAT1,FRNAT2)                         
