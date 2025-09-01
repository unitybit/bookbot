from stats import letter_count, word_count
import sys
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count(book)} total words")
    print("--------- Character Count -------")

    for letter in letter_count(book):
        if str(letter[0]).isalpha():
            print(f"{letter[0]}: {letter[1]}")
    
    print("============= END ===============")

main()