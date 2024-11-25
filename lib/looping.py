#!/usr/bin/env python3
def happy_new_year():
    k = 10
    while k > 0:
        print(k)
        k -= 1
        if k == 0:
            print("Happy New Year!")
    pass
print(happy_new_year())
def square_integers(int_list):
    return [i * i for i in int_list]
pass

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    pass
print(fizzbuzz())