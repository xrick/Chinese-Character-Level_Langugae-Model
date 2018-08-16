import numpy as np
import os
import re

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
    main()
                
