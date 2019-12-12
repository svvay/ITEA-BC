'''
2. Create program that get [Text](https://www.python.org/dev/peps/pep-0008/#code-lay-out)
from file, find 5 most popular words and write result to file.'''
import re


def popular_5_words(file_path):
    words_frequency = {}
    with open(f"{file_path}.txt", "r") as file_popular_words:
        text_from_file = file_popular_words.read().lower()
        list_words = re.findall(r'\b[a-z]{1,15}\b', text_from_file)

        for word in list_words:
            count = words_frequency.get(word, 0)
            words_frequency[word] = count + 1

        sorted_dict_most_freq_words = sorted(words_frequency.items(), key=lambda x: x[1], reverse=True)

    with open("../Text_Files/HW_02_result.txt", "w") as result_file:
        result_file.write(f"Here are 5 most popular words:\n")
        iter = 0

        for meanings_tuple in sorted_dict_most_freq_words:
            if iter == 5:
                break
            result_file.write(f"{meanings_tuple[0]} - {meanings_tuple[1]} times\n")
            iter += 1
        print("all done!")

popular_5_words("../Text_Files/HW_02_5Popular_words")
