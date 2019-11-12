def LMINCA(VALUE,NA,NB,NCYC):
    from lmin import LMIN
    from funk import FUNK
    import com as C

    PARAM=[0 for i in range(25)]
    
    HV=[0 for i in range(7574)]
    PARAM[0]=2

    PARAM[2]=C.BARR[35]
    PARAM[5]=0.05
    PARAM[6]=0.2
    PARAM[7]=0.1
    PARAM[12]=C.BARR[36]
    PARAM[21]=10
    C.BBOOVN=False
    NF=0

    C.XA,VALUE,NCYC,NF,HV,PARAM,ICONV=LMIN(NA,NB,C.XA,VALUE,C.XREL,C.GREL,C.EPS,\
               C.FEPS,C.DRV,C.AF,C.NFMX,NCYC,NF,-abs(C.ITR),HV,PARAM)
    a=0

    if(ICONV>=1):
        #Calculate the function
        a,C.XA,C.G,VALUE=FUNK(C.XA)
        if(a==1):
            return (VALUE,NCYC)

        #Re-optimise the function

        #IF Optimisation OK or MNL79 or later and C.CPUIND <> 0

        if(ICONV>=2 or(C.MNLY>= 79 and C.CPUIND!=0)):

            if(C.CLOSSV>0):
                FACTOR=1+C.CPUIND
                NF1=NF
                if(C.MNLY<79): FACTOR=1

                #Re-optimise

                if(FACTOR>=1):
                    C.VALUEM=FACTOR*C.VALUEO
                    C.BBOOVN=True
                    C.GREL[4]=C.VALUEM/100
                    C.AVALUE=C.COST
                    C.AF=-0.01+0.5*C.CPUIND

                    print( 'Optimising the manufacturing price')

                    C.XA,VALUE,NCYC,NF,HV,PARAM,ICONV=LMIN(NA,NB,C.XA,VALUE,C.XREL,C.GREL,C.EPS,\
               C.FEPS,C.DRV,C.AF,C.NFMX,NCYC,NF,-abs(C.ITR),HV,PARAM)
                    C.XA,VALUE,C.G,a=FUNK(C.XA)   

                    if(a==1):
                        return (VALUE,NCYC)
                    C.VALUEF=C.COST+C.CLOSSV
            #         WRITE (*,210) NF,C.VALUEF,C.CTROVN,C.COST,C.CLOSSV
             #      CALL NPAGE(8)
             #      WRITE (C.JFC,210) NF,C.VALUEF,C.CTROVN,C.COST,C.CLOSSV
             #      NF=NF+NF1
             #      WRITE (*,121) 'Dcore',1.E+3*C.XA(1),
    # &                           'Limb height',1.E+3*C.XA(2),
    # &                           'Flux density',C.XA(3)
#CCCC               WRITE (*,122) (1.E+6*C.XA(I),I=3+1,3+C.NWILI)
#CCCC               WRITE (*,123) (1.E+3*C.HPART(IWDG),IWDG=1,C.NWILI)
#CCCC               WRITE (*,124) (1.E+3*C.BPART(IWDG),IWDG=1,C.NWILI)
#CCCC               WRITE (*,125) (C.FILLF(IWDG),IWDG=1,C.NWILI)
#CCCC               WRITE (*,126) (1.E+3*C.RRWDG(IWDG),IWDG=1,C.NWILI)
#                   WRITE (C.JFC,121) 'Dcore',1.E+3*C.XA(1),
#     &                             ' Limb height',1.E+3*C.XA(2),
#     &                             ' Flux density',C.XA(3)
#CCCC               WRITE (C.JFC,122) (1.E+6*C.XA(I),I=3+1,3+C.NWILI)
#CCCC               WRITE (C.JFC,123) (1.E+3*C.HPART(IWDG),IWDG=1,C.NWILI)
#CCCC               WRITE (C.JFC,125) (C.FILLF(IWDG),IWDG=1,C.NWILI)
#CCCC               WRITE (C.JFC,126) (1.E+3*C.RRWDG(IWDG),IWDG=1,C.NWILI)

                    #PLIMIT[1]

    return VALUE,ICONV,NF,NCYC
