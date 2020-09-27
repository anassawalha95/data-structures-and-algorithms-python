import re

def repated_word(text):
    words = set()
    words_list = re.findall(r'[A-Za-z]+', text.lower())

    for word in words_list:
        if word in words:
            return word
        words.add(word)
    return None


if __name__ == "__main__":
    text = 'I want to go, like he want'
    print(repated_word(text))