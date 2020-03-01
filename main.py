import add
import mul


print ("enter two integers")
a = int(input())
b = int(input())
print (" you entered two numbers: a = ", a, ", b = ", b, )
print("choose the operation:")
print ("1. addition")
print ("2. Multiplication")
c= int(input())
if (c==1):
	print(add.add(a,b))
elif (c==2):
	print(mul.mu.(a,b))
