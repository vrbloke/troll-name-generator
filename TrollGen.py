#Version 1.1 comes with eXCITING UI & BETTER NAMES

from random import choice
import random
import string

version = "1.1"
consonants = "bcdfghjklmnpqrstvwxz"
vowels = "aeiouy"
random.seed()

#Title
print("TROLL NAME GENERATOR v" + version)

#UI
#Functionality:
#Choose to generate 1, 12 or infinity names
#Choose whether to display name number
#Return to this choice whenever 1 or 12 name generation finishes

while 1:

    amount_of_names = input("How many names would you want to generate?")

    if input("Would you want the names to be numbered? y/n") == "y":
        prefix = True
    else:
        prefix = False

    # Name generation process
    # Choose type of syllable to pick, generate the syllable, make sure it doesn't look terrible with the previous parts
    for n in range(int(amount_of_names)):
        name = ""

        while len(name) < 6:
        # Generate syllable type, make sure it's not too many vowels
            syllable_type = choice(range(4)) #0. CV, 1. VC, 2. CVC, 3. V
            if (len(name) > 1) and (syllable_type == 3) and (name[-1] in vowels) and (name[-2] in vowels): continue
            if syllable_type == 0: #CV
                syllable = choice(consonants) + choice(vowels)
            elif syllable_type == 1: #VC
                syllable = choice(vowels) + choice(consonants)
            elif syllable_type == 2: #CVC
                syllable = choice(consonants) + choice(vowels) + choice(consonants)
            elif syllable_type == 3: #V
                syllable = choice(vowels)

        # Add the syllable
            name += syllable

        name = name[0].upper() + name[1:6]
        print("{}. ".format(n+1) + name if prefix else name)

    #Continue prompt
    if input("Continue? y/n") != "y":
        quit()

