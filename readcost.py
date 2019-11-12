def READCOST(json,num):
    import common as CM
    J=0
    n=0
    list=["k1","k2","k3","k4","k5","k6","k7","k8","k9","k10","k11","k12","k13","k14","k15"]
    while(J<15):
        dict1=json["payload"][num]
        CM.R79[J][num]=dict1[list[n]]
        J=J+1
        n=n+1
    return
