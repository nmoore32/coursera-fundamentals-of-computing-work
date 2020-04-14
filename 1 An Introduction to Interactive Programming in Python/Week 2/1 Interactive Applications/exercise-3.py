count = 0


def reset():
    global count
    count = 0


def increment():
    global count
    count += 1


def decrement():
    global count
    count -= 1


def print_count():
    global count
    print(count)


reset()
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()
