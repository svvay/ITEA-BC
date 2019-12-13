# Create program that get Text from file, find 5 most popular words and write result to file.

# Done

from collections import Counter


# my_file = 'file_txt/text.txt'

def popular(my_file):
    text = open(my_file)
    words = text.read().lower().split()
    text.close()

    for word in words:
        counter = Counter(words)
        most_popular = counter.most_common(5)
        pop = open('file_txt/mostpopular.txt', 'w')
        pop.write(str(most_popular))
        pop.close()
    return most_popular

# print(popular(my_file))
