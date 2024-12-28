from nltk.stem import PorterStemmer


stemmer = PorterStemmer()


words = ["running", "jumps", "easily", "fairly", "played", "happily", "dogs"]


for word in words:
    stemmed_word = stemmer.stem(word)
    print(f"Original: {word}, Stemmed: {stemmed_word}")
