# NLP codes

#Tokenisation

import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt")   

text = "hello hi how are you charan sathwik?"
tokens = word_tokenize(text)

print(tokens)

# stop words

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "this is a sample code written by geethaa"

words = word_tokenize(text)
stop_words = set(stopwords.words("english"))

filtered_words = [word for word in words if word.lower() not in stop_words]

print("Original:", text)
print("Filtered:", " ".join(filtered_words))


# stemming

from nltk.stem import PoeterStemmer
stemmer=PortStemmer()
words=["running","runner","easily","fairly"]
stemmed_word=[stemmer.stem(word) for word in words]
print("stemmed words:",stemmed_words)


