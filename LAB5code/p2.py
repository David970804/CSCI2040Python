from functools import reduce
def word_count(x,n,str):
	nlarge = list(filter(lambda y: len(y)>n, x))
	occurance = list(map(lambda y: y.count(str), nlarge))
	totalOccurance = reduce(lambda a,b: a+b, occurance)
	return totalOccurance

