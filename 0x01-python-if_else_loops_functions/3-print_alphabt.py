#!/usr/bin/python3
for character in range(97, 123):
    if (character != 'q' or character != 'e'):
        print("{:c}".format(character), end='')
