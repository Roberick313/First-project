from The_class import Main, my_separator
import time

# make an instance of the
# Main class that contain
# all of the functions
my_class = Main()


class NotValid(Exception):
    pass


starter = f"""
   \r1.fibonacci
   \r2.factorial
   \r3.decorator
   \r4.max_min
   \r5.Prime
   \r6.Vowel sounds
   \r7.Calculator
   \r8.ord_ascii
   \r9.Lower_Upper
   \r10.Roberick
   """


def main():
    """This func will run the program
    to show the exercises and take an input for
    each choice to return the result of that exercise."""

    # my values...
    require = None
    counter = 0
    flag = False
    first_require = None
    second_require = None
    account_checker = False

    # make a welcome/info command for program
    time.sleep(0.5)
    welcome = f"""Hi there.
    \rWelcome to my program.
    \rThis program contain some exercises
    \rthat you can use them to see the result.
    \rFirst of all you need an account.
    \rif You created one before so you just need to log_in to your account.
    """
    print(welcome)
    time.sleep(1.5)
    info_command = F"""\nType one of the below word in any input to make it.
    \r1.end : is for to shutdown the program (CTRL+C) will do the same
    \r2.back : is to step back...
    """
    print("just type help/info in case you need it.\n")

    # Loop for sign up and log_in
    while True:

        try:

            # Question about having account
            require = input("Do you have account?(y/n): ")

            # If does have account
            if require.lower() == "y" or require.lower() == "yes" or require.lower() == "yep":
                account_checker = my_class.log_in()

            # If doesn't have account
            elif require.lower() == "n" or require.lower() == "no" or require.lower() == "nope":
                register_checker = my_class.register
                if register_checker:
                    print("Now you just need to log in to your account!")
                    time.sleep(0.5)
                    account_checker = my_class.log_in()
                else:
                    continue

            # In case user wants to shutdown the program
            elif require.lower() == 'end':
                raise KeyboardInterrupt

            # In case user wants help
            elif require.lower() == 'info' or require.lower() == 'help':
                print(info_command)
                time.sleep(0.5)
                continue

            # In case that the user entered the wrong input
            else:
                message = f"""You entered a wrong value.
                \ryou can user these keywords.
                \r'yes', 'no', 'end'
                """
                print(message)
                continue

            # Check if the user successfully logged in
            if account_checker:

                account_checker = False

                # The main loop to show the menu...
                while True:

                    try:

                        # show the exercise
                        print(starter)
                        command = input("Pls enter one of the above exercises: ")
                        if command.lower() == 'end':
                            raise KeyboardInterrupt

                        elif command.lower() == 'back':
                            break

                    # all the conditions to check which program
                    # has been chosen...

                        # Fibonacci
                        if command.lower() in ['1', 'fibonacci', 'fib']:

                            # this loop is for make a infinite request for
                            # inputs till the process will success.
                            while True:

                                try:

                                    if not flag:
                                        # Inform
                                        message = f"""\nThis program will calculate 
                                        \rthe fibonacci of the entry number"""
                                        print(message)
                                        flag = True

                                    # take input
                                    require = input('please enter a number: ')

                                    # In case that the user wants to shutdown the program
                                    if require.lower() == 'end':
                                        raise KeyboardInterrupt

                                    # In case that the user wants to step back to the main menu
                                    elif require.lower() == "back":
                                        break

                                    # In case that the user wants help
                                    elif require.lower() == "help" or require.lower() == "info":
                                        print(info_command)
                                        time.sleep(0.5)
                                        continue

                                    # Check is the input number
                                    elif type(int(require)) is int:

                                        # print out the result
                                        print('\n', my_class.fibonacci(int(require)))
                                        time.sleep(1)

                                    else:
                                        raise ValueError

                                except ValueError:

                                    print('\n'+"""the value that u just entered was incorrect
                                    \rplease enter a number value.. :)"""+'\n')
                                    continue

                                else:
                                    flag = False
                                    break

                        # Factorial
                        elif command.lower() in ['2', 'factorial', 'fac']:

                            while True:

                                try:

                                    if not flag:
                                        # Inform
                                        message = f"""\nThis program will calculate the Factorial of
                                        \rthe entry number that it takes."""
                                        print(message)
                                        flag = True

                                    # Getting input
                                    require = input('pls enter a number: ')

                                    # In case that the user wants to shutdown the program
                                    if require.lower() == 'end':
                                        raise KeyboardInterrupt

                                    # In case that the user wants to step back to the main menu
                                    elif require.lower() == "back":
                                        break

                                    # In case that the user wants help
                                    elif require.lower() == "help" or require.lower() == "info":
                                        print(info_command)
                                        time.sleep(0.5)
                                        continue

                                    # here is the own condition ...
                                    elif int(require) == 5:
                                        raise ValueError

                                    # Check the input that is number
                                    elif int(require):
                                        # print out the result
                                        print('\n', my_class.my_factorial(int(require)))
                                        time.sleep(1)

                                    else:
                                        raise ValueError

                                except ValueError:

                                    # Refer to the own condition
                                    if require == '5':
                                        my_message = f"""
                                        \rthere is an exception for number 5!
                                        \rhere is the factorial of number 6!"""
                                        print(my_message, '\n', my_class.my_factorial(6))
                                        break

                                    # default
                                    else:
                                        print('\n'+"""the value that u just entered was incorrect
                                        \rplease enter a number value.. :)"""+'\n')
                                        continue

                                else:
                                    flag = False
                                    break

                        # Decorator
                        elif command.lower() in ['3', 'decorator', 'dec']:

                            while True:

                                try:

                                    if not flag:
                                        # Inform
                                        message = f"""\nThis program will divide the two number
                                        \rthat it takes and return the result."""
                                        print(message)
                                        flag = True
                                        time.sleep(1)

                                    # Getting first input
                                    first_require = input('please enter the first number: ')

                                    # In case that the user wants to shutdown the program
                                    if first_require.lower() == 'end':
                                        raise KeyboardInterrupt

                                    # In case that the user wants help
                                    elif first_require.lower() == "help" or first_require.lower() == "info":
                                        print(info_command)
                                        time.sleep(0.5)
                                        continue

                                    # In case that the user wants to step back to the main menu
                                    elif first_require.lower() == "back":
                                        break

                                    # to check the being integer of input value
                                    if type(float(first_require)) is float:
                                        pass

                                    # Getting second input
                                    second_require = input('please enter the second number: ')

                                    # Check if the user wants to shut down the program
                                    if second_require.lower() == 'end':
                                        raise KeyboardInterrupt

                                    # to check the being integer of input value
                                    if type(float(second_require)) is float:
                                        pass

                                    # Check the numerical of both input
                                    if type(float(first_require)) is float or type(float(second_require)) is float:
                                        print('\n', my_class.decorator(float(first_require), float(second_require)))
                                        time.sleep(1)

                                    else:
                                        raise ValueError

                                except ValueError:

                                    # In case that one of the number is 0
                                    if first_require == "0" or second_require == "0":
                                        print('one of the entry value is zero (0).pls enter numbers bigger than 0')
                                        time.sleep(0.5)

                                    # Default
                                    else:

                                        print('\n'+"""the value that you just entered was incorrect
                                        \rplease enter a number value.. :)"""+'\n')
                                        time.sleep(0.5)
                                        continue

                                else:
                                    flag = False
                                    break

                        # Max and Min
                        elif command.lower() in ['4', 'min and maximum', 'min', 'max', 'min_max', 'max_min']:

                            while True:

                                try:

                                    # Check that if the program didnt have a start
                                    if not flag:
                                        # Inform
                                        message = f"""\nThis program will find out the minimum and maximum
                                        \rof the entry numbers."""
                                        print(message)

                                        # Getting input
                                        require = str(input('please enter more than two numbers: '))

                                        # Check if the user wants to shut down the program
                                        if require.lower() == 'end':
                                            raise KeyboardInterrupt

                                        # In case that the user wants to step back to the main menu
                                        elif require.lower() == "back":
                                            break

                                        # In case that the user wants help
                                        elif require.lower() == "help" or require.lower() == "info":
                                            print(info_command)
                                            time.sleep(0.5)
                                            continue

                                    # Check the type and make a list of the input
                                    if type(require) == str:
                                        my_list = my_separator(require)

                                        # Make sure about the entry value is number
                                        for i in my_list:
                                            if i:
                                                float(i)

                                        # This loop is for checking and continue the
                                        # loop in case the numbers between 10 - 100
                                        # to print out the custom error
                                        # Each time it finds a number between 10 - 100
                                        for i2 in my_list[counter:]:
                                            counter += 1
                                            if 10 <= float(i2) <= 100:
                                                flag = True
                                                raise NotValid

                                        # The calling function and print out the result
                                        print('\n', my_class.max_min(my_list))
                                        time.sleep(1)

                                        # Reset the values
                                        flag = False
                                        counter = 0

                                    else:
                                        raise ValueError

                                except ValueError:

                                    message = f"""
                                    \rThe entry value is not acceptable
                                    \rmay one of the value is not number.
                                    \rhere is an example of how to put value for this exercise:
                                    \r4,7,3,96,345,8,456,3 or
                                    \r4 765 23 543 2 45 2.4 
                                    \ryou can separate the numbers with ('one single space', ',' , '-','_')"""
                                    print(message)

                                # Custom Error
                                except NotValid:
                                    print(f'{counter}. i found a number between 10 - 100!')
                                    continue

                                else:
                                    break

                        # Prime Number
                        elif command.lower() in ['5', 'prime', 'prm', 'pri']:
                            while True:

                                try:

                                    if not flag:
                                        # Inform
                                        message = f"""\nThis program will find out that
                                        \rthe entry number is prime or not."""
                                        print(message)
                                        flag = True

                                    # Getting input
                                    require = input('Enter a number please: ')

                                    # Check if the user wants to shut down the program
                                    if require.lower() == 'end':
                                        raise KeyboardInterrupt

                                    # In case that the user wants help
                                    elif require.lower() == "help" or require.lower() == "info":
                                        print(info_command)
                                        time.sleep(0.5)
                                        continue

                                    # Check if the user wants to step back to the main menu
                                    elif require.lower() == "back":
                                        break

                                    # Check if the number is below or equal 1
                                    if int(require) <= 1:
                                        print('the number that just entered is 1 or below 1...')
                                        continue

                                    # if the entry value bigger than 1
                                    elif int(require) > 1:
                                        # This loop is for if the value is not prime
                                        for i in range(2, int(require)):
                                            if (int(require) % i) == 0:
                                                print("the number isn't prime")
                                                break

                                        # Calling function
                                        else:
                                            print('\n'+f"{require} is a prime number.")
                                            time.sleep(1)
                                            flag = False
                                            break

                                        # To make the infinite request until
                                        # The prime number has been find
                                        continue

                                except ValueError:
                                    message = f"""
                                    \rThe value that you entered is not 'Number' or below number 1
                                    \rPlease enter a number bigger than 1..."""
                                    print(message)
                                    continue

                                else:
                                    flag = False
                                    break

                        # Vowel sounds
                        elif command.lower() in ['6', 'vowel', 'vow', 'sound', 'vol', 'wol']:
                            while True:

                                try:

                                    if not flag:
                                        # Inform
                                        message = f"""\nThis program will show the number of
                                        \rvowel sounds that are in the entry sentence."""
                                        print(message)
                                        flag = True
                                        time.sleep(1.5)

                                    # Getting input
                                    require = input("Enter a sentence please: ")

                                    # Check if the user wants to shut down the program
                                    if require.lower() == 'end':
                                        raise KeyboardInterrupt

                                    # In case that the user wants help
                                    elif require.lower() == "help" or require.lower() == "info":
                                        print(info_command)
                                        time.sleep(0.5)
                                        continue

                                    # Check if the user wants to step back to the main menu
                                    elif require.lower() == "back":
                                        break

                                    # Calling function
                                    else:
                                        print('\n', my_class.vowel_sound(require))
                                        time.sleep(1)

                                except ValueError:
                                    message = f"""
                                    \rThere is something wrong
                                    """
                                    print(message)
                                    continue
                                else:
                                    flag = False
                                    break

                        # Calculator
                        elif command.lower() in ['7', 'calculator', 'cal']:
                            while True:

                                try:

                                    # take first number.
                                    first_number = input("Enter the first number: ")

                                    # In case user wants to shut down the program
                                    if first_number.lower() == 'end':
                                        raise KeyboardInterrupt

                                    # In case that the user wants help
                                    elif first_number.lower() == "help" or first_number.lower() == "info":
                                        print(info_command)
                                        time.sleep(0.5)
                                        continue

                                    # In case user want to exit from the current program
                                    elif first_number.lower() == 'done' or first_number.lower() == 'back':
                                        break
                                    else:
                                        if float(first_number):
                                            pass

                                    # take operand.
                                    operand = input("Enter the operand: ")

                                    # In case user wants to shut down the program
                                    if operand.lower() == 'end':
                                        raise KeyboardInterrupt

                                    # In case that the user wants help
                                    elif operand.lower() == "help" or operand.lower() == "info":
                                        print(info_command)
                                        time.sleep(0.5)
                                        continue

                                    # In case user want to exit from the current program
                                    elif operand.lower() == 'done' or operand.lower() == 'back':
                                        break

                                    # Check if the entry value for operand is not Operands!.
                                    elif not (operand in ['-', '+', '*', '**', '/']):
                                        raise ValueError

                                    # take second number.
                                    second_number = input("Enter the second number: ")

                                    # In case user wants to shut down the program
                                    if second_number.lower() == 'end':
                                        raise KeyboardInterrupt

                                    # In case that the user wants help
                                    elif second_number.lower() == "help" or second_number.lower() == "info":
                                        print(info_command)
                                        time.sleep(0.5)
                                        continue

                                    # In case user want to exit from the current program
                                    elif second_number.lower() == 'done' or second_number.lower() == "back":
                                        break
                                    else:
                                        if float(second_number):
                                            pass

                                    # Calling function
                                    print('\n', my_class.simple_calculator(float(first_number),
                                                                           float(second_number), operand))
                                    time.sleep(1)

                                except ValueError:
                                    message = f"""
                                    \rOne of the entry value that you entered is not number ...
                                    \rPlease enter a number...
                                    \rIn case you want to quite the calculator
                                    \rWrite 'Done' to exit from the calculator
                                    """
                                    print(message)
                                    continue

                                else:
                                    # Inform about how to exit from the calculator
                                    message = f"""
                                    \rIn case you want to quite the calculator
                                    \rwrite 'Done' in the input place ...
                                    """
                                    print(message)

                        # Ord_Ascii
                        elif command.lower() in ['8', 'ord_ascii', 'ord', 'ascii', 'ascii_ord', 'asci']:
                            while True:

                                try:

                                    if not flag:
                                        # Inform
                                        message = f"""\nthis program convert the characters to
                                         \rtheir ascii codes and convert numbers to character.
                                         \ryou can put numbers(only integer) in range 0 - 1,1141,111
                                         \rand for character it will return the ascii code
                                         \rfor each single character(alphabet of any language)
                                         \r!!!!!!!!!!!!!!!!
                                         \r'YOU HAVE TO SEPARATE NUMBERS AND CHARACTER WITH
                                         \rAT LEAST ONE SINGLE SPACE OR ANY OTHER SEPARATOR
                                         \rLIKE ('-','_',',',':')'.
                                         \r!!!!!!!!!!!!!!!!"""
                                        print(message)
                                        flag = True
                                        time.sleep(1)

                                    # Getting input
                                    require = input("Enter your word please: ")

                                    # Check if the user wants to shut down the program
                                    if require.lower() == 'end':
                                        raise KeyboardInterrupt

                                    # In case that the user wants help
                                    elif require.lower() == "help" or require.lower() == "info":
                                        print(info_command)
                                        time.sleep(0.5)
                                        continue

                                    # Check if the user wants to step back to the main menu
                                    elif require.lower() == "back":
                                        flag = False
                                        break

                                    # Calling function
                                    else:
                                        print('\n'+my_class.ord_asci(require))

                                except ValueError:
                                    message = f"""
                                    \rWrong value just entered
                                    \rPlease try again..."""
                                    print(message)
                                    continue

                                else:
                                    flag = False
                                    break

                        # Upper_lower
                        elif command.lower() in ['9', 'lower_upper', 'lower', 'upper', 'low', 'up', 'upper_lower']:
                            while True:

                                try:

                                    if not flag:
                                        # Inform
                                        message = f"""\nThis program will change the lower case
                                         \ralphabet to upper and vise versa."""
                                        print(message)
                                        flag = True

                                    # getting input
                                    require = input('Enter a sentence or word please: ')

                                    # Check if the user wants to shut down the program
                                    if require.lower() == 'end':
                                        raise KeyboardInterrupt

                                    # In case that the user wants help
                                    elif require.lower() == "help" or require.lower() == "info":
                                        print(info_command)
                                        time.sleep(0.5)
                                        continue

                                    # Check if the user wants to step back to the main menu
                                    elif require.lower() == "back":
                                        break

                                    # Check the entry value doesn't contain numbers
                                    for i in require:
                                        if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                                            raise ValueError

                                    # Calling function
                                    else:
                                        print('\n'+my_class.lower_upper(require))
                                        time.sleep(0.6)

                                except ValueError:
                                    message = f"""The value that you just entered contains numbers. 
                                    \rThe value that you should enter
                                    \rhas to have just alphabets not numbers..."""
                                    print(message)
                                    time.sleep(0.6)
                                    continue

                                else:
                                    flag = False
                                    break

                        # founding Roberick in sentence
                        elif command.lower() in ['10', 'roberick', 'rob', 'rick']:

                            while True:

                                try:

                                    if not flag:

                                        # Inform
                                        message = f"""\nThis program will find and counting
                                        \rthe number of repeated time of word 'roberick'
                                        \rin the input sentence"""
                                        print(message)
                                        flag = True

                                    # Getting input
                                    require = input('Enter a sentence please: ')

                                    # check if the user wants to shut down the program
                                    if require.lower() == 'end':
                                        raise KeyboardInterrupt

                                    # In case that the user wants help
                                    elif require.lower() == "help" or require.lower() == "info":
                                        print(info_command)
                                        time.sleep(0.5)
                                        continue

                                    # Check if the user wants to step back to the main menu
                                    elif require.lower() == "back":
                                        break

                                    # main process of this program.
                                    else:
                                        print('\n'+my_class.counting_str(require))
                                        time.sleep(1)

                                except ValueError:
                                    message = f"""The value that you entered is not valid.
                                    \rplease try again."""
                                    print(message)
                                    continue

                                else:
                                    flag = False
                                    break

                        # In case that use entered
                        # wrong name of program in the input
                        else:
                            raise ValueError

                    except ValueError:

                        err = f'''The entered value is not supported by the program
                        \rplease enter the number of selected exercise or
                        \rthe full name or the first 3 character of the exercise name
                        \rfor example: "1" or "fibonacci" or "fib"'''
                        print(err)
                        time.sleep(2)

        # This exception is for shortcut (CTRL+c) and 'END' input
        except KeyboardInterrupt:

            counter = 0
            print('\n')

            while counter <= 3:
                counter += 1
                print(counter)

                if counter == 3:
                    print('Bbye! :)')
                    time.sleep(0.4)
                    exit()

                time.sleep(1)

        else:
            continue


if __name__ == '__main__':
    main()
