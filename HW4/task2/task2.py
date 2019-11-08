from task2utils import *

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

numbers = [month,day,year,short_year,phone1,phone2,phone3,zipcode]
words = [firstname.lower(),lastname.lower(),city.lower(),state.lower()]
words.extend(email)
temp = []
for item in address:
	item = str(item)
	if item.isdigit():
		numbers.append(item)
	else:
		temp.append(item.lower())
temp = ''.join(temp)
words.append(temp)

if apt != '':
	numbers.append(apt)

passwords = create_list_of_passwords(words,numbers)
for password in passwords:
	print(password[0])


