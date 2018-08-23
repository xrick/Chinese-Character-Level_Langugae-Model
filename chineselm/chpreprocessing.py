import jieba


def load_doc(filename):
	# open the file as read only
	file = open(filename, 'r')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text


def save_doc(lines, filename):
	data = '\n'.join(lines)
	file = open(filename, 'w')
	file.write(data)
	file.close()

def isLineEmpty(line):
    return len(line.strip()) == 0

def getChineseWordList(filename):
    #load user-define dictionary
    jieba.set_dictionary('dict.txt.tw.big')
    #create stop word set
    stopwordset = set()
    #stop word to stopwordset
    with open('stopWordList_tw.txt', 'r', encoding='utf-8') as sw:
        for line in sw:
            stopwordset.add(line.strip('\n'))
    """ the following is processing the tokens"""
    #txtdata = load_doc(filename)
    charTokenList = list()
    output = open('chwords.txt', 'w')
    with open(filename,'r') as content:
        lines = content.readlines()
        for line in lines:
            #filtered = filter(lambda x: not re.match(r'^\s*$', x), line)  # filter the empty line
            #if len(line_list) != 0:
            if not isLineEmpty(line):
                line.replace("\n", "")
                words = jieba.cut(line, cut_all=False)
                for word in words:
                    word2 = word.strip()
                    if not len(word2) == 0:
                        print("current processing word is : ",word2)
                        if word2 not in stopwordset:
                            #charTokenList.append(word)
                            output.write(word2 + ' ')
    output.close()

    #return charTokenList

def generateSequence(token_seq_filename):
    rawtext = None
    sequences = list()
    with open(token_seq_filename, 'r') as content:
        rawtext = content.read()
        length = 10
        sequences = list()
        for i in range(length, len(rawtext)):
            # select sequence of tokens
            seq = rawtext[i-length:i+1]
            seq.replace("\n","")
            #store
            if not len(seq.strip()) == 0 :
                sequences.append(seq)
                print("seq is :",seq)
    print("The total sequences are : ",len(sequences))
    return sequences




def main():
    #getChineseWordList("rawdata.txt")
    #t = getChineseWordList("rawdata.txt")
    #print("the whole chinese words are : ",t)
    sequence_ = generateSequence("chwords.txt")
    save_doc(sequence_,"ch_char_sequences.txt")




if __name__ == "__main__":
    main()
