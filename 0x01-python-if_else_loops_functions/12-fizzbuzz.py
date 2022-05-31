#!/usr/bin/python3
def fizzbuzz():
    for value in range(1, 101):
        if value % 3 == 0 and value % 5 == 0:
            print("FizzBuzz ", end='')
            continue
        if value % 3 == 0:
            print("Fizz ", end='')
            continue
        elif value % 5 == 0:
            print("Buzz ", end='')
            continue
        else:
            print("{} ".format(value),  end='')
