#this gets the text from main, splits it into a list,
#and returns the length.
def get_num_words(text):
    splitter = text.split()
    return len(splitter)

#this gets the text from main, sets up an empty dict, and runs a loop through every char. 
#It lowers each char. Then checks if the char is already in the dict.
#If the char is alread in the dict, it increases the count. If it isn't in the dict it 
#adds it. Then it returns an unsorted dict.        
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
 
#sets our key to sort with 
def sort_on(d):
    return d["num"]
 
#this sets and empty list and then loops through the dict made in get_chars_dict 
#(pulled from main.) It appends each key value pair to the list as an individual dictionary.
#Then it sorts the list and returns it. 
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list