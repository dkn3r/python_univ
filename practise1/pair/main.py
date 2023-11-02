from statistics import mean
my_string = input("Enter string: ")

# print("Analys text " + my_string)
# print("Analys text {}".format(my_string))
# print("Analys text ", my_string)
print(f"Analys text\n {my_string}")


words = my_string.split(" ")
sentences = my_string.split(". ")
count_words = len(words)
count_sentences = len(sentences)

word_lengths = []
for word in words:
    count_let_word = len(word)
    word_lengths.append(count_let_word)

if count_sentences > 0:
    average_words = count_words / count_sentences
else:
    average_words=0

average_word_length = mean(word_lengths)

print(f"Count words in a sentence: {count_words}")
print(f"Count sentences: {count_sentences}")
print(f"Average len words: {average_word_length}")