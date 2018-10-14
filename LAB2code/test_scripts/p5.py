from math import sqrt

def check_valid(rectangle):
	return (rectangle[0]>0 and rectangle[1]>0)

def is_square(rectangle):
	return (rectangle[0]==rectangle[1])

def diagonal_len(rectangle):
	return sqrt(rectangle[0]**2+rectangle[1]**2)

def height(rectangle):
	return rectangle[0]

def width(rectangle):
	return rectangle[1]

def area(rectangle):
	return rectangle[0]*rectangle[1]

def perimeter(rectangle):
	return (rectangle[0]*2+rectangle[1]*2)
	
