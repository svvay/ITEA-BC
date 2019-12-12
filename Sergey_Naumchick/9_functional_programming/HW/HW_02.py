'''2. In English, the present participle is formed by adding the suffix -ing
    to the infinite form: go -> going. A simple set of heuristic rules can be
    given as follows:

    If the verb ends in e, drop the e and add ing (if not exception: be, see,
      flee, knee, etc.)
    If the verb ends in ie, change ie to y and add ing
    For words consisting of consonant-vowel-consonant, double the final letter
    before adding ing
    By default just add ing
    Your task in this exercise is to define a function make_ing_form() which
    given a verb in infinitive form returns its present participle form. Test
    your function with words such as lie, see, move and hug. However, you must
    not expect such simple rules to work for all cases.'''


def make_ing_form(word):
    volved = ["a", "e", "i", "o", "u", "y"]
    exceptions = ["be", "see", "flee", "knee"]
    if word in exceptions:
        print(f"word {word} is an exception!")
        return None

    elif word.endswith("ie"):
        new_word = f"{word[0:len(word) - 2]}ying"
        print(f"{word} - {new_word}")
        return new_word

    elif word.endswith("e"):
        new_word = f"{word[0:len(word) - 1]}ing"
        print(f"{word} - {new_word}")
        return new_word

    elif word[-1] not in volved and word[len(word) - 2:len(word) - 3:-1] in volved and word[len(word) - 3:len(word) - 4:-1] not in volved:
        new_word = f"{word}{word[-1]}ing"
        print(f"{word} - {new_word}")
        return new_word
    else:
        new_word = f"{word}ing"
        print(f"{word} - {new_word}")
        return new_word


make_ing_form("lie")
