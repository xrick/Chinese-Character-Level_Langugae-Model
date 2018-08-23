import numpy as np
import os
import re
from pickle import dump
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM


def load_doc(filename):
	# open the file as read only
	file = open(filename, 'r')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text


def testmain():
    txtdata = load_doc("rawdata.txt")
    charWordSet = set()
    charWordList = list()
    for line in txtdata:
        filtered = filter(lambda x: not re.match(r'^\s*$', x), line)  # filter the empty line
        line_list = list(filtered)
        if len(line_list) != 0:
            for charWord in line_list:
                charWordSet.add(charWord)
                charWordList.append(charWord)

    print("Total distinct char word is %d" % len(charWordSet))
    print("************************")
    print("Total char words in the article are %d" % len(charWordList))
    for char in charWordSet:
        print("char is :", char)


def main():
    file_path = "rawdata.txt"
    charWordSet = set()
    charWordList = list()
    with open("rawdata.txt","r") as fr:
        lines = fr.readlines()
        for line in lines:
            filtered = filter(lambda x: not re.match(r'^\s*$', x), line) #filter the empty line
            line_list = list(filtered)
            if len(line_list) != 0:
                for charWord in line_list:
                    charWordSet.add(charWord)
                    charWordList.append(charWord)

    print("Total distinct char word is %d" %len(charWordSet))
    print("************************")
    print("Total char words in the article are %d" %len(charWordList))
    for char in charWordSet:
        print("char is :",char)


if __name__ =="__main__":
    #main()
    testmain()

                
