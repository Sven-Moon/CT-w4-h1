# Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string.
# Should output:
# {'a': 5,
# 'abstract': 1,
# 'an': 3,
# 'array': 2, ... etc...
import re
from collections import Counter
a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'


def countDistinctWords(text):    
    return dict(Counter(re.sub('[^\w\s]+', '', text).lower().split(" ")))
    
# print(countDistinctWords(a_text))

def cdw(text):
    text = re.sub('[^\w\s]+', '', text).lower().split(" ")
    words = {}
    for w in text:
        if w not in words:
            words[w] = 0
        words[w] += 1
    return words
        
print(cdw(a_text))