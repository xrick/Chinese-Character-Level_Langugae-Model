
def load_doc(filename):
	# open the file as read only
	file = open(filename, 'r')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text

def getTokens(rawtext):
    tokens = rawtext.split()
    tokenList = ' '.join(tokens)
    print("tokenList is : ",tokenList)
    return tokenList


def createSeq(raw_text):
    # organize into sequences of characters
    length = 10
    sequences = list()
    for i in range(length, len(raw_text)):
	    # select sequence of tokens
	    seq = raw_text[i-length:i+1]
	    # store
	    sequences.append(seq)
        
    #print('Total Sequences: %d' % len(sequences))
    #print("Sequences are : ",sequences)
    return sequences

# save tokens to file, one dialog per line


def save_doc(lines, filename):
	data = '\n'.join(lines)
	file = open(filename, 'w')
	file.write(data)
	file.close()

# save sequences to file

def main():
    raw_text = load_doc('rhyme.txt')
    print("raw_text is : ",raw_text)
    print("*****************************************")
    tokens_seq = getTokens(raw_text)
    print("Tokens are :",tokens_seq)
    _seqs = createSeq(tokens_seq)
    #out_filename = 'char_sequences.txt'
    #save_doc(_seqs, out_filename)
    
    

if __name__ == "__main__":
    main()
