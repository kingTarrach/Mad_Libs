

from sentences import *
from prompts import *
from mad_libs import mad_libs_list
from prompt_definitions import prompt_definitions
import os

global choice
choice = 0

def menu():
    os.system("clear")              # Clears screen
    get_user_choice()               # Function will run infinitely until user gives a integer response
    match choice:
        # run_one_mad_lib(chunks, prompts)
        case 1:
            run_one_mad_lib(camping_sentence_chunks, camping_prompts)
        case 2:
            run_one_mad_lib(hospital_sentence_chunks, hospital_prompts)
        case 3:
            run_one_mad_lib(zoo_sentence_chunks, zoo_prompts)
        case 4:
            run_one_mad_lib(enchanted_forest_chunks, enchanted_forest_prompts)
        case 5:
            run_one_mad_lib(pizza_chunks, pizza_prompts)
        case 6:
            run_one_mad_lib(animals_chunks, animals_prompts)
        case 7:
            run_one_mad_lib(recipe_chunks, recipe_prompts)
        case 8:
            run_one_mad_lib(mad_scientist_chunks, mad_scientist_prompts)
        case 9:
            run_one_mad_lib(fifty_shades_of_gray_chunks, fifty_shades_of_gray_prompts)
        case _:
            menu()

def return_sentence(choice, index):
    match choice:
        case 1:
            return camping_sentence_chunks[index]
        case 2:
            return hospital_sentence_chunks[index]
        case 3:
            return zoo_sentence_chunks[index]
        case 4:
            return enchanted_forest_chunks[index]
        case 5:
            return pizza_chunks[index]
        case 6:
            return animals_chunks[index]
        case 7:
            return recipe_chunks[index]
        case 8:
            return mad_scientist_chunks[index]
        case 9:
            return fifty_shades_of_gray_chunks[index]
   
def get_user_choice():       
    global choice                       # var choice will be changed globally in this function  
    while True:
        print_options(mad_libs_list)    # Function to print all mad lib option
        choice = input("\nType the corresponding number: ")  
        try:
            choice = int(choice)
            return choice
        except ValueError:
            print("\nPlease enter a valid choice\n") 

def instructions():
    os.system("clear")
    print("Use all lowercase letters (Except for names). Definitions will be provided.")
    input("Press Enter to continue: ")
    os.system("clear")
    
def print_options(mad_libs):
    for i in range(len(mad_libs)):
        print("Option ", i + 1, ": ", mad_libs[i], sep='')
    
# Every mad lib MUST START with a sentence chunk
def run_one_mad_lib(sentence_chunks, prompts):
    
    # 1) Print the instructions for the user
    instructions()
    
    final_sentence = ""

    # 2) This loop will go through all the words from 2) and combine sentences bits with user input automatically
    for i in range(len(prompts)):
        final_sentence += make_sentences(prompts[i], i, len(prompts))
        os.system("clear")

    # 3) Optional step: Add the final bit of generated sentence if the mad lib doesn't end with user input
    if len(sentence_chunks) > len(prompts):
        final_sentence += sentence_chunks[len(sentence_chunks) - 1]

    # 4) Print and Wait for user to read before moving on
    print(final_sentence)
    input("Press Enter to continue: ")
    
    # 5) Clear the sentence and return to menu
    menu()
    
def make_sentences(descriptor, index, p_length):
    
    chunk_and_user_input = ""
    # First add the generated sentence chunk to the final sentence
    chunk_and_user_input = str(return_sentence(choice, index))
    # This prints the word the user needs to type
    print("Prompt ", index + 1, "/", p_length, ": ", "\n", descriptor, end="", sep='')
    i = 0
    # This prints the definition of the input word for the user if it has one
    while i < len(prompt_definitions):
        if prompt_definitions[i][0] == descriptor:
            print(";", prompt_definitions[i][1])
            break
        i += 1
    if i == len(prompt_definitions):
        print()
    #Now take the existing "chunk_and_user_input" which is the generated sentence and add the users word next
    user_input = ""
    while not user_input.strip():
        user_input = input("> ")
    chunk_and_user_input = chunk_and_user_input + " " + user_input
    return chunk_and_user_input