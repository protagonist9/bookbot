import sys
from stats import count_words
from stats import count_char
from stats import sort_final

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    count_words(get_book_text(sys.argv[1]))
    print("--------- Character Count -------")
    final_dictionary = count_char(get_book_text(sys.argv[1]))
    final_sorted_list = sort_final(final_dictionary)
    for item in final_sorted_list:
        char = item["char"]
        count = item["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main() 
   