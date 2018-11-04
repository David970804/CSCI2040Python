class Node ( object ):
	def __init__ (self , v, n):
		self.value = v
		self.next = n
class LinkedList ( object ):
	def __init__ ( self ):
		self.firstLink = None
	def add (self , newElement ):
		self.firstLink = Node ( newElement , self.firstLink )
	def test (self , testValue ):
		currentLink = self.firstLink
		while currentLink != None:
			if currentLink.value == testValue:
				return True
			currentLink = currentLink.next
		return False 
	def remove (self , testValue ):
		if not self.test(testValue):
			return False
		else:
			currentLink = self.firstLink
			previousLink = None
			while currentLink.value != testValue:
				previousLink = currentLink
				currentLink = currentLink.next
			if previousLink == None:
				self.firstLink = currentLink.next
			else:
				previousLink.next = currentLink.next
			del currentLink
			return True
	def len( self ): # return size of linked list
		length = 0
		currentLink = self.firstLink
		while currentLink != None:
			length += 1
			currentLink = currentLink.next
		return length

	def reverse ( self ): # return reverse linked list
		currentLink = self.firstLink
		previousLink = None
		postLink = self.firstLink
		while currentLink != None:
			postLink = currentLink.next
			currentLink.next = previousLink
			previousLink = currentLink
			currentLink=postLink
		self.firstLink = previousLink
	def Lprint ( self ):
		print('Current linked list: ',end="")
		currentLink = self.firstLink
		while currentLink != None:
			print("%d-->"%currentLink.value,end="")
			currentLink = currentLink.next
		print('none') 

