def main():
    book = r'books/frankenstein.txt'
    
    # Read text into memory
    text = get_book_path(book)

    # Count words
    count = count_words(text)

    # Could combine these into single function to return a sorted dictionary 
    count_dict = count_characters(text)
    sorted_dict = sort_dict(count_dict)

    # Final output
    generate_report(book, count, sorted_dict)
    
def get_book_path(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(string):
    lowered = string.lower().split()
    count_dict = {}
    for i in lowered:
        for c in i:
            if c.isalpha():
                if c in count_dict:
                    count_dict[c] += 1
                else:
                    count_dict[c] = 1
    
    return count_dict

def sort_dict(in_dict):
    sorted_dict = dict(sorted(in_dict.items(), key=lambda item: item[1], reverse=True))

    return sorted_dict

def generate_report(book, count, sorted_dict):

    print(f"--- Begin report of {book} ---")
    print(f"{count} words found in the document")
    print("")

    for k, v in sorted_dict.items():
        print(f"The '{k}' character was found {v} times")
    print("--- End report ---")

main()