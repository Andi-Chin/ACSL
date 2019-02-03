import re
def deleteWord(word, string):
	foundWord = re.findall(word, string)
	if foundWord:
		foundWord = foundWord[0]
	else:
		return string, ''
	index1 = string.index(foundWord)
	lastIndex = index1 + len(word)
	string = string[:index1] + string[lastIndex:]
	return string, foundWord

def diff(s1, s2):
	s1 = s1.split(' ')
	commonString = ''
	for i in s1:
		s2, foundWord = deleteWord(i, s2)
		commonString += foundWord + ' '
	return commonString

def second_algorithm(commonString1, commonString2):
	commonString1 = commonString1.replace(" ", '')
	commonString2 = commonString2.replace(" ", '')

	result = ''
	
	for char in commonString1:
		if char in commonString2:
			result += char

			commonString2 = commonString2[commonString2.index(char)+1:]
	return result
	
s1 = input("string 1 please:\n")
s2 = input("string 2 please:\n")
commonString1 = diff(s1, s2)
commonString2 = diff(s2, s1)
result = second_algorithm(commonString1, commonString2)

if result == '':
	print(None)
else:
	print(result)