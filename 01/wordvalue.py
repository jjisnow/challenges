from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
        words = f.read().split('\n')
    words = list(filter(lambda x: x != '', words))
    # another approach is to use words = [word.strip() for word in words]
    return words


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for letter in word:
        if letter.upper() in LETTER_SCORES:
            score += LETTER_SCORES[letter.upper()]
    # using the dict get method also simplifies things a bit
    # score = sum(LETTER_SCORES.get(letter.upper(),0) for letter in word)

    return score


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words()
    values = {}
    for word in words:
        values[word] = calc_word_value(word)
    return max(values, key=values.get)
    # return max(words or load_words(), key=calc_word_value)


if __name__ == "__main__":
    pass  # run unittests to validate
