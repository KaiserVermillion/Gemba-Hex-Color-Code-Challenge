
# Hex Colors Code

This project enables users to convert a word to a valid hex string if it satisfies requirements.
They will also be able to parse large text files which contain words in the form of a list.




## Requirements

To run this project, you will need to make sure you have the following versions of python

`Python 3.7`

If you do not have this version of python please visit https://www.python.org/downloads/release/python-3715/ and download the correct version.

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
represents a hex char or a char which is not hex.

