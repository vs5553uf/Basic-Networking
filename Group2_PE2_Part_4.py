import random
# This is a change to the file
# This is another change to the file


def main():
    exit = False
    difficulty = setdifficulty()
    option = getoperation()
    while not exit and option != 5:
        awser = createquestion(difficulty, option)
        exit = checkanswer(awser)
        option = getoperation()
    print("Thanks for playing")


def createquestion(difficulty, option):
    try:
        # if else statement to generate random numbers based
        # on the variable difficulty
        if difficulty == 1:
            num1 = random.randrange(10)
            num2 = random.randrange(10)
        else:
            num1 = random.randrange(100)
            num2 = random.randrange(100)

        if option == 1:
            print('How much is ', num1, ' + ', num2, '? ', sep='')
            return num1 + num2
        elif option == 2:
            print('How much is ', num1, ' - ', num2, '? ', sep='')
            return num1 - num2
        elif option == 3:
            print('How much is ', num1, ' * ', num2, '? ', sep='')
            return num1 * num2
        elif option == 4:
            print('How much is ', num1, ' / ', num2, '? ', sep='')
            while num2 == 0:
                if difficulty == 1:
                    num2 = random.randrange(10)
                else:
                    num2 = random.randrange(100)
            return num1 // num2
        else:
            print()

    except Exception:
        print("An Error has occurrred!")


def checkanswer(answer):
    try:
        num = int(input('Enter your answer (-1 to exit): '))

        while num != answer and num != -1:
            correct, wrong = getresponse()
            print(wrong)
            num = int(input('Enter your answer (-1 to exit): '))

        if num == answer:
            correct, wrong = getresponse()
            print(correct)
            return False

        if num == -1:
            return True
    except Exception as ex:
        print("Please enter a number!")
        return checkanswer(answer)


def getresponse():
    number = random.randint(1, 4)

    if number == 1:
        correct = "Very Good"
        wrong = "No. Please try again."
    else:
        if number == 2:
            correct = "Nice work!"
            wrong = "Wrong. Try once more."
        else:
            correct = "Keep up the good work!"
            wrong = "No. Keep trying."

    return correct, wrong


def setdifficulty():
    try:
        # stores the user's input in a variable
        difficulty = int(input('Select Difficulty 1 or 2: '))

        # input validation to make sure the user enters either 1 or 2
        while difficulty != 1 and difficulty != 2:
            print('Enter 1 or 2')
            difficulty = int(input('Select Difficulty 1 or 2: '))

        # returns the random numbers to be used in the game
        return difficulty

    # error handling
    except ValueError:
        print('Enter 1 or 2')
        return setdifficulty()
    except Exception:
        print('Enter 1 or 2')
        return setdifficulty()


# function to display the game menu
def getoperation():
    try:
        # displays the menu
        print('1. Addition')
        print('2. Subtraction')
        print('3. Multiplication')
        print('4. Division')
        print("5. Exit")
        option = int(input('Enter Option: '))
        print()

        # tests user input to make sure the user enters
        # a valid menu option
        while option < 1 or option > 5:
            print('Enter a valid menu option\n')

            # displays the menu
            print('1. Addition')
            print('2. Subtraction')
            print('3. Multiplication')
            print('4. Division')
            print("5. Exit")
            option = int(input('Enter Option: '))
            print()
        else:
            # returns the selected option
            return option

    # error handling
    except ValueError:
        print('\nEnter a valid menu option\n')
        return getoperation()
    except Exception:
        print('\nEnter a valid menu option\n')
        return getoperation()


main()
