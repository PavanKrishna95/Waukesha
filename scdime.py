#Title:Calculate the actual short-circuit tangential
#      stresses appearing for those cases which are dimensioning.
#      The dimensioning cases will be determined in routine "DIMSCC".
from scstre import SCSTRE
def SCDIME(BBOUT):
    import com as C
    print("\n")
    print("start of SCSTRE")
    #DECLARATIONS


    #END OF DECLARATIONS

    #INITIALIZATIONS
    for IWDG in range(1,1+C.NWILI):
        C.STRWMM[IWDG-1]=0
        C.STRWMP[IWDG-1]=0
    
    #Determine No. of taps
    
    NTAPS=4

    #For each terminal
    for JTML in range(1,1+min(C.NG,3)):
        #Adjust the no of taps

        #Only for the regulated terminal
        if(C.BBVR[JTML-1]):
            if((C.NXSTEP[JTML-1]==C.NPSTEP[JTML-1])or (C.NXSTEP[JTML-1]==C.NMSTEP[JTML-1])or(C.NXSTEP[JTML-1]==0)):
                NTAPS=3

    #Calculate stresses

    # Non- regulated trafos and  "CFR"
    if(not C.BBVFR):
        #For each tap
        for ITAP in range(1,1+NTAPS):
            #If C.BBSCI(ITAP)    
            #Calculate stresses         
            if(C.BBSCI[ITAP-1]):
                for JTAP in range(1,1+NTAPS):
                    #If C.BBSCJ(ITAP)
                    #Calculate stresses
                    if(C.BBSCJ[JTAP-1]):
                        for KTAP in range(1,1+NTAPS):
                            #If C.BBSCK(ITAP)
                            #Calculate stresses
                            if(C.BBSCK[KTAP-1]):
                                I1=ITAP
                                J1=JTAP
                                K1=KTAP
                                ##Calculate stresses
                                SCSTRE(I1,J1,K1,BBOUT)

    else:
        for JTAP in range(1,1+NTAPS):
            J1=JTAP

            #Calculate stresses
            if(C.BBSCJ[JTAP-1]): SCSTRE(1,J1,J1,BBOUT)      

    print("\n")
    print("end of SCSTRE")                              

    return


                       

