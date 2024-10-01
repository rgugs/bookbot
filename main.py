def main():
    book = r'books/frankenstein.txt'
    
    text = get_book_path(book)
    count = count_words(text)
    count_dict = count_characters(text)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document")
    print(count_dict)
    
def get_book_path(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(string):
    lowered = string.lower().split()
    count_dict = {}
    character_list = []
    for i in lowered:
        for c in i:
            if c in count_dict:
                count_dict[c] += 1
            else:
                count_dict[c] = 1

    return count_dict


main()
