def count_alphabet(test_string):
	char_list = [char for char in test_string if char.isalpha()]
	return len(char_list)

def vowel_capitalization(test_string):
	vowel = ('a','e','i','o','u')
	capitalized=[]
	for char in test_string:
		if char in vowel:
			capitalized.append(char.capitalize())
		else:
			capitalized.append(char)
	return "".join(capitalized)

def concat(test_string,new_string):
	return test_string+new_string

def search(test_string,sub):
	return test_string.find(sub)