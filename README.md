
# Hex Colors Code

This project enables users to convert a word to a valid hex string if it satisfies requirements.
They will also be able to parse large text files which contain words in the form of a list.




## Requirements

To run this project, you will need to make sure you have the following versions of python

`Python 3.7`

If you do not have this version of python please go [here](https://www.python.org/downloads/release/python-3715/) and download the correct version.

Now you should be all set! :)

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
## Theory

### > Main solution

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

## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

