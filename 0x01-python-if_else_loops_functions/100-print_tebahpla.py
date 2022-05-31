#!/usr/bin/python3
for alph in range(122, 96, -1):
    print("{}".format(chr(alph) if alph % 2 == 0 else chr(alph - 32)), end='')
