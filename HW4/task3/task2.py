from .task2utils import *


def task2(firstname, lastname, email, phone, birth, address, apt, city, state, zipcode):
	phone = phone.split('-')
	birth = birth.split('/')
	email = email.split('@')
	email = email[0].split('_')
	phone1 = str(phone[0])
	phone2 = str(phone[1])
	phone3 = str(phone[2])
	month = str(birth[0])
	day = str(birth[1])
	year = str(birth[2])
	short_year = str(year[2]) + str(year[3])
	address = address.split(' ')

	numbers = [
		[month, "birth month"],
		[day, "birth day"],
		[year, "birth year"],
		[short_year, "birth year"],
		[phone1, "phone"],
		[phone2, "phone"],
		[phone3, "phone"],
		[zipcode, "zip code"]
	]
	words = [
		[firstname.lower(), "first name"],
		[lastname.lower(), "last name"],
		[city.lower(), "city"],
		[state.lower(), "state"]
	]
	email.extend(["email"])
	words.append(email)
	temp = []
	for item in address:
		item = str(item)
		if item.isdigit():
			numbers.append([item, "address"])
		else:
			temp.append(item.lower())
	temp = ''.join(temp)
	words.append([temp, "address"])

	if apt != '':
		numbers.append([apt, "apt #"])
	passwords = create_list_of_passwords(words)
	passwords.append(numbers)
	return passwords


if __name__ == "__main__":
	print('Please enter the following details to create your account.')
	email = input('Email address: ')
	firstname = input('First name: ')
	lastname = input('Last name: ')
	birth = input('Date of Birth (Format MM/DD/YYYY): ')
	phone = input('Phone number (Format XXX-XXX-XXXX): ')
	print('Mailing Address')
	address = input('Street Information (Street number and name): ')
	apt = input('Apartment Number (if applicable, else hit \'enter\' key): ')
	city = input('City: ')
	state = input('State: ')
	zipcode = input('Zip Code: ')

	passwords = task2(firstname, lastname, email, phone, birth, address, apt, city, state, zipcode)
	#print(passwords)
	
	for i in range(len(passwords) - 2):
		print(passwords[i][0])
	print("Any password which contains the following numbers:", passwords[len(passwords) - 1], 
	"(will be checked with Python's string.contains() method)")
	


