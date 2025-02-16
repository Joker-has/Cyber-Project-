
def printStrongNess(input_string): 
	
	n = len(input_string) 

	# Checking lower alphabet in string 
	hasLower = False
	hasUpper = False
	hasDigit = False
	specialChar = False
	normalChars = "abcdefghijklmnopqrstu"
	"vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
	
	for i in range(n): 
		if input_string[i].islower(): 
			hasLower = True
		if input_string[i].isupper(): 
			hasUpper = True
		if input_string[i].isdigit(): 
			hasDigit = True
		if input_string[i] not in normalChars: 
			specialChar = True

	# Strength of password 
	print("Strength of password:-", end = "") 
	if (hasLower and hasUpper and
		hasDigit and specialChar and n >= 8): 
		print("Strong") 
		print("The Lenght Of Password is :",n)
		
	elif ((hasLower or hasUpper) and
		specialChar and n >= 6): 
		print("Moderate") 
		print("The Lenght Of Password is :",n)
	else: 
		print("Weak") 
		print("The Lenght Of Password is :",n)

# Driver code 
if __name__=="__main__": 
	
	input_string = input( "Enter The Password : " )
	
	printStrongNess(input_string) 

