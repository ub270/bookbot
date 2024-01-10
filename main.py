def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_word_count(text)
    print(words)
    print (get_letter_count(text))


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    count = len(text.split(" "))
    return count

def get_letter_count(text):
    letter_counts = {}
    for letter in text:
        lowered = letter.lower()
        if lowered in letter_counts:
            letter_counts[lowered] += 1
        else:
            letter_counts[lowered] = 1
    return letter_counts


main()
