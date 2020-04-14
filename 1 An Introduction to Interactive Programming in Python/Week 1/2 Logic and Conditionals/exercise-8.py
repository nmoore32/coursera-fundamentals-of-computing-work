def name_lookup(first_name):
    '''Returns a last name depending on name entered'''
    if first_name == 'Joe':
        return 'Warren'
    elif first_name == 'Scott':
        return 'Rixner'
    elif first_name == 'John':
        return 'Greiner'
    elif first_name == 'Stephen':
        return 'Wong'
    else:
        return 'Error: Not an instructor'


print(name_lookup('Joe'))
print(name_lookup('Scott'))
print(name_lookup('John'))
print(name_lookup('Stephen'))
print(name_lookup('Nathan'))
