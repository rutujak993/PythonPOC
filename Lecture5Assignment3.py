#WAP to accept three numbers from user and print minimum of them.

num1, num2, num3 = eval(input('Please enter three numbers: '))
print ('The minimum of the three numbers is : ')
if	num1 < num2 and num1 < num3 :
	print (num1)
elif (num2 < num3) :
	print (num2)
else :
	print (num3)