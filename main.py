from stats import get_num_words, get_chars_dict, chars_dict_to_sorted_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

     
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
    #get text from file
    text = get_book_text(file_path)
    #get word count from text file using func in stats
    word_count = get_num_words(text)
    #gets individual chars from dict using func in stats
    char_dict = get_chars_dict(text)
    #gets sorted list of dicts using func in stats
    char_list = chars_dict_to_sorted_list(char_dict)
    
    #print document as requested in lesson
    print(f"""============ BOOKBOT ============
Analyzing book found at {file_path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")
    
    #check each key in char_list to ensure it is a letter and not symbol or number.
    #then prints each pair.
    for char_data in char_list:
        if char_data["char"].isalpha():
            print(f" {char_data['char']}: {char_data['num']}")

    print("============= END ===============")

main()