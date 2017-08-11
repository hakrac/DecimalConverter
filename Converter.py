import sys

result = ""

decimal = input("Type in a new decimal number: ")
try: 
	decimalint = int(decimal)
except ValueError:
	print("Sorry, it has to be a number")
	sys.exit()

#calculation

remainder = decimalint % 2
y = decimalint / 2 
decimalint = y
result += str(int(remainder))

while int(y) > 0:
	remainder = decimalint % 2
	y = decimalint / 2
	decimalint = y
	result += str(int(remainder))	 

print(decimal +" is {}".format(result[::-1]))
