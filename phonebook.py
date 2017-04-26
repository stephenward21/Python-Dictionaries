# import stuff
import os
# Main loop

phonebook_data = [
    {
        "name": "Melissa",
        "number": "404-235-5428"
    },
    {
        "name": "Joe",
        "number": "404-235-2125"
    },
    {
        "name": "Mike",
        "number": "770-134-2229"
    },
    {
        "name": "Igor",
        "number": "770-233-3461"
    }
]



def look_up(name):
	for i in phonebook_data:
		if i['name'] == name:
			print (i['number'])


def search(name_input):
	for name in phonebook_data:
		if ['name'] == name_input:
			return number


def searcher(number_input):
	for number in phonebook_data:
		if ['number'] == number_input:
			return number_input ['name']
			
	# for (name,number) in phonebook_data:
	# 	if name == search_input:
	# 		return number	#number is the same as phonebook_data["name"]
	# 	elif number == search_input:
	# 		return name
			

while 1:
	print """Electronic Phone Book
		=====================
		1. Look up an entry
		2. Set an entry
		3. Delete an entry
		4. List all entries
		5. Search for an entry
		6. Quit
	"""
	user_input = raw_input("What do you want to do (1-6)? ")
	
	if (user_input == "1"):
		name = raw_input("Please enter a name:")
		look_up(name)

	elif (user_input == "2"):
		new_name = raw_input("name: ")
		new_number = raw_input("number: ")
		phonebook_data.append({'name':new_name, 'number':new_number})
		# new_entry = [{new_name: new_number}]
		print phonebook_data

	elif (user_input == "3"):
		del_name = raw_input("name: ")
		del_entry = {'name':del_name}
		phonebook_data.remove(del_entry)
		print phonebook_data
		
	elif (user_input == "4"):
		print phonebook_data

	elif (user_input == "5"):
		search_input = raw_input("Enter name or number: ")
		print search(search_input)

	elif (user_input == "6"):
		print "Quit"
		break
		


	# option 2
	# try:
	# 	convert_user = int(user_input)
	# except: ValueError
	# os.system("clear")
	# 	print "You must enter a number!\n"
	# else:
	# 	# i tried to convert it and succeeded!
	# 	if (convert_user == 1):
	# 		print ("You chose 1")
	# 	elif (convert_user == 6):
	# 		break



