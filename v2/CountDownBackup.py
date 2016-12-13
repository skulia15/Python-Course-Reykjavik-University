def countdown(file, letters):
    with open(file) as fileData:
        wordList = fileData.readlines()
    ans = []
    characters = list(letters)
    for word in wordList:
        word = word.strip()
        if all(True if word.count(char) <= characters.count(char) else False for char in word):
            ans.append(word.strip())
    return ans