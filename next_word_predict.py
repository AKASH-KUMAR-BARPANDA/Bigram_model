import random
def predict_next_word(model_table,current_word):

    if current_word in model_table:
        # Get the inner dictionary of possible next words and their probabilities
        possible_words = model_table[current_word]

        # Extract the words and their probabilities into separate lists
        words = list(possible_words.keys())
        probabilities = list(possible_words.values())

        # random.choices 
        return random.choices(words,weights=probabilities,k=1 )[0] # type: ignore
    else:
        return None
    