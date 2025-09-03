
from frequency_table import bigram_count,word_count


bigram_probabilistic_model_table = {}

for bigram,count in bigram_count.items():

    first_word,second_word = bigram

    # the probability formula
    probability = count / word_count[first_word]

    # Structure the model dictionary

    if first_word not in bigram_probabilistic_model_table:
        bigram_probabilistic_model_table[first_word] = {}
    
    bigram_probabilistic_model_table[first_word][second_word] = probability

print(bigram_probabilistic_model_table)