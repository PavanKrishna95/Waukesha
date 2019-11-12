
''' Title: Read external variables for calculation of
           no load losses, active and apparent. '''

def nlossr():
    
  
       open(15, file=FILE, form='formatted')
C
       REWIND(15)
C
C.. Read identifier for external no load data
       READ(15,80,END=98,ERR=98) LAMID
 80    FORMAT(A44)
C
       READ(15,*,END=98,ERR=98)
     &             PSPL1    ,  PSPL2    ,  PSPL3    ,
     &             PSPHD1   ,  PSPHD2   ,  PSPHD3   ,
     &             PSPHT1   ,  PSPHT2   ,  PSPHT3   ,
     &             PSPTY1   ,  PSPTY2   ,  PSPTY3   ,
     &             SSPL1    ,  SSPL2    ,  SSPL3    ,
     &             SSPHD1   ,  SSPHD2   ,  SSPHD3   ,
     &             SSPHT1   ,  SSPHT2   ,  SSPHT3   ,
     &             SSPTY1   ,  SSPTY2   ,  SSPTY3
C
       CLOSE(15)
       GO TO 99
C
  98   CALL FPRINT(2,BBERR,BBHELP,BBTS,JFC,
     &      'Reading external no loss parameters failed' )

  99   RETURN
       END
