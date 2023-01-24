text = input()
# print(len(text))
# print(text[2]) # string index starts at 0
# for letter in text
#     print(letter)
# for letter in range(len(text)): # in range (0,len(text))
#     print (text[letter])

# За извличане на индекс на даден символ от низа и неговото съдържание

for index, character in enumerate(text):
    print(f"Index ->{index} character -> {character}")
