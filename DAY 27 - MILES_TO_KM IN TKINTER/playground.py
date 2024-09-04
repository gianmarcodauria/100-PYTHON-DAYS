def add(*args):
    print(args[0])

    result = 0
    for n in args:
        result += n
    return result

#print(add(1, 3 , 6, 80))

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items()
        # print(key)
        # print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)


def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)


bar(1, 2)


def all_aboard(a, *args, **kw):
    # reme,ber: a is a argument with a specific value;
    #*args is a tuple: when printed it will print parenthesises as well
    # **kw is a dictionary, when printet it prints brackets as well
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)


