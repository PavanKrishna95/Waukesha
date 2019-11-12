
def NCDLTB(TYP,DCOR):

    NCD=0

    if (round(TYP)==10):
        if (DCOR >= 720. ): NCD=1
        if (DCOR >= 800. ): NCD=2
        if (DCOR >= 860. ): NCD=3
        if (DCOR >= 960. ): NCD=4
        if (DCOR >= 1025.): NCD=5
        if (DCOR >= 1125.): NCD=6
        if (DCOR >= 1225.): NCD=7
        if (DCOR >= 1325.): NCD=8
        if (DCOR >= 1365.): NCD=9
    else:
        if (DCOR >= 800. ): NCD=1
        if (DCOR >= 1025.): NCD=2
        if (DCOR >= 1145.): NCD=3
        if (DCOR >= 1325.): NCD=4

    NCDLTB=NCD

    return NCDLTB
