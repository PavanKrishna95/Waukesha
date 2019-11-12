
''' Title: Core Stockings of ASECOND band
            according to ZK-TA 4610-115 '''
import numpy
def ASEC(DCOR,HLIMB,ACCTR):

    DY=DCOR/numpy.sqrt(2.)

    ''' Shrinking-tape '''

    RLKRMC=(HLIMB-120.)/25.*numpy.pi*DCOR*1.E-3
    RLKRMO=RLKRMC*DY/DCOR

    ''' Crepe paper '''

    RMC=6./15.*(HLIMB-120.)*numpy.pi*DCOR*1.E-6
    RMO=RMC*DY/DCOR

    ''' Number of ASECOND-layers in the limb-centre '''
    DKLP=[0.,0.]
    DKHLP[0]=DCOR

    for I in range(1,3):
        DKHLP[1]=DCOR
        DKX=DKHLP[I-1]
        if(I ==1.):
            D1K=5.26
            D2K=1.67
            D3K=1.50
        else:
            D1K=4.21
            D2K=0.95
            D3K=1.20

        N1X=ACCTR*HLIMB*HLIMB*D1K*1E-7+0.99999
        N1Y=ACCTR*HLIMB*DKX*D2K*1E-6+0.99999
        N1Z=ACCTR*HLIMB*HLIMB*HLIMB/DKX*D3K*1E-7+0.99999
        N1 =max(N1X,N1Y,N1Z,2)

        ''' Number of ASECOND-layers at the end of the cylinder '''

        if(I == 1.):
            D4K=1.93
        else:
            D4K=0.96
        
        N2=ACCTR*DKX*DKX*HLIMB*D4K*1E-9+0.99999
        N2=max(N1,N2)

        ''' Corresponding Thicknesses '''

        T1 =0.5*N1
        T2 =0.5*N2

        DKHLP[1]=DY
        DKX=DKHLP[I-1]
        if(I == 1):
            N1C=N1
            N2C=N2
            T1C=T1
            T2C=T2
            RLCC=numpy.pi*DKX*((HLIMB-120.)/60.*N1C+5.*(N2C-N1C))*1.E-3
        elif(I == 2):
            N1O=N1
            N2O=N2
            T1O=T1
            T2O=T2
            RLCO=numpy.pi*DKX*((HLIMB-120.)/60.*N1O+5.*(N2O-N1O))*1.E-3

    return (N1C,N2C,T1C,T2C,RLCC,RLKRMC,RMC,N1O,N2O,T1O,T2O,RLCO,RLKRMO,RMO)
