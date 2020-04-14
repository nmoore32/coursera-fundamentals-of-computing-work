def set_goodbye():
    '''Updates global variable 'message' with value 'Goodbye' and prints it'''
    global message
    message = 'Goodbye'
    print(message)


message = "Hello"
print(message)
set_goodbye()
print(message)

message = "Ciao"
print(message)
set_goodbye()
print(message)
