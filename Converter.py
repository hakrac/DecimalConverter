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
if baseint == 17:
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
	elif int(remainder) == 16:
		remiander = "g"

if baseint == 16:
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

elif baseint == 15:
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

elif baseint == 14:
	if int(remainder) == 10:
		remainder = "a"
	elif int(remainder) == 11:
		remainder = "b"
	elif int(remainder) == 12:
		remainder = "c"
	elif int(remainder) == 13:
		remainder = "d"


elif baseint == 13:
	if int(remainder) == 10:
		remainder = "a"
	elif int(remainder) == 11:
		remainder = "b"
	elif int(remainder) == 12:
		remainder = "c"



elif baseint == 12:
	if int(remainder) == 10:
		remainder = "a"
	elif int(remainder) == 11:
		remainder = "b"


elif baseint == 11:
	if int(remainder) == 10:
		remainder = "a"

else:
	remainder = int(remainder)

y = int(decimalint / baseint)
decimalint = y
result += str(remainder)

while int(y) > 0:
	remainder = decimalint % baseint

	if baseint == 16:
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

	elif baseint == 15:
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

	elif baseint == 14:
		if int(remainder) == 10:
			remainder = "a"
		elif int(remainder) == 11:
			remainder = "b"
		elif int(remainder) == 12:
			remainder = "c"
		elif int(remainder) == 13:
			remainder = "d"


	elif baseint == 13:
		if int(remainder) == 10:
			remainder = "a"
		elif int(remainder) == 11:
			remainder = "b"
		elif int(remainder) == 12:
			remainder = "c"



	elif baseint == 12:
		if int(remainder) == 10:
			remainder = "a"
		elif int(remainder) == 11:
			remainder = "b"


	elif baseint == 11:
		if int(remainder) == 10:
			remainder = "a"

	else:
		remainder = int(remainder)


	
	y = int(decimalint / baseint)
	decimalint = y
	result += str(remainder)


#print out the result
print(decimal +" -> {}".format(result[::-1]))



start = input("New number(y/n) ")
if start.lower() == "y":
	pass
else:
	sys.exit()
