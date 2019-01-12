data = open('data.txt', 'r+')
enddata = []
keywords = 'ihopeyouhaveaveryhappythanksgiving'

for word in data:
	letterscorrect = 0
	keywordcopy = keywords

	word = word[:-1:]
	for letter in word:
		if letter in keywordcopy:
			keywordcopy = keywordcopy.replace(letter, '',1)
			letterscorrect += 1
		if letterscorrect == len(word):
			print(keywordcopy)
			enddata.append(word)

print(sorted(enddata, key=str.lower))
#print(enddata)