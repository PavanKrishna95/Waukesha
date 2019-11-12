#Title: Assigns values to diverse variables
#for calculation of the tank
#TANK PARAMETERS
#. -----------------------------------------------------
#. KTAN79  .  TYPE                  .  KTANK
#. .......................................................
#. 1       .  Oval                  .  3, 4
#. 2       .  Rectangular           .  2
#. 3       .  TAA - Vacuum proof    .  10
#. 4       .  TAA - Non-vacuum proof.  11
#. 5       .  TBA - Rectangular     .  12
#. 5       .  TBA - Oval            .  13
#. 5       .  TBA - One straight end.  14
#. 6       .  Curved + others       .  1, 5, 6, 7, 8, 9
#. .......................................................
#.
#. KTAN79 is used for the cost calculation in MNL79
#. F1TANK,F2TANK,F3TANK are geometrical factors used to
#. calculate tank volume & areas based on total dimensions.

def PRETAN(KTANK):
    print("start of PRETAN")
    #Start of the declarations block.
    F1=[1,1,1,1,0.97,0.97,0.97,0.97,0.97,1,1,1,1,1]
    F2=[0,0,-0.214,-0.104,-0.101,-0.208,-0.208,-0.208,-0.208,-0.172,-0.172,0,-0.215,-0.107]
    F3=[0.57,1,0.57,0.785,0.785,0.57,0.57,0.57,0.57,0.657,0.657,1,0.570,0.785]

    IHLP=[6,2,1,1,6,6,6,6,6,3,4,5,5,5]

    #End of the declarations block.

    # Allocation of values to certain tank variables.

    #Start of the allocation block.

    KT=KTANK
    if(KT>14): KT=13
    if(KT<= 0): KT=13
    F1TANK=F1[KT-1]
    F2TANK=F2[KT-1]
    F3TANK=F3[KT-1]
    KTAN79=IHLP[KT-1]
    print("end of PRETAN")
    return (F1TANK,F2TANK,F3TANK,KTAN79)

    #End of the allocation block.