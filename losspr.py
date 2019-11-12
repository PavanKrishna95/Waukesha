def LOSSPR(ITAP2,JTAP2,KTML2,LTML2,MTML):
    import com as C
    #Declarations
    ARR1=[0 for i in range(9)]
    ARR2=[0 for i in range(9)]
    ARR3=[0 for i in range(9)]
    ARR4=[0 for i in range(9)]
    ACUR=[0 for i in range(9)]

    WTYPE1=["" for i in range(9)]
    
    
    C1=C.ZWOULI/1.E+3
    C2=1.E-3
    if(C.KCON[KTML2-1]==1 or C.KCON[KTML2-1]>10): C2=C2*C.SQR3
    C3=1.E-3
    if(C.KCON[LTML2-1]==1 or C.KCON[LTML2-1]>10): C3=C3*C.SQR3
    C4=1.E-3


    #   WRITE(C.JFC,1) KTML2,LTML2,AMIN1(C.SRATEP(KTML2),
    ## &              C.SRATEP(LTML2))*C1/1.E+3,
    # &              C.UN(KTML2,ITAP2)*C2,C.UN(LTML2,JTAP2)*C3
    #   WRITE(C.JFC,2)
    #   WRITE(C.JFC,3) C.PCU*C1,C.PED*C1,C.POED*C1,(C.PCU+C.PED+C.POED)*C1
    #   if (C.KWITYP(C.NWILI).EQ.5) THEN
    #      WRITE(C.JFC,5)
    #   ELSE
    #      WRITE(C.JFC,6)
    #   ENDIF

    # Prepare some data for the database
    C.UNTAP[ITAP2+4*(KTML2+LTML2-3)-1]=C.UN[KTML2-1][ITAP2-1]*C2
    C.UNTAP[12+ITAP2+4*(KTML2+LTML2-3)-1]=C.UN[LTML2-1][JTAP2-1]*C3

    
#C... Prepare the data for printout
#*#

#*
#C... Create the required character string
    for IWDG in range(1,1+C.NWILI):
        WTYPE1[IWDG-1]='    '
        ACUR[IWDG-1]=abs(C.CUR[IWDG-1])

        #CONCAT(WTYPE[IWDG-1],1,C.NCOL[IWDG-1],1,1)
        ACUR[IWDG-1]=abs(C.CUR[IWDG-1])
        if (ITAP2==1):
            C.CURPRT[IWDG-1][MTML-1]=ACUR[IWDG-1]
        elif (ITAP2==2):
            C.CURMNT[IWDG-1][MTML-1]=ACUR[IWDG-1]
        elif (ITAP2==3) :
            C.CURMXT[IWDG-1][MTML-1]=ACUR[IWDG-1]
        elif (ITAP2==4) :
            C.CURSPT[IWDG-1][MTML-1]=ACUR[IWDG-1]

        ARR1[IWDG-1]=ACUR[IWDG-1]/C.ACOND[IWDG-1]*C4*C4
        ARR2[IWDG-1]=(C.PCUW[IWDG-1]+C.PEDW[IWDG-1])*C4
        ARR3[IWDG-1]=C.PCUW[IWDG-1]*C4
        ARR4[IWDG-1]=C.PEDW[IWDG-1]*C4    







    #End of the declarations block.