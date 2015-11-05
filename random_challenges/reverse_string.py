def reverseString(string):
	result = ''
	tmp = ''
	letters = []
	for letter in string:
		letters.append(letter)
	j = len(letters)-1
	for i in range(0,len(letters)/2):
		tmp = letters[i] 
		letters[i] = letters[j]
		letters[j] = tmp
		j -= 1
	for letter in letters:
		result += letter
	return result

def main():
	string = "Take chances, make mistakes. That's how you grow. Pain nourishes your courage. You have to fail in order to practice being brave."
	print string
	reverse = reverseString(string)
	print reverse

if __name__=="__main__":
	main()

