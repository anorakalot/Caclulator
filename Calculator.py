# add subtract multiply divide 
def main():
	try:
		a=float(input("first number..."))
		c =input("which operation (m = multiply a = add s = subtract d = divide)")
		b=float(input("second number..."))
	except ValueError:
		print("not a valid number")
		main()

	if c == 'm':
		multiply(a,b)
	elif c == 'a':
		add(a,b)
	elif c == "s":
		subtract(a,b)
	elif c == "d":
		divide(a,b)
	else:
		print("what the FUDGE! (not a valid operation")
		main()



def divide(a,b):
	print(a/b)
	print ("remainder is" + a%b)
	input('...')
	main()
	
def add(a,b):
	print(a+b)
	input('...')
	main()
	
def subtract(a,b):
	print(a-b)
	input('...')
	main()
	
def multiply(a,b):
	print(a*b)
	input('...')
	main()
	
if __name__ == "__main__":
	main()

