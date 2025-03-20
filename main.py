import sys
from stats import count_words
from stats import count_symbols
from stats import sort_on
from stats import report

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    file_path = sys.argv[1]
    #file_path = os.path.expanduser("~/code/github.com/GuillaumeDeshors/bookbot/books/frankenstein.txt")
    text = get_book_text(file_path)
    dictionnary = count_symbols(text)
    pairs = report(dictionnary)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f'Found {count_words(text)} total words')
    print("--------- Character Count -------")
    for pair in pairs:
        value = list(pair.values())
        if not value[0].isalpha():
            continue
        print(f'{value[0]}: {value[1]}')
    print("============= END ===============")
    

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

main()
