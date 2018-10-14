def unique(list):
	unique_list = []
	for item in list:
		if item in unique_list:
			continue
		else:
			unique_list.append(item)
	return unique_list



