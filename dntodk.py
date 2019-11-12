
''' Title: Difference between Nominal diameter and Net Diameter
           for the TA1 core. '''

def DNTODK(DNI,RMLMB,ACCTR,HLIMBI,CBBAND,TASEC,JFC):

    ''' DNI     Net Diameter (m)
        RMLMB   Mass of limbs (kg)
        ACCTR   Transport force in transverse direction (*G)
        HLIMBI  Limb Height (m)
        HLIMB   Limb Height (mm)
        CBBAND  Limb banding ASEC, PRESS '''

    BBERR = False
    
    EA = 4250.
    EP = 1500.
    PI  =3.141592654
    GFORCE=9.81
    ''' Convert to (mm) '''
    
    DN = DNI*1000.
    HLIMB = HLIMBI*1000.

    if (DN > 600.):
        TOL = 6.
    else:
        TOL = 4.

    T2 = 0.
    TLPC = 0.

    if (CBBAND == 'ASEC'):
        N1=((RMLMB/3.*GFORCE*ACCTR*HLIMB*HLIMB*167.)/
            (PI*EA)+DN*DN*DN*DN)**0.25-DN
        N1 = max(N1,2.)
        N2 = N1 + 1.
        T1 = 0.5*N1
        T2 = 0.5*N2
        TASEC = T1/1000.
    elif (CBBAND == 'PRESS'):
        TLPC = ((RMLMB/3.*GFORCE*ACCTR*HLIMB*HLIMB*167.)/
                (PI*EP)+DN*DN*DN*DN)**0.25-DN
        TASEC = 0.
    else:
        TASEC = 0.
        ''' WRITE(JFC,*) 'Error in DNtoDK: Illegal limb banding ',CBBAND '''
        BBERR = True

    if (BBERR):
        DNTODK = 0.
        BBERR = False
    else:
        T = max(T2,TLPC)
        A = round(2.*(0.5+T)+TOL)
        DNTODK = A/1000.

    return DNTODK
