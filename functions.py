

from sentences import *
from definitions import definitions
import os

finalSentence = ""
global choice
choice = 0

def returnSentence(choice, index):
    match choice:
        case 1:
            return campingSentence[index]
        case 2:
            return hospitalSentence[index]

def makeSentences(descriptor, index):
    
    userPhrase = ""
    # First add the generated sentence to the final sentence
    userPhrase = str(returnSentence(choice, index))
    # This prints the word the user needs to type
    print(index + 1, ": ", descriptor, ";", end=" ", sep='')
    i = 0
    # This prints the definition of the input word for the user if it has one
    while i < len(definitions):
        if definitions[i][0] == descriptor:
            print(definitions[i][1])
            break
        i += 1
    #Now take the existing "userPhrase" which is the generated sentence and add the users word next
    print(type(userPhrase))
    userPhrase = userPhrase + " " + input("Print: ")
    return userPhrase

def instructions():
    os.system("cls")
    print("Use all lowercase letters (Except for names). Definitions will be provided.")
    input("Press Enter to continue: ")
    os.system("cls")

def menu():
    global choice
    os.system("cls")
    print("Option 1: Camping")
    print("Option 2: Hospital")
    choice = int(input("Type the corresponding number: "))
    match choice:
        case 1:
            camping(finalSentence)
        case 2:
            hospital(finalSentence)
        case _:
            menu()

def camping(finalSentence):
    
    
    # 1) Print the instructions for the user
    instructions()
    
    # 2) This is all the things (in order!) that the user must come up with words or phrases for
    words = ["Proper noun", "Noun", "Adjective", "Verb", "Adjective", "Animal", "Verb", "Color", "Verb", "Adverb", "Number", "Measure of time", "Color", "Animal", "Number", "Silly word", "Noun"]

    # 3) This loop will go through all the words from 2) and combine sentences bits with user input automatically
    i = 0
    while i < 17:
        finalSentence += makeSentences(words[i], i)
        os.system("cls")
        i+=1

    # 4) Optional step: Add the final bit of generated sentence if the mad lib doesn't end with user input
    finalSentence += campingSentence[i]

    # 5) Print and Wait for user to read before moving on
    print(finalSentence)
    input("Press Enter to continue: ")
    
    # 6) Clear the sentence and return to menu
    finalSentence = ""
    menu()
    
def hospital(finalSentence):
    
    instructions()
    
    words = ["Number", "Measure of time", "Mode of transportation", "Adjective", "Adjective", "Noun", "Color", "Part of the body", "Verb", "Number", "Noun", "Noun", "Part of the body", "Verb", "Noun", "Adjective", "Silly word", "Noun"]
    
    i = 0
    while i < 18:
        finalSentence += makeSentences(words[i], i)
        os.system("cls")
        i += 1
    
    
    finalSentence += hospitalSentence[i]
    
    print(finalSentence)
    input("Press Enter to continue: ")
    
    finalSentence = ""
    menu()