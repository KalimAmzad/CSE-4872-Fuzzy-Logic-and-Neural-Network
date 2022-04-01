Speed = 120
Acceleration = 125

print("The speed input is: ", Speed)
print("The Acceleration input is: ", Acceleration)
print("\n")

#Functions for open left-Right fuzzyfication  
def openLeft(x,alpha, beta):
    if x<alpha:
        return 1
    if alpha<x and x<=beta:
        return (beta - x)/(beta - alpha)
    else:
        return 0
    
def openRight(x,alpha, beta):
    if x<alpha:
        return 0
    if alpha<x and x<=beta:
        return (x-alpha)/(beta - alpha)
    else:
        return 0

# Function for traingular fuzzyfication  
def triangular(x,a,b,c):
    return max(min((x-a)/(b-a), (c-x)/(c-b)),0)


