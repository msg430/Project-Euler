import math

saved = 3*math.pi/2
identity = math.atan(0.75)

def verticalIntegral(x):
    height = 3 - (0.75*x)
    # altF = (0.5*(x-4)*math.log((x*x-(8*x)+16)/((x*x) - (8*x)+(height*height)+16)))
    # F = (height * math.atan((4-x)/height)) + (0.5*(x-4)*math.log((x*x-(8*x)+16)/((x*x) - (8*x)+(height*height)+16)))
    E = height*identity-(3*identity)-(3*math.atan(-3/x))+(0.5*x*math.log(((25/16)*x*x)/(9+(x*x))))
    # result = height*saved - F - E
    result = height * saved - E
    return(result)



firstPart = (-0.75*(4*4/2-(4*4))*math.atan(4/3))
secondPart = 4 - 4*math.log(16)
thirdPart = 4*(math.log(25)-1)
shortcut = (firstPart+secondPart+thirdPart)/2/math.pi/6

A = -6*identity
print(A)
B = 3*(math.log(125/27)+4*math.atan(3/4))
print(B)
C = 4*(2*math.log(5)-1)
print(C)
D = 0.25*(16-(16+9)*math.log(16+9))-0.25*(-9*math.log(9))
print(D)
other = (A+B+C+D)/12/math.pi

print(0.75-shortcut-other)




# integrals = []
# prior = 0
# step = 1
# switch = True
# while switch:
#     step = 0.1 * step
#     totalLength = 0
#     totalSum = 0
#     for n in range(1, int(4*(1/step))):
#         totalLength += 3 - (0.75*n*step)
#         totalSum += verticalIntegral(n*step)
#     integral = (totalSum/totalLength)/2/math.pi - shortcut
#     print('for step:', step, 'integral is:', integral)
#     if abs(integral-prior) < 0.0000001:
#         switch = False
#     integrals.append(integral)
#     prior = integral
#
# print(integrals)
