from bigram_list import bigram_list
from token_list import token_list

from collections import Counter

bigram_count = Counter(bigram_list)
word_count = Counter(token_list)

print(bigram_count)
print(word_count)