#WAP to accept a sentence from user and replace the not bad construct, if found, with good construct. e.g. (australia played not bad but they lost -> australia played good but they lost)

inputStmt = input('Enter an input string : ')
notIndex = inputStmt.find('not')
result = ""
if notIndex != -1:
	badIndex = inputStmt.find('bad')
	if badIndex != -1 and badIndex > notIndex:
		result = inputStmt[:notIndex]
		result += 'good'
		result += inputStmt[badIndex+3:]

print (result)