import getpass


class Main:

    def __init__(self,
                 number=None,
                 array=None,
                 first_number=None,
                 second_number=None,
                 operand=None,
                 word=None,
                 parameter=None,
                 my_input=None,
                 input_str=None):

        self.number = number
        self.array = array
        self.first_number = first_number
        self.second_number = second_number
        self.operand = operand
        self.word = word
        self.parameter = parameter
        self.my_input = my_input
        self.input_str = input_str

    def fibonacci(self, number: int):
        """This function will calculate the fibonacci of the\r
        entry parameter"""
        self.number = number
        b = 0
        result = ''
        c = 1
        final_result = None

        for _ in range(1, self.number + 1):

            while b < self.number:

                result += str(b) + ","

                b = b + c

                if c <= self.number:
                    result += str(c) + ','

                    c = b + c

        if result.endswith(','):
            final_result = result[0:len(result) - 1]

        return final_result

    def my_factorial(self, number: int):
        """this function will return the factorial of the entry parameter\r
        and have a default parameter in case that it doesnt get any parameter."""

        self.number = number
        storage = 1
        counter = 1

        f = open('My_factorial.txt', 'w')
        f.write('')
        f.close()

        if self.number:
            while counter <= self.number:
                storage *= counter
                counter += 1
            return f'the factorial of {self.number} is {storage}'
        else:
            self.number = [2, 3, 5, 8, 9]
            for i in self.number:

                while counter <= i:
                    storage *= counter
                    counter += 1

                f = open('My_factorial.txt', 'a')
                f.write('the factorial of: ' + str(i) + ' ' + 'is' + ' ' + str(storage) + '\n')
                f.close()

            return open('My_factorial.txt').read()

    def decorator(self, a, b):

        def my_decorator(func):
            def inner_func(a, b):
                if a == 0 or b == 0:
                    raise ValueError
                return func(a, b)

            return inner_func

        @my_decorator
        def double(a, b):
            return "the result of divide is %6.2f" % (a / b)

        return double(a, b)

    def max_min(self, array):
        self.array = array
        if not self.array:
            self.array = [20, 50, 2]

        min_number = self.array[0]
        max_number = self.array[0]

        for FirstVal in self.array:

            if float(max_number) < float(FirstVal):

                max_number = FirstVal

            elif float(min_number) > float(FirstVal):

                min_number = FirstVal

        return f'the Greatest number is: {max_number} and the Least Number is: {min_number}'

    def vowel_sound(self, word):
        """this function will count the number of vowel sound that it
        takes."""

        self.word = word
        a = 0
        e = 0
        i = 0
        o = 0
        u = 0

        for first_for in self.word:

            if first_for in 'aA':
                a += 1
            elif first_for in 'eE':
                e += 1
            elif first_for in 'iI':
                i += 1
            elif first_for in 'oO':
                o += 1
            elif first_for in 'uU':
                u += 1

        return f'\ra: {a}\ne: {e}\ni: {i}\no: {o}\nu: {u}'

    def simple_calculator(self, first_number: float, second_number: float, operand: str):

        self.first_number = first_number
        self.second_number = second_number
        self.operand = operand
        if self.operand == '+':
            my_sum = self.first_number + self.second_number
            return f'the Division of two numbers is: {my_sum}'

        elif self.operand == '*':
            multi = self.first_number * self.second_number
            return f'the Division of two numbers is: {multi}'

        elif self.operand == '-':
            sub = self.first_number - self.second_number
            return f'the Division of two numbers is: {sub}'

        elif self.operand == '/':

            div = self.first_number / self.second_number
            return f'the Division of two numbers is: {div}'

        elif self.operand == '**':

            power = self.first_number ** self.second_number
            return f'the Division of two numbers is: {power}'

    def ord_asci(self, parameter):
        """ This Function will return the ascci code of characters and
    character of numbers that has given to it.
    ________________________

    For call the function you need to enter a single string that can contain numbers and character.
    for example: main("57 67 39 67 213 Roberick")"""

        self.parameter = parameter
        number = ''
        character = ''
        sepi = my_separator(self.parameter)

        def my_ord(i3):

            nonlocal number
            number += chr(int(i3)) + ' '
            return number

        def my_char(i2):

            nonlocal character
            for ss in i2:
                character += str(ord(ss)) + ' '
            return character

        for i in sepi:

            try:

                if int(i):
                    my_ord(i)

            except:
                my_char(i)

        if number.endswith(" "):
            number = number[:(len(number) - 1)]

        if character.endswith(" "):
            character = character[:(len(character) - 1)]

        return f'"({self.parameter})" converted to: \nnumbers are:"{number}". \ncharacters are:"{character}".'

    def lower_upper(self, input_str):
        """This Function will return the vice versa of the entered sentence"""
        try:

            self.input_str = input_str
            result = ''
            # todo :-32
            my_dict = {
                65: 97, 66: 98,
                67: 99, 68: 100,
                69: 101, 70: 102,
                71: 103, 72: 104,
                73: 105, 74: 106,
                75: 107, 76: 108,
                77: 109, 78: 110,
                79: 111, 80: 112,
                81: 113, 82: 114,
                83: 115, 84: 116,
                85: 117, 86: 118,
                87: 119, 88: 120,
                89: 121, 90: 122,
            }
            for i in self.input_str:

                if 65 <= ord(i) <= 90:
                    result += chr(my_dict[ord(i)])

                elif 97 <= ord(i) <= 122:

                    for key, value in my_dict.items():

                        if value == ord(i):
                            result += chr(key)

                else:
                    result += i
        except TypeError or ValueError:

            return f'''You entered wrong value.
            \rEnter a sentence like:
            \r"RobeRIcK" '''

        except:
            return f'what the hell did you entered??!? :))'

        else:
            return result

    def counting_str(self, my_input):
        """This function will return the index and
    the Repeated time of Roberick in the entered sentence """

        self.my_input = my_input
        counter_test = 0
        sentence = ''
        counter_of_word = 0

        try:
            # checking the length of the Input...
            if len(self.my_input) < 10:
                self.my_input = 'python language tutorials by Roberick'
                print(f'''you entered a sentence less than 10 character.
                \rthe default sentence is:
                \r"python language tutorials by Roberick"''')

            # I used my own module to separate the sentence to a list
            cup_1 = my_separator(self.my_input)

            # this loop is just to count the repeated time
            # of Roberick in the sentence
            for i in cup_1:
                if 'roberick' in i.lower():
                    counter_of_word += 1

            # this loop here is to find out the index of the first
            # Roberick in the sentence
            for i2 in self.my_input:
                sentence += i2
                counter_test += 1

                # to find the roberick and its index
                if 'roberick' in sentence.lower():
                    counter_test = counter_test - 8
                    break

                # this condition is for clear the
                # sentence variable
                if i2 == ' ':
                    sentence = ''
                    continue

        except:
            return f'something wrong happens pls try again.'

        return f'''Repeated time of Roberick: {counter_of_word}
        \rthe index of first Roberick in this sentence: {counter_test}'''

    @property
    def register(self):
        """
        This function will do the registry stuff.
        check if the username exist or not.
        add the username to the database.
        encrypt the password and check if the password enter correct or not.
        """

        while True:

            try:

                # Opening the file
                my_data = open("my_data_base.txt")
                my_data_2 = open("my_data_base.txt", 'a')

                # Get username
                set_username = input("Enter a user name for your account: ")

                # In case the username is back or end
                if set_username.lower() == 'back' or set_username.lower() == "end":
                    exit_question = input("Do you want to take a step back?(y/n): ")

                    if exit_question == "y" or exit_question == "yes" or exit_question == "yep":
                        return False
                    else:
                        print("This username that u entered has been reserved. please try something else")
                        continue

                # Check if the username is exist in database
                for i in my_data.readlines():
                    username_checker = my_separator(i)
                    if username_checker == [] or set_username == username_checker[0]:
                        if not username_checker:
                            continue
                        else:
                            raise ValueError

                # Add the username to the data base
                else:

                    my_data_2.write('\n' + set_username + ' ' + ":" + " ")

                    # specific loop for getting password
                    while True:
                        print("the password wont show up when you typing...")
                        set_password = getpass.getpass(prompt="Enter a password for your account: ")
                        # set_password = input("Enter a password for your account: ")
                        # Check that the entry password is empty or less than 4 char...
                        if len(set_password) < 4 or len(set_password) > 16:
                            print('Your password should has more than 3 and less than 16 character')
                            continue

                        # make sure that the user typed the desire password correct
                        elif set_password:

                            confirm_password = getpass.getpass(prompt="Enter your password again to confirm it: ")

                            # End the loop
                            if set_password == confirm_password:

                                # Put the encrypted password for the entry user in database
                                my_password = str(encoder(set_password))
                                my_data_2.write(my_password)

                                # Close the file
                                my_data.close()
                                my_data_2.close()

                                return True
                            else:
                                print("the password doesn't match.")
                                continue

                # Put the encrypted password for the entry user in database

                # my_password = str(encoder(set_password))
                # my_data_2.write(my_password)

                # Close the file
                my_data.close()
                my_data_2.close()

            # In case that the username was exist
            except ValueError:
                print('the username that you entered has exist. Try another username...')
                continue

            except IndexError:
                print('Something wrong happened!.')
                pass

            else:
                break

    def log_in(self):
        """This function is check the entry username in my own created database
        and encrypted the password that entered and compared it with the one that
        set for the entered username in the database."""

        # set needed value
        import time
        counter = 0
        flag = False
        password_checker = None

        # Main loop
        while True:

            try:

                # set flag in case the user is correct
                # and stop repeating for getting username
                # when the password entered wrong or ...
                if not flag:

                    # Take the username
                    my_data_base = open("my_data_base.txt")
                    take_username = input("Enter your user name please: ")

                    # Check if the value is not empty
                    if take_username:

                        if take_username.lower() == "back" or take_username.lower() == "end":
                            exit_checker = input("Do you want to take a step back?(y/n): ")
                            if exit_checker == "y" or exit_checker == "yes" or exit_checker == "yep":
                                return False
                            else:
                                print("This username has been reserved. please try something else")
                                continue

                        # Search for the entered username in database
                        for i in my_data_base.readlines():

                            # Make a list of user and password for each line
                            username_checker = my_separator(i)

                            # Check if the entered username
                            # is exist in each line of database
                            if take_username == username_checker[0]:
                                # Change the flag to true to prevent from the repetition
                                # Make an instance of encrypted password that belongs
                                # to the entered username...
                                flag = True
                                password_checker = username_checker[1]
                                break

                        if not flag:
                            # In case that the entered username has not existence
                            print("The username is not exist.Try again or sign up.")
                            continue

                # Take the password
                # Encrypt the entered password
                # Make a counter for avoiding the Bruteforce attack...
                take_password = getpass.getpass(prompt="Enter your password please: ")
                encode_password = encoder(take_password)
                counter += 1

                # Check if the entered password is correct
                if str(encode_password) == password_checker:

                    counter = 0
                    print("\n" + f"Welcome dear {take_username}")
                    return True
                    # time.sleep(3)

                # Preventing from BruteForce attack.
                # Can add some feature or change the waiting time.
                elif counter == 3:
                    print(f"You tried {counter} time to enter."
                          "You have to wait 10 sec and then try again.")
                    time.sleep(10)
                    counter = 0
                    continue

                # For letting the user try entering password
                # if it was wrong...
                else:
                    my_data_base.close()
                    continue

            # Just to make sure that it handle but didnt get any ValueError yet
            except ValueError:
                print("ValueError")

            except IndexError:
                with open("my_data_base.txt") as f:
                    index = 0
                    my_list = f.readlines()
                    # len_l = len(my_list)
                    for line in my_list:
                        if take_username in line:
                            del my_list[index]
                        index += 1
                    f.close()
                with open("my_data_base.txt", "w") as f:
                    f.writelines(my_list)
                    f.close()
                flag = False
                continue


def my_separator(character: str) -> list:
    """This function will make a list of
    its entry parameter and separate each word or numerical number
    to a member of the list
    the criterion of the separator is:
    ["space", ":", "-", "_", ",", "\n", "\r", ]"""

    l1 = []
    ss = ''
    counter = 0

    for i in character:

        if i == ' ' or i == ',' or i == '-' or i == '_' or i == ':' or i == '\n' or i == '\r':

            l1.append(ss)
            ss = ''
            counter += 1

        elif counter == len(character) - 1:

            ss += i
            l1.append(ss)
            ss = ''

        else:
            ss += i
            counter += 1

        if '' in l1:
            for i2 in l1:
                if i2 == '':
                    l1.remove(i2)

    return l1


def first_reverse(str_param):
    """this func will make the entered parameter, revers"""

    result = ''
    length = len(str_param)

    for i in range(length - 1, -1, -1):
        result += str_param[i]

    return result


def encoder(password: str = None):
    """This function will encrypt
    the parameter that it takes"""

    out_put = None
    formula_number = 0

    # Check if the parameter is not None
    if password:

        # Make a reverse of the entry parameter
        reverse_input = first_reverse(password)

        # Convert the each character
        # to the ascii code of it
        # and sum each code to the previous one
        # to have a number of sum all the ascii code...
        for i in reverse_input:
            formula_number += ord(i)

        # Here is my formula for encryption
        # that write it into a function
        def encrypt(input_parameter) -> int:

            en_bowl = ((input_parameter * 7) // 2) - 1

            return en_bowl

        # Call the function
        out_put = encrypt(formula_number)

        # return the encrypted password
        return out_put
