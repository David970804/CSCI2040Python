def letter_count(string):
	neat_string = string.replace(" ","").lower()
	result=[]
	for char in neat_string:
		if char.isalpha():
			count = neat_string.count(char)
			char_tuple = (char,count)
			if char_tuple not in result:
				result.append(char_tuple)
			else:
				continue
		else:
			continue
	return sorted(result)

