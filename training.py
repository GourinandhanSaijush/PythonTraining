# First program - Hello World
print("Hello World")

# Operators and Variables - Add Numbers
num1 = 1.5
num2 = 6.3
sum=num1+num2
print(sum)
#user inputs
num3= input('enter first number:')
num4= input('enter second number: ')
sum1=float(num3) +float(num4)
print(sum1) #Since, input() returns a string, we convert the string into number using the float() function. Then, the numbers are added.

# program to find square root
num1= int(input('enter number:'))
num_sqt=num1 ** 0.5
print(num_sqt) #square root using the ** exponent operator
#for complex and real numbers
num2=1+2j
import cmath
num_sqt1=cmath.sqrt(num2)
print(num_sqt1)# using the sqrt() function in the cmath (complex math) module.

# program to solve quadratic equation
#ax2 + bx + c = 0 is standard form 
a=1
b=5
c=6
d=(b**2)-(4*a*c)# calculate discriminant
# cmath module to perform complex square root. 
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)
print(sol1,sol2)

#simple variable swap using temp variable
x=5
y=10
temp=x
x=y
y=temp
print(x)
print(y)

