def divideAndConq(self,word):
     """
     divideAndConq divides a word into 2 and converts the values which can be converted from and identifies the 
     differnt combinations of the values that are avalible. The assumption made here is that there is no word that 
     wil satisfy.
     :param word: A string
     :return: A list of words which contains all the possible combinations of the string reconstructed from the 4
              parts listContA, listContB, strA and strB
     """
     listContA = ""
     listContB = ""
     strA = word[:len(word)//2]
     strB = word[len(word)//2:]
     for i in range(len(strA)):
         tempLetter = strA[i]
         if tempLetter in letterMap.keys():
             listContA = strA.replace(tempLetter, letterMap[tempLetter])
     for i in range(len(strB)):
         tempLetter = strB[i]
         if tempLetter in letterMap.keys():
             listContB = strB.replace(tempLetter, letterMap[tempLetter])
     return [strA+listContB,strA+strB,listContA+strB,listContA+listContB]

     
# Generates a new string by replacing values which 
# Solution 1
# If its already a hex value in the string dont replace it
def wordToHex(self, word):
     """
     wordToHex
     """
     counter = 0
     for x in range(len(word)):
         if word[x] in letterMap.keys() and word[x] in hexAlpha:
             counter += 1
     if counter == 2 :
         return self.divideAndConq(word)
     else:
         for i in range(len(word)):
             # tempLetter = word[i]
             if word[i] in letterMap.keys():
                 word = word.replace(word[i], letterMap[word[i]])
     return word