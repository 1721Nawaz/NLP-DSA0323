import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet


nltk.download('wordnet')
nltk.download('omw-1.4')


def get_wordnet_pos(word):
    """Map POS tag to format used by WordNetLemmatizer."""
    from nltk.corpus.reader.wordnet import ADJ, NOUN, ADV, VERB
    
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {
        'J': ADJ,
        'N': NOUN,
        'V': VERB,
        'R': ADV
    }
    return tag_dict.get(tag, NOUN)


lemmatizer = WordNetLemmatizer()

words = ["running", "ran", "better", "cats", "swimming"]

for word in words:
    pos = get_wordnet_pos(word)
    lemma = lemmatizer.lemmatize(word, pos)
    print(f"Original: {word}, POS: {pos}, Lemmatized: {lemma}")
