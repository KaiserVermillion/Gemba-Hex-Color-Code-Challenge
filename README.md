
# Hex Colors Code

This project enables users to convert a word to a valid hex string if it satisfies requirements.
They will also be able to parse large text files which contain words in the form of a list.



## Requirements

To run this solution make sure you have `python 3.7` if you do not please go [here](https://www.python.org/downloads/release/python-3715/).

That's it, that's all you need and you are good to go! :)
## Demo

To run this project simply run the MainScript.py file. This will greet you with a simple to use user interface


                        WELCOME USER TO THE WORD TO HEX PROGRAM PLEASE CHOOSE FROM THE FOLLOWING:
                
                        ┌───────────────────────────────────────────────────────────────────────┐
                          note to user: ensure that files are saved in the read_in_files folder
                                            if you inted on using option 1
                        └───────────────────────────────────────────────────────────────────────┘
                
                                            1) Select a file from the list
                                                 2) Enter a file path
                                                    3) Enter a word
                                                    4) Exit Program

From here you will be able to select an option by typing it into the CLI. 

#### - Option 1 -
Will allow you to choose from a list of files placed with in the assets/read_in_files directory
doing so will read the file in and then proceed to process the words in the file.

[NOTE: When using Option 1 make sure the each word is on a new line.]

#### - Option 2 -
Will allow you to choose any file within the system as long as the program has access to it and will
convert the words to hex if there are and as long as they follow file structure in the NOTE above.

#### - Option 3 -

Pass in a custom word either of length 3 or 6 and ensure it has characters that can be converted to hex. This will
output ever combination of the word that can be created into hex form.

#### - Option 4 - 

I mean it does what it says on the can. :)
# Theory

### > Main solution (pièce de résistance)

Within in this section I will discuss the logic behind the different solutions and provide more ways
to solve the problem that I may not have listed out below.

The solution which is in the WordsToHex.py script takes advantage of binary numbers as a way 
to identify all combinations. Lerts says we have the cassia, in this string we have 2 As 2 Ss
and 1 I, all of which can be converted to a hex chars, however the As can either be represented 
as an A in themselves of as the number 4 so there exists multiple combinations of this word in
hex form.

To address this problem and identify all versions of this hex string. I began by assigning 0s and 1s
to each repective character as shown below.

                                                    CASSIA
                                                    010001
    
The number 1 represents a letter which can be both a hex letter and a hex number and 0 which 
represents a hex char or a char which is not hex. Now that we know where all the chars which will not
need to change and the one will need change, we can generate all combinations of 0s and 1s for a string
of length 6 and use this binary representation of the inital string as a filter to find all binary strings
that follow its pattern.


                                              CASSIA      000000
                                              C4551A      010000
                                              CA5514      000001
                                              C45514      010001

The filter in this case is essentially find the binary string whos 0s are in the same location 
as the ones in the orignal string, as  we do not need to changes thoes. Then from there its just a
matter of replacing the numbers to their respective letters. This method will yield the correct
number of combinations for any given word.

### > Alternate solution 1 (Divide And Conquer)

This method makes a few assumptions, first of which is that it is very unlikley that a word 
will satisfy the conditions for it to be converted into a hex word and also have 2 chars
which can be converted into hex be in the same half of the string. For example...

                                                    CAS SIA

Here the word from before is split into 2 so that both As are in 2 differnet parts, and thus 
making it eaiser to convert the As and the rest of the 2 halfs accordingly and then mix them 
up.

                                                    CAS SIA
                                                    C45 51A
                                                    CA5 514
                                                    C45 514

This method will result in only 4 strings being created. This will mean that even if there was
a string which had more than 4 versions of its self you would only ever get back 4 hence why 
I decided to go back to the drawing board for a new solution.

### > Alternate solution 2 (Brute Force)

This approach takes a while to run due the amount of hex values it needs to generate, but it essentially
involves creating a list of Hex values of length 3 and 6 and then writing these to a file. Using the file
as a dictonary where the hex representation is equal to the word in english, the program can then seach text 
and match the words to ones in the file and out put the hex value. This solution can be sped up if the word hex
list is generated before hand and then used, however if it needs to be generated each time its ran then it will
be very slow.
# Documentation

In this section I will describe the project structure and outline how the code works.

## > Project Structure

```
HEXCOLORS/
├── assets/
│   ├── english-words-master
│   ├── read_in_files
│   │    ├── words_alpha.txt
│   │    ├── words_dictionary.json
│   │    └── words.txt
│   └── HexWords.txt
│   
├── test/
│   └── test.py
│   
├── WordsToHex/
│    ├── __pycache__
│    └── WordsToHex.py
│ 
├── alternateSolutions.py 
├── MainScript.py
└── README.md
```
The assets folder contains data and files which can be used by the program, when it is being run
to test it.

The test folder contains python scripts which are used to run tests on the project to ensure
that the methods are running as intended.

WordsToHex contains the main class script which is used to run the main solution as described before.

alternateSolutions.py are were the method for the first alternate solution described above was placed
as I didnt want it taking up space in the main script.

MainScript.py is where the user interface is ran and is the script that needs to be ran to 
start the program.

### > WordsToHex.py

#### -  parseFile

```python
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
```

This method uses built in python modules to open a given file and returns the lines from the file
as a list of words. Ensure that the file has each word on a new line. This method was made to deal with 
txt files.

#### -  preProcess

```python
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
```

With this method I can filted the output list from parseFile and find words which match the criteria
that will allow them to be converted to their respective hex representations. Using regex with the help
of python re module I am able to match words that have required chars for them to be converted.

#### > readWords

```python
def readWords(self, filePath):
        """
        readWords takes in a file and depending on the type processes it differently and generate the hex words

        :params filePath: the path of the fi
        """
        hexWords = []
        parsedFile = self.parseFile(filePath)
        isJson = re.search(r'(?<=\.).*',filePath[1:])

        try:
            if(isJson.group() == "json"):
                parsedFile =  self.parseJSON(filePath)
        except:
            return False

        if not parsedFile:
            print ("ERROR SPECIFIED PATH CANNOT BE LOCATED, PLEASE TRY AGAIN")
            return
        else:
            processedList =  self.preProcess(parsedFile)

            for i in processedList:
                hexWords.append( self.wordsToHex(i))

            self.writeToFile(hexWords)
        return
```

Given a file path this method will parse the file however if its a JSON file it will need 
to handle it slightly differently due to the way that JSON objects are normally formatted
a seperate method will handle parsing that file. Once the file is parsed the word list generated
from this process will be filted to remove words which cannot be converted and remaining
ones will be converted added to a new list and also wrote to a txt file so it can be viewed later.

#### > createBinaryRepresentation

```python
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
```
This method checks if each char of a string is in both the list that contains the hex letters
and if the char is in the dictonary which contains the letter to number conversions. If it is
then it will assing that letter a 1 by placing it in the same location as char in the string
but inside the list. The list is then returned filled with 0s and 1s represening the english
word passed to it.

#### > processList

```python 
def processList(self, binaryRep, versions):
        """
        processList filters the different binary representations (versions) of a word based on the original binary represenation (binaryRep)
        and returns only the ones which match the original word.

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
```

Here we need to process the list of binary values that are generated by using the 
binary representation of the word as a filter. [Here](https://github.com/KaiserVermillion/Gemba-Hex-Color-Code-Challenge#theory) 
I discuss why this is done and this method does this by first makeing a list of indeicies
where the 0s are in the original binary representation (binaryRep), then loops through 
the list of tuples (versions) and makes a list for each tuple of where the 0s are.
The two lists are then compared and if the index for the 0s are the same then that is one
of the binary represenations we can use to represent the combination.

#### > wordsToHex

```python
    def wordsToHex(self, word):
        """
        wordsToHex uses the word given to it (word) and makes the different binary versions of it and then reconstruct the word
        in hex form, adds it to the list and retunrs it.

        :params word: Is the string we are trying to convert to hex
        :returns: A list of strings that are the hex representations of the word passed to the method
        """
        binaryRep = self.createBinaryRepresentation(word)
        

        if (len(word) == 3):
            binaryWords = self.processList(binaryRep,versions3)
        elif(len(word) == 6):
            binaryWords = self.processList(binaryRep,versions6)
        else:
            return "ERROR WORD LENGTH EXEEDS LEGAL HEX VALUE LENGTH"

        finalHex = []
        strConstruct = ""
        
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
```

wordsToHex is the core method and is returns the hex conversions of the word passed to it
once it gets the list of binary represenations from processList it loops through them 
and turns the binary values into chars and reconstructs the string from the binary data. 
Before adding the word to the list it will pass it to a few more method to make sure no 
chars were missed and then appends it to a list.

#### > formateHex

```python
    def formatHex(self, hex):
        """
        formateHex concatenates the # symbol to the front and make all the chars in the string uppercase

        :params hex: Is a string of chars 
        :returns: A string with a # appended to the front and all the chars converted to uppercase
        """
        return "#" + hex.upper()
```

This method is just to make add the # to the first of the regenerated string and make it caps.

#### > isHex
```python
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
```

This method converts any missed chars in the string by checking if the char is in the letter to 
number dictonary and not in the hex alphabet characters.

#### > writeToFile

```python
    def writeToFile(self, hexList):
        """
        writeToFile is incharge of adding the strings passed to it via the hexList parameter to a txt file where
        each string has a new line.

        :params hexList: is a list of string which should have been converted and processed into hex codes
        """
        try:
            file = open("./assets/HexWords", "w")
            for tmp in hexList:
                for i in tmp:
                    file.write("%s\n" % i)
            file.close()
        except:
            return("ERROR CANNOT WRITE TO FILE ADD A FILE NAMEED HexWords.txt TO THE ASSETS FOLDER")
```

Once all the hex values are generated, they are output to a test file so it can be viewed eaiser by the user
the list passed to this method has nested list where the nested lists contain variations of hex string for a 
given word, which is why a nested for loop is used to write them to a file.

### > MainScript.py

This is where the user interface lives and makes interacting with the program eaiser.

#### > getFiles

```python
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
```

Using this method will return a list of file names in the same order as they are listed in the 
directory and it will then print it out onto the screen so the user can select which file to run.

#### > customWord

```python
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
```
This is option 3 on the user interface and it takes a word converts it to lower case and make sure the
word is suitable for converstion before converting it. Once we have established it can be converted
it is passed to the method previously mentioned (wordsToHex) and its converted.

#### > userInterface

```python
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
            test = GSobject.readWords(filepath)

            if(test == False):
                print("ERROR CANNOT PROCESS FILE")

        elif option == "3":

            word= input("Enter a word you wish to convert:")
            print(customWord(word))

        elif option == "4":

            alive = False
            
        else:
             print("Not a valid option please enter a value the give ones above")
```
Using pythons input method this method allow a user to interact with the program by providing
options from them to choose from. Depending on the option it will trigger a certain method unless
they pick 4 in which it will end the program. Option 1 will used the file names returned from 
getFiles and index the list to choose the correct file based on their input.

## Time Complexity

In this section I will discuss the Time Complexity of main solution and the fucntions that are
more than just calling other python functions, as most of the time complexities for thoes functions
can be found online.

Due to the potential size of files being ran into the program
it would be in my best intrest to consider the potential 
run time of methods as to determine how viable my soultion may be.


### parseFile
```python
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
```

This method uses list comprehension to create a list of words which have been take from the imput file.
The time complecity for the for loop will be O(n) as the time take depends on the size of file.readlines().
The strip method used here will have a time complexity of O(n), as this was used to strip anything that wasnt
associated to the intial string. As a result this method will a time complexity of O(n).

### preProcess

```python
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
```

In this method we have a for loop as part of the python list comprehension so there are 2 
process happening here, first is the loop then the appending to the list. The time complexity for 
the for loop would be O(n) as the time it takes to run depends on the size of words list, and to append
these items to the list is O(1), as a result this line would have a time complexity of O(n).

The next part is the if statement its only comparing the side of the new list to 0. The len 
method in python works by calling a pre-defined function which stores the count of a list
as its being added to so there is no need to loop through to count the values thus give that 
process a time complexity of O(1) and the if statement will have a time complecity of O(1) too.

As a result, this methods time complexity would be O(n) as this is the worst case senario for it.

### createBinaryRepresentation

```python
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
```

This method is quite simple, in that its only an if statement and a for loop. The for loops time 
complexity will scale with the side of the word, thus will be O(n). The check inside of the for loop
calls the in method twice this operator vairies in run time depending on the context. When used
on a list it has a time complexity of O(n) and when used on a dict the average time complexity O(1), however
the worst case is O(n). We are only concerened with the worst case so we can say that has a time complexity of 
O(n). As a whole this method will have a time complexity of O(n).


### processList

```python
    def processList(self, binaryRep, versions):
        """
        processList filters the different binary representations (versions) of a word based on the original binary represenation (binaryRep)
        and returns only the ones which match the original word.

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
```
This method uses a few python functions whos time complexity needs to be discussed. Firstly, enumerate
this method returns an [iterator](https://anandology.com/python-practice-book/iterators.html) which poits to 
first item in the list and returns the next item when next() is called. So to reach the end of the list
it would take n jumps thus giving us a time complexity of O(n). Later on this for loop is used
once again inside another loop which retuns in that next loop having a time complexity of O(n^2). Meaning this
method has a worst case time complexity of O(n^2). 

### readWords
```python
    def readWords(self, filePath):
        """
        readWords takes in a file and depending on the type processes it differently and generate the hex words

        :params filePath: the path of the file
        """
        hexWords = []
        parsedFile = self.parseFile(filePath)
        isJson = re.search(r'(?<=\.).*',filePath[1:])

        try:
            if(isJson.group() == "json"):
                parsedFile =  self.parseJSON(filePath)
        except:
            return False

        if not parsedFile:
            return False
        else:
            processedList =  self.preProcess(parsedFile)

            for i in processedList:
                hexWords.append(self.wordsToHex(i))

            self.writeToFile(hexWords)
        return
```

As metioned before parseFile has a time complexity of O(n) and the time complexity of preProcess
is O(n) as well the if statements should all have a time complexity of O(1). This method makes a call to 
the wordsToHex method which makes calls to the O(n^2) method processList, resulting in this methods
worst case time complecity of O(n^2).

### wordsToHex

```python
 def wordsToHex(self, word):
        """
        wordsToHex uses the word given to it (word) and makes the different binary versions of it and then reconstruct the word
        in hex form, adds it to the list and retunrs it.

        :params word: Is the string we are trying to convert to hex
        :returns: A list of strings that are the hex representations of the word passed to the method
        """
        binaryRep = self.createBinaryRepresentation(word)

        if (len(word) == 3):
            binaryWords = self.processList(binaryRep,versions3)
        elif(len(word) == 6):
            binaryWords = self.processList(binaryRep,versions6)
        else:
            return "ERROR WORD LENGTH EXEEDS LEGAL HEX VALUE LENGTH"

        finalHex = []
        strConstruct = ""
        
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
```
As mentioned above we can declare that this method has a worst case time complexity of
O(n^2) firstly due to the nexted for loops, which are used to reconstruct the binary represented
strings and secondly the call to processList which itself has a worst case time compelxity of
O(n^2) which is used to find the combination of words that can be made based on the binary represenation 
of a word.

### formatHex 

```python
    def formatHex(self, hex):
        """
        formateHex concatenates the # symbol to the front and make all the chars in the string uppercase

        :params hex: Is a string of chars 
        :returns: A string with a # appended to the front and all the chars converted to uppercase
        """
        return "#" + hex.upper()
```

This method makes a call to upper(), before python 3.3 it used an api to convert the chars of the string
since then python now uses simple case mappings, which I assume means a dictonary of some sort meaning that reading 
from it would have a worst case time complexity of O(n), making this method have a worst case time complexity of
O(n).

### isHex

```python
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
```

This method has a worst case time complexity of O(n) due to the time taken for the for loop completing
scales with the size of hex.

### writeToFile

```python

    def writeToFile(self, hexList):
        """
        writeToFile is incharge of adding the strings passed to it via the hexList parameter to a txt file where
        each string has a new line.

        :params hexList: is a list of string which should have been converted and processed into hex codes
        """
        try:
            file = open("./assets/HexWords", "w")
            for tmp in hexList:
                for i in tmp:
                    file.write("%s\n" % i)
            file.close()
            return
        except:
            return("ERROR CANNOT WRITE TO FILE ADD A FILE NAMEED HexWords.txt TO THE ASSETS FOLDER")
```

 Due to the nested for loop I can state that this method has a time complexity of O(n^2), however 
 this may not be the true time complexity of this method as it used open and write whos time complexity 
 varies depending on the operations performed as well as the system configurations.

 ## Unit Testing

To execute the unit test run this command `python -m unittest`


## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

