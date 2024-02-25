

from sentences import *
from prompts import *
from mad_libs import mad_libs_list
from definitions import definitions
import os

global choice
choice = 0

def return_sentence(choice, index):
    match choice:
        case 1:
            return camping_sentence_chunks[index]
        case 2:
            return hospital_sentence_chunks[index]
        case 3:
            return zoo_sentence_chunks[index]

def menu():
    global choice
    os.system("cls")
    print_options(mad_libs_list)
    choice = int(input("Type the corresponding number: "))
    match choice:
        case 1:
            run_one_mad_lib(camping_sentence_chunks, camping_prompts)
        case 2:
            run_one_mad_lib(hospital_sentence_chunks, hospital_prompts)
        case 3:
            run_one_mad_lib(zoo_sentence_chunks, zoo_prompts)
        case _:
            menu()
            
def instructions():
    os.system("cls")
    print("Use all lowercase letters (Except for names). Definitions will be provided.")
    input("Press Enter to continue: ")
    os.system("cls")
    
def print_options(mad_libs):
    for i in range(len(mad_libs)):
        print("Option ", i + 1, ": ", mad_libs[i], sep='')
    
# Every mad lib MUST START with a sentence chunk
def run_one_mad_lib(sentence_chunks, prompts):
    
    # 1) Print the instructions for the user
    instructions()
    
    finalSentence = ""

    # 2) This loop will go through all the words from 2) and combine sentences bits with user input automatically
    for i in range(len(prompts)):
        finalSentence += make_sentences(prompts[i], i)
        os.system("cls")

    # 3) Optional step: Add the final bit of generated sentence if the mad lib doesn't end with user input
    if len(sentence_chunks) > len(prompts):
        finalSentence += sentence_chunks[len(sentence_chunks) - 1]

    # 4) Print and Wait for user to read before moving on
    print(finalSentence)
    input("Press Enter to continue: ")
    
    # 5) Clear the sentence and return to menu
    menu()
    
def make_sentences(descriptor, index):
    
    userPhrase = ""
    # First add the generated sentence to the final sentence
    userPhrase = str(return_sentence(choice, index))
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