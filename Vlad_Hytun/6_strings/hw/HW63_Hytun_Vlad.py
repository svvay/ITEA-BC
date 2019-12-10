# 3. Write a function filter_long_words() that takes a list
# of words and an integer n and returns the list of words that
# are longer than n.


def filter_long_word(list_of_word, n_count):
    for word in list_of_word.split(','):
        if len(word) > int(n_count):
            print(word)


my_list_of_word = input('Enter list of word use separator , : ')
my_n_count = input('Enter number please: ')
filter_long_word(my_list_of_word, my_n_count)