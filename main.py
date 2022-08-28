from genericpath import exists
import os
import string
import sys
from tokenize import String
import random
import csv
from typing import final

import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.stem import WordNetLemmatizer

import re

POSSIBLE_FORMATS = ["{adj}", "{noun}"]
DEFAULT = ''

NOUN = 1
ADJ = 0
MAX_RANDOM = 1000
# ALL_CAPS
# UPPERCASE
# LOWERCASE


NOUN_LIST = "animalList.csv"
ADJ_LIST = "english-adjectives.csv"

def randomWord(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        randomRow = random.choice(list(reader))
    
    randomWord = randomRow.pop()
    return randomWord

def main():
    args = sys.argv
    lemmatizer = WordNetLemmatizer()

    
    

    # Check if given default or specific format
    if args[1] == DEFAULT : formatListInitial = "The {adj} {noun}"
    else: formatListInitial = args[1]

    blackListedWordsInitial = args[2].lower()

    # Text Pre Processing

    # Remove any symbols from blacklisted and formated word list
    formatPunct2Space = re.sub(r'[^A-z\s{}]', ' ', formatListInitial)
    formatNoSpaceAlt = re.sub(r'\s+', ' ', formatPunct2Space)
    formatListAdjective = re.sub(r"{[aA][dD][jJ][A-z]*}", "{adj}", formatNoSpaceAlt)
    formatListNoun = re.sub(r"{[nN][oO][uU][nN]}", "{noun}", formatListAdjective)
    formatList = formatListNoun.split()
    print(formatList)

    blPunct2Space = re.sub(r'[^A-z\s]', ' ', blackListedWordsInitial)
    blNoSpaceAlt = re.sub(r'\s+', ' ', blPunct2Space)
    blackListedWords = blNoSpaceAlt.split()

    # Style of word
    capitalBool = args[3]

    # separator between words
    if len(args)-1 < 4: seperator = ''
    else: seperator = args[4]

    # true false for random number generator
    if len(args)-1 < 5: RNG = False
    else: RNG = args[5]



    formatChoice =  {}
    formatChoiceIndices = []
    chosenWord = {}
    wordIndex = 0

    
    print(blackListedWords)

    # Check if a word is either a format to be replaced (eg. {ajd}), or a word they want included
    for word in formatList:
        if(word in POSSIBLE_FORMATS):
            formatChoice.update([(wordIndex, word)])
            formatChoiceIndices.append(wordIndex)
            wordIndex += 1
        else:
            chosenWord.update([(wordIndex, word)])
            wordIndex += 1
    maxWordCount = wordIndex

    # Lemmatize and casefold every word in the blacklisted words
    processedBlackListedWords = []
    for blackListWord in blackListedWords:
        processedBlackListedWords.append(lemmatizer.lemmatize(blackListWord))
    
    print(processedBlackListedWords)

    # Replace format option with a random word from the list
    # If random word is blacklisted, choose a new random word
    finalFormats = {}
    for formatOption in formatChoice.keys():
        if(formatChoice.get(formatOption) == POSSIBLE_FORMATS[NOUN]):
            randomNoun = randomWord(NOUN_LIST)
            while(randomNoun in processedBlackListedWords):
                randomNoun = randomWord(NOUN_LIST)
            finalFormats.update([(formatOption, randomNoun)])

        elif(formatChoice.get(formatOption) == POSSIBLE_FORMATS[ADJ]):
            randomAdj = randomWord(ADJ_LIST)
            while(randomAdj in processedBlackListedWords):
                randomAdj = randomWord(ADJ_LIST)
            finalFormats.update([(formatOption, randomAdj)])
    
    # Append all the words into the final word list/string

    i = 0
    wordList = []
    while i < maxWordCount :
        if i in formatChoiceIndices:
            wordList.append(finalFormats.get(i))
        else:
            wordList.append(chosenWord.get(i))
        i+=1

    finalWordList = []

    # Change the format of the words depending on the option of the user (lower case, upper case, and capitalization)
    if(capitalBool == "All Caps"):
        for word in wordList:
            finalWordList.append(word.upper())
    elif(capitalBool == "Lowercase"):
        for word in wordList:
            finalWordList.append(word.lower())
    elif(capitalBool == "Capitalize"):
        for word in wordList:
            finalWordList.append(word.capitalize())

            
    if(RNG == "True"): finalWordList.append(str(random.randint(0, MAX_RANDOM)))

    print(seperator.join(finalWordList))

if __name__ == "__main__":
    main()

