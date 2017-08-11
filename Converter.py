import sys

result = ""

decimal = input("Type in a new decimal number: ")
try:
	decimalint = int(decimal)
except ValueError:
	print("Sorry, it has to be a number")
	sys.exit()

base = input("Type in the base of the numeral system: ")
try:
	baseint = int(base)
except ValueError:
	print("Sorry, it has to be a number!")


#calculation

remainder = decimalint % baseint
y = decimalint / baseint
decimalint = y
result += str(int(remainder))

while int(y) > 0:
	remainder = decimalint % baseint
	y = decimalint / baseint
	decimalint = y
	result += str(int(remainder))

print(decimal +" is {}".format(result[::-1]))
