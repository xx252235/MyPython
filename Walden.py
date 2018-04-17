import string
path = 'C://Users/xu01.xin/Downloads/Walden.txt'
with open(path,'r',encoding='UTF-8') as text:
    words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    words_index = set(words)
    counts_dict = {index: words.count(index) for index in words_index}
    for word in sorted(counts_dict, key=lambda x: counts_dict[x], reverse=True):
        print('{} -- {} times'.format(word, counts_dict[word]))