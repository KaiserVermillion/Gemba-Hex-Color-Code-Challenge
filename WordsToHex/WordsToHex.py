import re
import itertools
import json

letterMap = {'o':'0','l':'1','i':'1','a':'4','s':'5','t':'7'}
hexAlpha = ['a','b','c','d','e','f']
lettersReq = ['a','b','c','d','e','f','o','s','t','l','i']

versions3 = list(itertools.product([0, 1], repeat=3))
versions6 = list(itertools.product([0, 1], repeat=5))

class HexGenerator:

    def __init__(self, *args):
        if(len(args) != 0):
            self.file = args[0]

    def parseJSON(self, fileName):
        with open(fileName) as file:
            loaded = json.load(file)
        jsonWords = [i for i in loaded]
        return jsonWords

    def parseFile(self, fileName):
        """
        parseFile recieves a filename and put the values into a list with the newline delimter stripped

        :param fileName: dictates the location of the file in the system
        :return: Returns a list of strings without the newline delimiter and if the file cannot be opened
                 returns False so that the error can be handled.
        """
        try:
            file = open(fileName, 'r')
            lines = [x.strip() for x in file.readlines()]
            return lines
        except:
            return False

    # Removes words which do not need to be processed as they lay outside the max hex value length
    # Regex
    def preProcess(self, words):
        """
        preProcess, filters the original words list to leave behind only words of length 3 or 6 and 
        also words that only contain characters that can either be converted to hex characters or 
        are hex characters already.

        :param words: A list of strings
        :return: Returns a list of strings that are either of length 3 or 6 and have character which can
                 either be converted to a hex char, is already a hex char or satisfies both conditions.
                 If the the word cannot be converted then it will be return False.
        """
        filteredWords = [w for w in words if (len(w) == 3 or len(w) == 6) and re.match("^[abcdefolist]+$",w)]

        if(len(filteredWords) != 0):
            return filteredWords
        else:
            return False

    def readWords(self, filePath):
        """
        readWords takes in a file and depending on the type processes it differently and generate the hex words

        :params filePath: the path of the fi
        """
        hexWords = []
        parsedFile = self.parseFile(filePath)
        isJson = re.search(r'(?<=\.).*',filePath[1:])


        if(isJson.group() == "json"):
            parsedFile =  self.parseJSON(filePath)

        if not parsedFile:
            print ("ERROR SPECIFIED PATH CANNOT BE LOCATED, PLEASE TRY AGAIN")
            return
        else:
            processedList =  self.preProcess(parsedFile)

            for i in processedList:
                hexWords.append( self.wordsToHex(i))

            self.writeToFile(hexWords)
        return


    def createBinaryRepresentation(self,word):
        """
        createBinaryRepresentation injests a string and iterates through each char checking if the char is both a
        hex char on its own and a hex char that can be converted. It will then add a 1 to the check list if it satisfies
        the previously mentioned condition and a 0 if not.

        :param word: A string chracters
        :returns: A list of chars that represents, respectivly which chars can be either a hex char on their own or 
                  converted to one
        """
        check = []
        for i in word:
            if i in hexAlpha and i in letterMap.keys():
                check.append('1')
            else:
                check.append('0')
        return check

    def processList(self, binaryRep, versions):
        """
        processList identifies the index of the 0 values which are in the binary represenation of the word,
        indexes holds this information and is then used to find the binary values with 0 in the corrosponding spots.
        This is done by finding the indecies of the 0 char within the binary values and seeing if they match up with 
        the ones from the original binary representation (binaryRep) which is passed into the method. If its a match
        this is appended to the list.

        :params binaryRep: Is the binary representation of the string we want to identify the possible combinations for
        :params versions: Is a list of tuples that represent every combination of 0s and 1s that can exist from either a length
                          of 3 or 6.

        :returns: The binary representations of every possible combination of a string.
        """
        indexes = [m for m,n in enumerate(binaryRep) if (n =='0')]
        binaryWords = []
        for x in versions:
            xIndexes = [o for o,p in enumerate(list(x)) if (p == 0)]
            if all(item in xIndexes for item in indexes):
                binaryWords.append(x)
        return binaryWords


    def wordsToHex(self, word):
        """
        wordsToHex is the main processing method which first generates all the different combinations of 0s and 1s
        based on the length of the word. The binary representation of the word is then made, both of these values are
        then passed to the processList method which will return the binary representaions of the combinations that exist
        for that word. The binary representations are then looped over and the word is then reconstructed, formatted and
        checked one last time to make sure all the chars are correct.

        :params word: Is the string we are trying to convert to hex
        :returns: A list of strings that are the hex representations of the word passed to the method
        """
        versions = list(itertools.product([0, 1], repeat=len(word)))
        binaryRep = self.createBinaryRepresentation(word)
        

        if (len(word) == 3):
            binaryWords = self.processList(binaryRep,versions3)
        elif(len(word) == 6):
            binaryWords = self.processList(binaryRep,versions6)
        else:
            return ("ERROR WORD LENGTH EXEEDS LEGAL HEX VALUE LENGTH")

        finalHex = []
        strConstruct = ""
        hexStr = ""
        
        for bWords in binaryWords:
            inc = 0
            for t in bWords:
                if(t == 0):
                    strConstruct += word[inc]
                else:
                    strConstruct += letterMap.get(word[inc])
                
                inc += 1
            
            finalHex.append(self.formatHex(self.isHex(strConstruct)))
            strConstruct = ""

        return finalHex

    def formatHex(self, hex):
        """
        formateHex concatenates the # symbol to the front and make all the chars in the string uppercase

        :params hex: Is a string of chars 
        :returns: A string with a # appended to the front and all the chars converted to uppercase
        """
        return "#" + hex.upper()

    def isHex(self, hex):
        """
        isHex loops through and makes sure all values are converted to their correct hex counter parts

        :params hex: Is a string that should contain chars which can either be converted to hex or are themselves
                     already hex chars.
        :returns: A string with the chars converted to hex chars 
        """
        for i in hex:
            if i in letterMap.keys() and not(i in hexAlpha):
                hex = hex.replace(i, letterMap.get(i))
        return hex

    def writeToFile(self, hexList):
        """
        writeToFile is incharge of adding the strings passed to it via the hexList parameter to a txt file where
        each string has a new line.

        :params hexList: is a list of string which should have been converted and processed into hex codes
        """
        file = open("./assets/HexWords", "w")
        for tmp in hexList:
            for i in tmp:
                file.write("%s\n" % i)
        file.close()