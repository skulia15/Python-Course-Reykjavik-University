#def countdown(file, letters)
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
ans = []
response = urlopen('https://mooshak.ru.is/~python/all_words_no_short.txt')
lines = response.read().decode('utf8').splitlines()
letters = 'pythonxyz'
characters = list(letters)
print(characters)
for word in lines:
    if all(True if characters.count(char) >= word.count(char) else False for char in word):
        ans.append(word)
print(ans)