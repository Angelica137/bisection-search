range(100)
x = 0
y = 100


def guess(x, y):
    return int((x + y) / 2)


def userInput(input):
    return input("Is your secret number " + str(ans) + "?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")


ans = guess(x, y)
print("Please think of a number between 0 and 100!")
value = userInput(input)
while value != "c":
    if value == "l":
        x = ans
        ans = guess(x, y)
        value = userInput(input)
    elif value == "h":
        y = ans
        ans = guess(x, y)
        value = userInput(input)
    else:
        print("error, please enter h, l, or c.\n")
        value = userInput(input)
