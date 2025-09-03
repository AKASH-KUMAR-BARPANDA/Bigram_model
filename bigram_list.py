from token_list import token_list

bigram_list = []

for i in range(len(token_list)-1):
    bigram = (token_list[i],token_list[i+1])
    bigram_list.append(bigram)

print(bigram_list)