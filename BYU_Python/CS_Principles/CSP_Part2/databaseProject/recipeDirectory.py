from database import Simpledb

command = ''
while command != 'q':
    print('Would you like to insert, delete, modify, or quit?')
    command = input('(i, d, m, q) --> ')

    db = Simpledb('recipes.txt')

    # INSERT COMMAND
    if command == 'i':
        key = input('Key:    ')
        value = input('Value:    ')
        db.insert(key, value)

    # DELETE COMMAND
    elif command == 'd':
        key = input('Key:    ')
        findKey = db.select_one(key)
        if findKey == None:
            print('Key not found in database\n')
        else:
            db.delete(key)

    # UPDATE COMMAND
    elif command == 'm':
        key = input('key:    ')
        findKey = db.select_one(key)
        if findKey == None:
            print('Key not found in database\n')
        else:
            NewValue = input('New Value:    ')
            db.modify(key, NewValue)

