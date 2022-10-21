
# Hex Colors Code

This project enables users to convert a word to a valid hex string if it satisfies requirements.
They will also be able to parse large text files which contain words in the form of a list.




## Documentation

In this section I will describe the project structure and outline how the code works.

### > Project Structure

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

### -  parseFile

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

### -  preProcess

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



```python

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
```
# Demo

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

### -  parseFile

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

### -  preProcess

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

### > readWords

```python
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
```

Given a file path this method will parse the file however if its a JSON file it will need 
to handle it slightly differently due to the way that JSON objects are normally formatted
a seperate method will handle parsing that file. Once the file is parsed the word list generated
from this process will be filted to remove words which cannot be converted and remaining
ones will be converted added to a new list and also wrote to a txt file so it can be viewed later.
## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

