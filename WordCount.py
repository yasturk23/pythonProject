#we will create a word counter

#we ask our user for a question
question = input('Hello! What\'s on your mind today? ')

#we create a function to count each string separated by empty spaces
def count_of_words(str):
    return(len(str.strip().split()))

#we print out the number of string given by the user
print("Okay! You just told me what's on your mind in " + str(count_of_words(question)) + " words!")
print('\t')
print("Anyways, I can count the number of words in a file")

#we ask for the filename
filename = input("Enter a file name:")

#we create a variable for the number of words in the file
number_of_words = 0

#we open the file in read mode and use a for loop to count words
with open(filename, 'r') as f:
    for line in f:
        words = line.split()
        number_of_words += len(words)

#we print out the number of words in the text file
print("The number of words: " + str(number_of_words))
