def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        splitter = file_contents.split()
        num_words = len(splitter)
        return num_words
     
def main():
    word_count = num_words("./books/frankenstein.txt")
    print(f"{word_count} words found in the document")
    

main()