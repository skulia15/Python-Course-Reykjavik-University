def reverse_words(words):
    ans = ""
    split = words.split()
    split.reverse()
    return " ".join(split)