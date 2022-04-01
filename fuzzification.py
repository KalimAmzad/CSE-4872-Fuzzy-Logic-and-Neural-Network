#Fuzzy Partition 
def partition(x):
    NL = 0;  NM = 0; NS = 0; ZE = 0; PS = 0; PM = 0; PL = 0
    
    if x> 0 and x<60:
        NL = openLeft(x,30,60)
    if x> 30 and x<90:
        NM = triangular(x,30,60,90)
    if x> 60 and x<120:
        NS = triangular(x,60,90,120)
    if x> 90 and x<150:
        ZE = triangular(x,90,120,150)
    if x> 120 and x<180:
        PS = triangular(x,120,150,180)
    if x> 150 and x<210:
        PM = triangular(x,120,150,180)
    if x> 180 and x<240:
        PL = openRight(x,180,210)
 
    return NL,NM,NS,ZE,PS,PM,PL;

# Getting fuzzy values for all the inputs for all the fuzzy sets
NLSD,NMSD,NSSD,ZESD,PSSD,PMSD,PLSD = partition(Speed)
NLAC,NMAC,NSAC,ZEAC,PSAC,PMAC,PLAC = partition(Acceleration)

# Display the fuzzy values for all fuzzy sets
outPut = [[NLSD,NMSD,NSSD,ZESD,PSSD,PMSD,PLSD],
          [NLAC,NMAC,NSAC,ZEAC,PSAC,PMAC,PLAC]]
print("The fuzzy values of the crisp inputs")
print(["NL","NM","NS","ZE","PS","PM","PLSD"])
print(np.round(outPut,2))
