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

#print out letters for numeral system with a base of 10
if baseint > 10:
	if int(remainder) == 10:
		remainder = "a"
	elif int(remainder) == 11:
		remainder = "b"
	elif int(remainder) == 12:
		remainder = "c"
	elif int(remainder) == 13:
		remainder = "d"
	elif int(remainder) == 14:
		remainder = "e"
	elif int(remainder) == 15:
		remiander = "f"

y = decimalint / baseint
decimalint = y
result += str(remainder)

while int(y) > 0:
	remainder = decimalint % baseint

	if baseint > 10:
		if int(remainder) == 10:
			remainder = "a"
		elif int(remainder) == 11:
			remainder = "b"
		elif int(remainder) == 12:
			remainder = "c"
		elif int(remainder) == 13:
			remainder = "d"
		elif int(remainder) == 14:
			remainder = "e"
		elif int(remainder) == 15:
			remiander = "f"
	else:
		remainder = int(remainder)

	y = int(decimalint / baseint)
	decimalint = y
	result += str(remainder)

print(decimal +" is {}".format(result[::-1]))
