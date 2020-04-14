from random import randrange


def powerball():
    print(f"Today's numbers are {randrange(1, 60)}, {randrange(1, 60)}, {randrange(1, 60)}, "
          f"{randrange(1, 60)}, and {randrange(1, 60)}. The Powerball number is {randrange(1, 39)}")


powerball()
