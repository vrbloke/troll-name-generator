#Troll name generator v2
#Assembles random names from collection of vowels and consonants

import random
import string
version = "1.0"

print("TROLL NAME GENERATOR v" + version)

#Variables I will use
vowels = "aeiou"
vowels_uppercase = 'AEIOU'
consonants = "bcdfghjklmnpqrstvwxz"
consonants_uppercase = 'BCDFGHJKLMNPQRSTVWXZ'
name = ""
consonant_count = 0
vowel_count = 0

random.seed()

#Name generation process
name += random.choice(string.ascii_uppercase)
for i in range(5):
    #Basic process for version 1.0: Only prevent more than 2/3 consonants/vowels in a row
    if consonant_count > 3:
        consonant_count = 0
        name += random.choice(vowels)
        vowel_count += 1
    elif vowel_count > 2:
        vowel_count = 0
        name += random.choice(consonants)
        consonant_count += 1
    else:
        name += random.choice(string.ascii_lowercase)
        if name[-1] in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print(name)
