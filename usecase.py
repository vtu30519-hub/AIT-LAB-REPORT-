import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# Download the needed data (only the first time)
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# lil helper to map POS tags
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

lemmatizer = WordNetLemmatizer()

text = "The striped bats are hanging on their feet for best"
tokens = nltk.word_tokenize(text)
pos_tags = nltk.pos_tag(tokens)

lemmatized = [lemmatizer.lemmatize(word, get_wordnet_pos(pos)) for word, pos in pos_tags]

print("Original:", tokens)
print("Lemmatized:", lemmatized)
