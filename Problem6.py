"""
Problem 6:

Write a program which reads from a text file (attached to email) and returns individual words in lowercase and stripped from digits and punctuation. It should return a list of words.
Problem 6.1

Make a function which takes as input the list of words, and returns a dict that has as a key the word and as value the number of occurrences.
Problem 6.2

Return the word with the most occurrences

"""
list=[]
with open ("/home/rachel/Documents/test.txt") as f:
  lines = f.readlines()
  for line in lines:
      words = line.split()
      for word in words:
	 a = "a!b@c#d$"
	 b = "!@#$"
	 	for i in range(0,len(b)):
		 a =a.replace(b[i],"")   			print a
	#print "%s" %(word)
	#list=word.strip ('0', '1', '[' , '"', '(')
	list = word
	print "%s" % (list)

"""

>>>
>>> a = "a!b@c#d$"
>>> b = "!@#$"
>>> for i in range(0,len(b)):
...  a =a.replace(b[i],"")
...
>>> print a
abcd
>>>
"""

