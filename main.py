import random 
# library to select things randomly
# there are also 5 text tiles that are referenced (animals.txt, plants.txt, foods.txt, countries.txt, and objects.txt) 
# opens and reads files and puts data in lists for each category, so each category list is a list of words that are in that category
plant_file = open("plants.txt", "r")
plant_data = plant_file.read()
data_from_plants = plant_data.replace('\n', '').split(",")

animal_file = open("animals.txt", "r")
animal_data = animal_file.read()
data_from_animals = animal_data.replace('\n', '').split(",")

food_file = open("foods.txt", "r")
food_data = food_file.read()
data_from_foods = food_data.replace('\n', '').split(",")

object_file = open("objects.txt", "r")
object_data = object_file.read()
data_from_objects = object_data.replace('\n', '').split(",")

country_file = open("countries.txt", "r")
country_data = country_file.read()
data_from_countries = country_data.replace('\n', '').split(",")

# puts all of the category lists into a dictionary
categories = {
    'plants': data_from_plants,
    'objects': data_from_objects,
    'countries': data_from_countries,
    'animals': data_from_animals,
    'foods': data_from_foods,
}

# gets a word from the category that has been selected
def getWordFromCategory(input):
    if (input!="random"): # if the user chose random, it gets a word from the randomly selected category
        return random.choice(categories[input])
    else: # if the user chose another category, it will get a word from that category
        return random.choice(categories[randomlyChosenCategory])

# function to print heart emojis to display lives left
def printLivesAsHearts(livesLeft):
    heart =" \u2764\uFE0F"
    return livesLeft * str(heart)

# defines a list of the categories
listOfCategories = ['plants', 'animals', 'foods', 'objects', 'countries']

# random category chooses a random category without telling the player which category is chosen
randomlyChosenCategory = random.choice(listOfCategories)

# used https://fsymbols.com/generators/carty/ text art generator to create the title
print("\n-------------------------------------------------\n")
print(" █ █ █ █▀█ █▀█ █▀▄ █▀▀ █ █ █▀▀ █▀ █▀ █▀▀ █▀█")
print(" ▀▄▀▄▀ █▄█ █▀▄ █▄▀ █▄█ █▄█ ██▄ ▄█ ▄█ ██▄ █▀▄")
print("\n-------------------------------------------------\n")

# prints a menu of word categories for players to choose from
print(" ___________________________ ")
print(" | categories               |")
print(" |--------------------------|")
print(" | plants                   |")
print(" | animals                  |")
print(" | foods                    |")
print(" | objects                  |")
print(" | countries                |")
print(" | random (extra hard!)     |")
print(" --------------------------- \n\n")

# instructions to play
print("welcome to word guesser!\n")
print("- lives =" + printLivesAsHearts(10))
print("- incorrect letter/word = -\u2764\uFE0F")
print("- if you want a hint, type HINT in all caps")
print("- if you want to give up, type 'I give up'\n")

# asks player to chooses a category
key = input("type the category you want to guess a word from\n")
print("")

# sets the answer to the randomly selected
answer = getWordFromCategory(key)

# I wrote this second half of the code
length = len(answer) # number of letters in answer
lives = 10 # gives user 10 lives to start off with
won = False # variable to determine whether player has won
letterFound = False # variable to determine if guessed letter is found
print("category: " + key) # print category chosen
print("the answer has " + str(length) + " letters") # print number of letters in answer
print("lives left: " + printLivesAsHearts(lives)) # prints number of lives left
guessed = [] # list of guessed letters
while lives > 0: # game ends when lives are out
    guess = input("guess a letter or word: ") # asks user to guess
    print(" ")
    print("you guessed: " + str(guess)) # prints guess

    # if the player's guess is longer than 1 letter, they are guessing the word, asking for a hint, or giving up
    if len(guess) > 1:
        if(guess=="HINT"): # gives user a hint
            print("hint: " + str(random.choice(answer)))
        if(guess=="I give up" or guess=="i give up"): # sets lives to 0 if player gives up
            lives = 0
        elif(guess == answer): # player wins if their guess is the answer
            print("correct")
            won = True
            lives = 0 # the lives are set to 0 to end the game
        else: # the player has incorrectly guessed the word, so a life is subtracted
            lives = lives - 1
            print("try again")
            print("lives left: " + printLivesAsHearts(lives))
    else: # the user is guessing a letter
        letterFoundInWord = False # will be changed to true if found
        for i in answer: # loops through the word to see if the guessed letter is in it
            if guess == i: # player has guessed a letter in the word
                letterFoundInWord = True
                guessed.append(i)
                print("correctly guessed letters: " + str(guessed))
                letterFoundInWord = True
        if letterFoundInWord == False:
            lives = lives - 1
            print("lives left: " + printLivesAsHearts(lives))
        else:
            print("lives left: " + printLivesAsHearts(lives))
            letterFoundInWord = False

if lives == 0 and won == False: # player has run out of lives or given up and has lost
    print("out of lives\nthe answer was " + str(answer))
