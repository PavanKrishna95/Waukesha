#Title:  Calculation of masses for cover

def COVMA(ACOV,KTAN79):
    #COVER
#      ACOV =     COVER AREA               (M2)
#      GCOVER =   COVER MASS
#
#      KTAN79 =   TANK CODE
#                 1 = OVAL TANK         TMY
#                 2 = RECTANGULAR TANK  TMY
#                 3 = TAA, VACUUM-PROOF
#                 4 = TAA, NOT VAKUUM-PROOF
#                 5 = TBA
#                 6 = OTHER TYPES , TMY

    CA=[172.6, 121.4, 160.9, 59.71, 110.85, 96.99]
    CB=[1.040, 1.148, 1.172, 1.394, 1.200, 1.230]

    
    GCOVER =  (CA[KTAN79-1] * ACOV**CB[KTAN79-1])*1.02
    return GCOVER

