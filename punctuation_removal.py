import string

def remove_punctuation(text):
    # Create the translation table to remove punctuation
    translator = str.maketrans('','',string.punctuation)

     # Apply the translation to the text
    clean_text = text.translate(translator)
    return clean_text

