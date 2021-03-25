#We will create a Mad Libs game where the user will input a list of adjectives, nouns, and verbs


import random

#we create lists of adjectives, verb, and nouns
adjective = [str(i) for i in input("Enter a list of adjectives separated by space then press Enter:").split(" ")]
noun = [str(i) for i in input("Enter a list of nouns separated by space then press Enter:").split(" ")]
verb = [str(i) for i in input("Enter a list of verbs separated by space then press Enter:").split(" ")]

#Our story is printed below with random elements of the lists
print("In The Jungle!")
print("I walk through the color jungle. I take out my " + random.choice(adjective) + " canteen. ")
print("There's a " + random.choice(adjective) + " parrot with a " + random.choice(adjective) + " " + random.choice(noun) + " in his mouth right in front of me in the " + random.choice(adjective) + " trees! ")
print("I gaze at his " + random.choice(adjective) + " " + random.choice(noun) + ". ")
print("A panther " + random.choice(verb) + " in front of my head! I " + random.choice(verb) + " his " + random.choice(adjective) + " breath. ")
print("I remember I have a packet of " + random.choice(noun) + " that makes go into a deep slumber!")
print("I " + random.choice(verb) + " it away in front of the " + random.choice(noun) + ". ")
print("Yes he's eating it! ")
print("I " + random.choice(verb) + " away through the " + random.choice(adjective) + " jungle. ")
print("I meet my parents at the tent.")
print("Phew; It’s been an exciting day in the jungle.")
