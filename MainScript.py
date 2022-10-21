import WordsToHex.WordsToHex as GS
from os import listdir
from os.path import isfile, join
import re

def getFiles():
    """
    getFiles will enter the target folder specifies in the filePath variable and add the names of the 
    files in that folder into a list.

    :returns: A list containing the names of all the files in the folder
    """
    filePath = "./assets/read_in_files"
    file = [f for f in listdir(filePath) if isfile(join(filePath, f))]
    for i in file:
        print(str(file.index(i) + 1) + ") " + i + '\n')
    return file

def customWord(word):
    """
    customWord recieves a string and processes it and if the string is valid it will convert the string
    so its hex form.

    :params word: A string of chars of length 3 or 6
    :returns: either an error message if the string cannot be converted or the converted string
    """
    GSobject = GS.HexGenerator()
    val = GSobject.preProcess([word.lower()])

    if val != False:
        return GSobject.wordsToHex(val[0])
    else:
        return "WORD CANNOT BE CONVERTED IT MUST CONTAINS CHARS WITHIN THE HEX RANGE AND MUST HAVE A LENGTH OF 3 OR 6"

def userInterface():
    """
    userInterface is used to help user navigete the program by providing them with options and showing
    error messages accordingly to make sure they are made clear what is happening.
    """
    GSobject = GS.HexGenerator()
    alive = True

    print("""
        WELCOME USER TO THE WORD TO HEX PROGRAM PLEASE CHOOSE FROM THE FOLLOWING:

        ┌───────────────────────────────────────────────────────────────────────┐
          note to user: ensure that files are saved in the read_in_files folder 
                            if you inted on using option 1                      
        └───────────────────────────────────────────────────────────────────────┘

                            1) Select a file from the list
                                 2) Enter a file path
                                    3) Enter a word
                                    4) Exit Program
    """)

    while(alive):
        print("Enter option")
        option = input()

        if option == "1":
            files = getFiles()
            fileNum = input("Enter the number of the file you wish to read in: ")
            fileName = files[int(fileNum) - 1]
            GSobject.readWords("./assets/read_in_files/" + fileName)
        elif option == "2":
            filepath = input("Enter the full file path:")
            GSobject.readWords(filepath)

        elif option == "3":
            word= input("Enter a word you wish to convert:")
            print(customWord(word))

        elif option == "4":
            alive = False
            
        else:
             print("Not a valid option please enter a value the give ones above")
        

userInterface()