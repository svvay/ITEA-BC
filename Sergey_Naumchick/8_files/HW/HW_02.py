'''
2. Create program that get [Text](https://www.python.org/dev/peps/pep-0008/#code-lay-out)
from file, find 5 most popular words and write result to file.'''
import re

list_w = {}
words_frequency = {}
with open("../Text_Files/HW_02_5Popular_words.txt", "r") as file_popular_words:
    text_from_file = file_popular_words.read().lower()
    list_words = re.findall(r'\b[a-z]{1,15}\b', text_from_file)

    for word in list_words:
        count = words_frequency.get(word, 0)
        words_frequency[word] = count + 1

# sorted(words_frequency.values())
frequency_dict = words_frequency.keys()
print(words_frequency)
print(frequency_dict)

with open("../Text_Files/HW_02_result.txt", "w") as result_file:
    i = 0
    for words in frequency_dict:
        if i > 4:
            break
        if words_frequency[words] >= 3:
            result_file.write(f'"{words}" - {words_frequency[words]}\n')
            i += 1
