age=int(input("enter the age:"))
number=age
fact=1

while(age>0):
	fact=fact*age
	age=age-1
else:
	print('Python while loops have a redundant else')
print('factorial of your age is:',fact)
