from next_word_predict import predict_next_word
from probabilistic_model_table import bigram_probabilistic_model_table

def sentence_generator(prompt,word_number = 50):
    sentence = [prompt]
    temp = prompt
    for i in range(word_number):
    
        next_word = predict_next_word(bigram_probabilistic_model_table,temp)
    
        if next_word is None:
            continue
        else:
            sentence.append(next_word)

        temp = next_word
    return " ".join(sentence)

prompt = input("enter the word :- ")
sentence_generator(prompt=prompt)