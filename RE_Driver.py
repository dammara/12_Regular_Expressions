# Markhus Dammar
# 23 March 2020
# This program takes a user inputted string and uses RegEx to perform matches within the string

import time, re


def invalid():                                          # Screen for Invalid input
    print("INVALID CHOICE, TRY AGAIN")
    time.sleep(1.5)


def welcome():              # Splash Screen
    print("""\033[1m
    ---------RegEx String Check Version 1.0.2--------- \033[0m
    Welcome. This program will check for matches
                  within a given string.""")
    time.sleep(2)
    usertype()


def usertype():             # Takes User input for string
    string = str(input("""Type out a string of your choosing.
                  >>>"""))
    time.sleep(1)
    choose(string)


def choose(string):                   # This is where the user chooses a method
    print(f"""\n
    Please choose a check method. 
    \033[1m ----ENTER the NUMBER (1, 2, 3...).---- \033[0m
    1.See if the string has a 'q'
    2.See if the string contains 'the'
    3.See if the string has a '*' in it
    4.See if the string contains a digit
    5.See if the string contains a period
    6.See if the string has at least 2 consecutive vowels (a,e,i,o,u) like in the word "bear"
    7.See if the string contains white space
    8.See if the string has any letters that repeat three times in a single word
    9.See if the string starts with the word ‘Hello’ (must match the capital H)
    10.See if the string contains an email address 
    \033[1mYour String is: \033[0m""" + string)

    method = int(input(">>>"))          # Method is inputted here

    while method > 10 or method < 1:
        invalid()
        choose(string)

    if method == 1:                                 # Checks for a 'q'
        qcheck = bool(re.search('q', string))
        if qcheck == True:
            print("This string has a q in it")
        elif qcheck == False:
            print("This string doesn't have a q in it")
        next(string)
    elif method == 2:                               # Checks for 'the'
        thecheck = bool(re.search('the', string))
        if thecheck == True:
            print("This string has the word 'the' in it")
        elif thecheck == False:
            print("This string doesn't have the word 'the' in it")
        next(string)
    elif method == 3:                               # Checks for '*'
        starcheck = bool(re.search('\*', string))
        if starcheck == True:
            print("This string has a '*' in it")
        elif starcheck == False:
            print("This string doesn't have a '*' in it")
        next(string)
    elif method == 4:                               # Checks for digits
        digitcheck = bool(re.search(r'\d', string))
        if digitcheck == True:
            print("This string has at least one digit in it")
        elif digitcheck == False:
            print("This string has no digits in it")
        next(string)
    elif method == 5:                               # Checks for '.'
        dotcheck = bool(re.search('\.', string))
        if dotcheck == True:
            print("This string has a '.' in it")
        elif dotcheck == False:
            print("This string has no '.' in it")
        next(string)
    elif method == 6:                               # Checks for consecutive vowels
        vcheck = bool(re.search(r'[aeiou]{2,}', string))
        if vcheck == True:
            print("This string has consecutive vowels in it")
        elif vcheck == False:
            print("This string has no consecutive vowels in it")
        next(string)
    elif method == 7:                               # Checks for white space
        wscheck = bool(re.search(r"\s", string))
        if wscheck == True:
            print("This string has white space in it")
        elif wscheck == False:
            print("This string has no white space in it")
        next(string)
    elif method == 8:                               # Checks for letters that repeat 3 times
        threecheck = bool(re.search(r'(.)\1\1', string))
        if threecheck == True:
            print("This string has a word with letters that repeat 3 times")
        elif threecheck == False:
            print("This string has no repeating letters")
        next(string)
    elif method == 9:                               # Checks for "Hello"
        hcheck = bool(re.match('Hello*', string))
        if hcheck == True:
            print("This string starts with 'Hello'")
        elif hcheck == False:
            print("This string doesn't start with 'Hello'")
        next(string)
    elif method == 10:                               # Checks for email addresses
        echeck = bool(re.search(r'\w+@\w+\.\w+', string))
        if echeck == True:
            print("This string has an email in it")
        elif echeck == False:
            print("This string doesn't contain an email")
        next(string)


def next(string):                     # This is the end screen to determine if the user will continue or not
    time.sleep(2)
    print("\nNOW WHAT?")
    choice = int(input("""
    \033[1mTYPE 1, 2, or 3 \033[0m
        1. Re-Check the same string
        2. Check a new string
        3. Exit
        >>>"""))
    if choice == 1:             # Will return to the method choice menu
        choose(string)
    elif choice == 2:           # Will return to the string input
        usertype()
    elif choice == 3:           # Exits the program
        print("\033[1mGoodbye! \033[0m")
        time.sleep(1)
        exit()
    else:                       # Checks if input is 1, 2 or 3. If not, Invalid.
        invalid()
        next()


welcome()
