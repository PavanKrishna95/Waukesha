#Assigns values to topoil temp.rise over 30 deg ambient
#which is used for calculation of the core.
#No. of cooling ducts set to 0 if guided oil flow used.
#( Mean oil temperature rises )

def PRETEM(AARR):
    print("start of PRETEM")

#Allocation of values to certain temperature variables.    

#Start of the allocation block.
    DTSNN=AARR[155]-18
    DTSNF=AARR[155]-25
    DTSFF=AARR[155]-18
    if(AARR[109]>0.1): DTSNN=AARR[109]
    if(AARR[119]>0.1): DTSNF=AARR[119]
    if(AARR[129]>0.1): DTSFF=AARR[129]

    print("end of PRETEM")
    return (DTSNN,DTSNF,DTSFF)


    #End of the allocation block.


