def input_preprocess():
	with open("input_text.txt", "r") as input_file:
		return "".join(input_file.readlines())

def compress():
	'''
	Compresses "input_text.txt" and generates "compressed_text.txt".
	Also returns compressed pairs (as a list of 2-length tuples) to be used in decompression.
	'''
	input_text, compressed_text, compressed_pairs, codebook, current_code = input_preprocess(), "", [], {}, 1

	i = 0
	while i < len(input_text):
		j = i+1
		substring = input_text[i:j]
		while substring in codebook and j < len(input_text):
			j += 1
			substring = input_text[i:j]

		pair = ("0",substring) if len(substring) == 1 else (str(codebook[substring[:-1]]),substring[-1])
		compressed_text += pair[0] + pair[1]
		compressed_pairs.append(pair)

		codebook[substring] = current_code
		current_code += 1
		i = j

	with open("compressed_text.txt", "w") as compressed_file:
		compressed_file.write(compressed_text)

	return compressed_pairs


def decompress(compressed_pairs):
	'''Decompresses "compressed_text.txt" and generates "back_to_original.txt".'''
	original_text, codebook, current_code = "", {}, 1
	
	for code, letter in compressed_pairs:
		original_substring = codebook.get(int(code),"") + letter
		original_text += original_substring
		codebook[current_code] = original_substring
		current_code += 1
	
	with open("back_to_original.txt", "w") as f:
		f.write(original_text)

pairs = compress()
decompress(pairs)
