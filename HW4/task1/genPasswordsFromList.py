from task1utils import *

read_path = './commonPasswords.txt'
write_path = './createdPasswords.txt'

with open(read_path, 'r') as passwordFile:
    write_file = open(write_path, 'w')
    for word in passwordFile:
        # Create a flag so the application can report which word a password matched with
        write_file.write("$ ")
        for created in create_list_of_passwords(word.strip()):
            write_file.write(created[0] + ' ')

