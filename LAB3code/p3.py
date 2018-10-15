import pickle

def load_data(file):
	try:
		file_object = open(file,'rb')
		departments = pickle.load(file_object)
		file_object.close()
	except Exception as e:
		departments={}
		print(e)
		print("Sorry we cannot open %s"%file)
	return departments
def query(prof_name):
	departments=load_data('dept-prof.pydata')
	listOfDept = []
	for key,value in departments.items():
		if prof_name in value:
			listOfDept.append(key)

	return listOfDept

def update():
	departments=load_data('dept-prof.pydata')
	del departments['Artificial Intelligence']
	departments['Space Engineering']=['Musk','Andy','Jane']
	try:
		file_object = open('dept-prof-updated.pydata','wb')
		pickle.dump(departments,file_object)
		file_object.close()
	except Exception as e:
		print(e)
		print("Failed to store the updated dept-prof data")

def get_depts_size():
	try:
		file_object = open('dept-prof-updated.pydata','rb')
		departments = pickle.load(file_object)
		file_object.close()
		return departments
	except Exception as e:
		print(e)
		print("Sorry we cannot open dept-prof-updated.pydata")

print(load_data('dept-prof.pydata'),'\n')
print(query('Andrew'),'\n')
update()
print(get_depts_size())