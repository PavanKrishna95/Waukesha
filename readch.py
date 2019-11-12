
#Title:Read cost files from external files.
#THIS ROUTINE WILL FIND THE COST FILE,
#        READ IN COST CONSTANTS (R79,C75), CURRENCY (CHCOST),
#        AND HEAD FOR COST FILE (RUBCH).
#MNL.YEAR
from readcost import READCOST
import json
def READCH(MNLY,MNL,RUBCH,CHCOST):
    import common as CM

    
    with open("cost-file-structured.json") as json_file:
        json1=json.load(json_file)
    BB79  = (MNLY >=79 and MNLY < 91)
    BB79=True
    
    if(BB79):

#     MNL79 
#   READ(IF30,2010,END=50) (RUBCH(I), I=1,15) 
        #reading the costfile json for years 79-91
        for I in range(146):
            READCOST(json1,I)

        #''' CALCULATION OF WORKSHOPTIMES ? '''
        #CHLP=' '
        #''' READ(MNL, 82,END=999,ERR=999 ) CHLP
        

        #if(CHLP == 'T'):

         #   HOUR-CALCULATION'''
            #for  I in range(146):
            #    CM.R79[2 ][I] = 0.
            #    CM.R79[3 ][I] = 0.
            #    CM.R79[4 ][I] = 0.
            #    CM.R79[5 ][I] = 0.
            #    CM.R79[7 ][I] = 1.
            #    CM.R79[12][I] = 0.
            #    CM.R79[13][I] = 0.
            #    CM.R79[14][I] = 0.
            #RUBCH[13] = 'HRS '

            CHCOST='      '
            CONCAT(CHCOST,0,RUBCH[13],0,4)

        else:
            pass

            

# MNL92 - FORMULAS
#*
#         READ(IF30,80,END=999,ERR=999)( RUBCH(I), I=1, 13)
#         READ(IF30,81,END=999,ERR=999)  CHCOST
#         READ(IF30,*,END=999,ERR=999)   CUC92(1), CUC92P(1)
#         READ(IF30,*,END=999,ERR=999)   CUC92(2), CUC92P(2)
#         READ(IF30,*,END=999,ERR=999)   CUC92(3), CUC92P(3)
#         READ(IF30,*,END=999,ERR=999)   FEC92(1), FEC92P(1)
#         READ(IF30,*,END=999,ERR=999)   FEC92(2), FEC92P(2)
#         READ(IF30,*,END=999,ERR=999)   FEC92(3), FEC92P(3)
#         READ(IF30,*,END=999,ERR=999)   FEC92(4), FEC92P(4)
#         READ(IF30,*,END=999,ERR=999)   OLC92, OLC92P
#         READ(IF30,*,END=999,ERR=999)   PNFDUC
#         READ(IF30,*,END=999,ERR=999)   PNFWIN
#         READ(IF30,*,END=999,ERR=999)   PNFYOK
# 80      FORMAT(13A4)
# 81      FORMAT(A6)'''
#            CONCAT(RUBCH(14),0,CHCOST,0,4)
#            ENDIF
#       GO TO 800 

#    C---------------------------------------------------------------
#C   Error during external file reading
# 999   WRITE(JFC,*)' *** ERROR **** during reading external cost file'
#       WRITE( * ,*)' *** ERROR **** during reading external cost file'
#       WRITE(JFC,*)' *** ERROR **** (missing data or no permission)'
#       WRITE( * ,*)' *** ERROR **** (missing data or no permission)'
#       WRITE(JFC,*)' *** ERROR **** FILE= ',FILECH
#       WRITE( * ,*)' *** ERROR **** FILE= ',FILECH
#       WRITE(JFC,*)'               '
#       WRITE( * ,*)'               '
#        STOP
#C---------------------------------------------------------------
# 800   REWIND IF30
#       CLOSE(IF30)

#   return

# Title:  Concatenates two character strings

def CONCAT(STRNG1,N,STRNG2,M,LENG):

#   Concatenate the strings 

    L1=max(LENG,1)
    N1=max(N,1)
    M1=max(M,1)
#   

    return
