import math

shape=0
area=0
side=0
length=0
width=0
height=0
base=0
radius=0

print('Area Calculator 📐')

print('1) Triangle')
print('2) Rectagle')
print('3) Square')
print('4) Circle')

shape=int(input('Which shape: '))

if shape==1:
    height=int(input('Height: '))
    base=int(input('Base: '))
    area=(height*base)/2
    print('The area is ' + str(area))
elif shape==2:
    length=int(input('Length: '))
    width=int(input('Width: '))
    area=length*width
    print('The area is ' + str(area))
elif shape==3:
    side=int(input('Side: '))
    area=side**2
    print('The area is ' + str(area))
elif shape==4:
    radius=int(input('Radius: '))
    pi=math.pi
    area=pi*(radius**2)
    print('The area is ' + str(area))
else:
    print('Error')