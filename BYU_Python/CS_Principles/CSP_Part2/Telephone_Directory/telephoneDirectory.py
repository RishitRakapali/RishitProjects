import databaseModule

command = ''
while command != 'q':
    print('Would you like to add, find, delete, update, or quit?')
    command = input('(a, f, d, u, q) --> ')

    # ADD COMMAND
    if command == 'a':
        name = input('Name:    ')
        phoneNumber = input('Phone Number:    ')
        databaseModule.insert('telephoneDatabase.txt', name, phoneNumber)
    # FIND COMMAND
    elif command == 'f':
        name = input('Name:    ')
        findKey = databaseModule.select_one('telephoneDatabase.txt', name)
        if findKey == None:
            print('Name not found in database\n')
        else:
            print(findKey)
    # DELETE COMMAND
    elif command == 'd':
        name = input('Name:    ')
        findKey = databaseModule.select_one('telephoneDatabase.txt', name)
        if findKey == None:
            print('Name not found in database\n')
        else:
            databaseModule.delete('telephoneDatabase.txt', name)
    # UPDATE COMMAND
    elif command == 'u':
        name = input('Name:    ')
        findKey = databaseModule.select_one('telephoneDatabase.txt', name)
        if findKey == None:
            print('Name not found in database\n')
        else:
            phoneNumber = input('New Phone Number:    ')
            databaseModule.update('telephoneDatabase.txt', name, phoneNumber)

