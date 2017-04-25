import os

def look_up(inputName):
	for (name,number) in phonebook_data.iteritems():
		if name == inputName:
			return number	#number is the same as phonebook_data["name"]

def search(search_input):
	for (name,number) in phonebook_data.iteritems():
		if name == search_input:
			return number	#number is the same as phonebook_data["name"]
		elif number == search_input:
			return name


# Main loop
while 1:	#This always means while True; end by adding break
	print """\nElectronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Search for an entry
6. Quit\n"""
	user_input = raw_input("What do you want to do (1-6)? ")
	#raw_imput comes in as a string, the response will be a number
	try:
		convert_user = int(user_input)
	except ValueError:
		print "You must enter a number!\n" #This will force a return carriage
		os.system("clear") #This will pass any Linux command you want
	else:
		#Tried to convert and succeeded
		if (convert_user == 1):
			search_name = raw_input("Enter name: ")
			print look_up(search_name)
		elif (convert_user == 2):
			new_entry_name = raw_input("What is new user's name? ")
			new_entry_num = raw_input("What is new user's number? ")
			phonebook_data[new_entry_name] = new_entry_num
			print phonebook_data
		elif (convert_user == 3):
			del_entry = raw_input("Which name would you like to delete? ")
			del phonebook_data[del_entry]
			print phonebook_data
		elif (convert_user == 4):
			print phonebook_data
		elif (convert_user == 5):
			search_answer = raw_input("Enter name or number to search: ")
			print search(search_answer)
		elif (convert_user == 6):
			print "Bye."
			#user chose to quit, so leave the loop
			break