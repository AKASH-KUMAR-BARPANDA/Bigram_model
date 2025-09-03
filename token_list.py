from dataprint import data
from punctuation_removal import remove_punctuation

final_data = data.lower()
final_data = remove_punctuation(final_data)
token_list = list(final_data.split())
print(token_list)