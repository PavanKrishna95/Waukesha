
''' Title:  Calculates the Yoke reduction for the LTS core '''

def LTSOK (B,AN):

    N=round(AN)

    if(B[N-1] == B[N-2] or B[N-2] == B[N-3]):
        B[N-1]=B[N-4]
        B[N-2]=B[N-4]
        B[N-3]=B[N-4]
    else:
        B[N-1]=B[N-3]
        B[N-2]=B[N-3]

    return B
