import GembaScript as GS
import os
import os.path

filename = "lol"


fileName2 = "C:/Users/Kog Arun/Documents/Gemba Advantage Coding Test/english-words-master/words_alpha.txt"
# test1 = GS.WordsToHex(fileName2)
# tmpHolder = test1.parseFile(fileName2)
# tmpHolder2 = test1.preProcess(tmpHolder)

# for i in tmpHolder2:
#     tmpList.append(test1.wordsToHex(i))

# test1.writeToFile(tmpList)


# print(tmpList)
# print(len(tmpList))

def getFiles(filePath):
    print("lmfao")

def readWords(filePath):
    tmpList = []
    test1 = GS.WordsToHex(filePath)
    tmpHolder = test1.parseFile(filePath)

    if not tmpHolder:
        print ("ERROR SPECIFIED PATH CANNOT BE LOCATED, PLEASE TRY AGAIN")
        return
    else:
        tmpHolder2 = test1.preProcess(tmpHolder)

        for i in tmpHolder2:
            tmpList.append(test1.wordsToHex(i))

        test1.writeToFile(tmpList)
        #print(tmpList)
    return
    
def customWord(word):
    test1 = GS.WordsToHex("lol")
    val = test1.preProcess([word.lower()])

    if val != False:
        print(test1.wordsToHex(val[0]))
    else:
        print("WORD CANNOT BE CONVERTED MAKE SURE ITS EAITHER 3 OR 6 CHRACTERS LONG")
        return

def userInterface():

    alive = True

    print("""
        WELCOME USER TO THE WORD TO HEX PROGRAM PLEASE CHOOSE FROM THE FOLLOWING:

                            1) Select a file from the list
                                 2) Enter a file path
                                3) Enter a custom word
                                    4) Exit Program
    """)

    while(alive):
        print("Enter option")
        option = input()

        if option == "1":
            getFiles("lol")
            print(option)
        elif option == "2":
            filepath = input("Enter the full file path:")
            readWords(filepath)
        elif option == "3":
            word= input("Enter a word you wish to convert:")
            customWord(word)
        elif option == "4":
            alive = False
        else:
             print("Not a valid option please enter a value the give ones above")
        

userInterface()