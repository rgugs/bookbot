def main():
    book = r'books/frankenstein.txt'
    
    text = get_book_path(book)
    count = count_words(text)
    
    print(text)
    print(count)
    
def get_book_path(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)
    
    return counter

main()
