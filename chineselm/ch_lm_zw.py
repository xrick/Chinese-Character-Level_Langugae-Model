
from numpy import array
from pickle import dump
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import re

# load doc into memory


def load_doc(filename):
	# open the file as read only
	file = open(filename, 'r')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text

def main():
    # load
    in_filename = 'engrawdata.txt'  # 'char_sequences.txt'
    raw_text = load_doc(in_filename)
    lines = raw_text.split('\n')

    # integer encode sequences of characters
    chars = sorted(list(set(raw_text)))
    mapping = dict((c, i) for i, c in enumerate(chars))
    sequences = list()
    for line in lines:
	    # integer encode line
	    encoded_seq = [mapping[char] for char in line]
	    # store
	    sequences.append(encoded_seq)

    # vocabulary size
    vocab_size = len(mapping)
    print('Vocabulary Size: %d' % vocab_size)

    # separate into input and output
    sequences = array(sequences)
    X, y = sequences[:, :-1], sequences[:, -1]
    #print("X is :",X)
    #sequences = [to_categorical(x, num_classes=vocab_size) for x in X]
    #X = array(sequences)
    #y = to_categorical(y, num_classes=vocab_size)
    #print("X is : ",X)
    '''
    # define model
    model = Sequential()
    model.add(LSTM(75, input_shape=(X.shape[1], X.shape[2])))
    model.add(Dense(vocab_size, activation='softmax'))
    print(model.summary())
    # compile model
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam', metrics=['accuracy'])
    # fit model
    model.fit(X, y, epochs=100, verbose=2)

    # save the model to file
    model.save('model.h5')
    # save the mapping
    dump(mapping, open('mapping.pkl', 'wb'))
    '''

def train_ch_main():
	# load
    in_filename = 'ch_char_sequences.txt'  # 'char_sequences.txt'
    raw_text = load_doc(in_filename)
    lines = raw_text.split('\n')
    #lines = removeEmptyLines(raw_text)

    # integer encode sequences of characters
    #chwordSet = splitCHWord(raw_text)
    chars = sorted(list(set(raw_text)))
    #print("chars are : ",chars)
    mapping = dict((c, i) for i, c in enumerate(chars))
    #print("The mapping are : ",mapping)

    sequences = list()
    for line in lines:
	    # integer encode line
	    encoded_seq = [mapping[char] for char in line]
	    # store
	    sequences.append(encoded_seq)

    # vocabulary size
    vocab_size = len(mapping)
    print('Vocabulary Size: %d' % vocab_size)

    # separate into input and output
    sequences = array(sequences)
    X, y = sequences[:, :-1], sequences[:, -1]
    sequences = [to_categorical(x, num_classes=vocab_size) for x in X]
    X = array(sequences)
    y = to_categorical(y, num_classes=vocab_size)

    # define model
    model = Sequential()
    model.add(LSTM(75, input_shape=(X.shape[1], X.shape[2])))
    model.add(Dense(vocab_size, activation='softmax'))
    print(model.summary())
    # compile model
    model.compile(loss='categorical_crossentropy',optimizer='adam', metrics=['accuracy'])
    # fit model
    model.fit(X, y, epochs=100, verbose=2)

    # save the model to file
    model.save('ch_model.h5')
    # save the mapping
    dump(mapping, open('mapping.pkl', 'wb'))
    
    

    


def splitCHWord(textdata):
    charWordSet = set()
    #charWordList = list()
    for line in textdata:
        filtered = filter(lambda x: not re.match(
            r'^\s*$', x), line)  # filter the empty line
        line_list = list(filtered)
        if len(line_list) != 0:
            for charWord in line_list:
                charWordSet.add(charWord)
                #charWordList.append(charWord)
    return charWordSet  # , charWordList

"""
The codes below are for test
"""



"""
def removeEmptyLines(rawtext):
    lines = rawtext.split('\n')
    lines = filter(lambda x: x.strip(), lines)
    return lines
"""

"""
paprameter : single line
return : 
true : if line is empty
false : if line is not empty 
"""
def isLineEmpty(line):
    return len(line.strip()) == 0

def removeEmptyLines(raw_lines):
    processedLines = list()
    for line in raw_lines:
        if not isLineEmpty(line):
            processedLines.append(line)
    return processedLines



if __name__ == "__main__":
	#main()
    train_ch_main()
    
    #txtdata = load_doc("rawdata.txt")
    #lines = txtdata.split('\n')
    #t = list()
    
    #for line in lines:
     #   if not isLineEmpty(line):
      #      t.append(line)
    
    #lines = filter(lambda x: x.strip(), lines)
    
    #t = removeEmptyLines(lines)
    #print("no empty lines are:",t)
    #print("Total lines are : ", len(t))
    
