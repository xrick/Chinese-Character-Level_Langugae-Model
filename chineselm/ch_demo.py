from pickle import load
from keras.models import load_model
from keras.utils import to_categorical
from keras.preprocessing.sequence import pad_sequences

# generate a sequence of characters with a language model

# load the model
model = load_model('ch_model.h5')
# load the mapping
mapping = load(open('mapping.pkl', 'rb'))

def generate_seq(model, mapping, seq_length, seed_text, n_chars):
	in_text = seed_text
	# generate a fixed number of characters
	for _ in range(n_chars):
		# encode the characters as integers
		encoded = [mapping[char] for char in in_text]
		# truncate sequences to a fixed length
		encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')
		# one hot encode
		encoded = to_categorical(encoded, num_classes=len(mapping))
		encoded = encoded.reshape(1, encoded.shape[0], encoded.shape[1])
		# predict character
		yhat = model.predict_classes(encoded, verbose=0)
		# reverse map integer to character
		out_char = ''
		for char, index in mapping.items():
			if index == yhat:
				out_char = char
				break
		# append to input
		in_text += char
	return in_text

def test_generate_seq(model, mapping, seq_len, seed_text, n_chars):
	in_text = seed_text
	for _ in range(n_chars):
		for char in in_text:
			print("current processing char is : {}".format(char))
			encoded_ch = [mapping[char] for char in in_text]
			print("current get encoded_ch is : {}".format(encoded_ch))
		
		


"""
print(generate_seq(model, mapping, 14, '台灣 長年 意識', 20))

print(generate_seq(model, mapping, 18, '政黨政治 手段 失能', 20))

print(generate_seq(model, mapping, 16, '耐不住 口號 美麗', 20))
"""
if __name__ == "__main__":
	test_generate_seq(model, mapping, 14, '台灣 長年 意識', 20)
