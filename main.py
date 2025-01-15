def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    file_contents = file_contents.lower()
    words = file_contents.split()
    print(len(words))

    print(count_characters(file_contents))

def sort_on(char):
    return char[1]

def count_characters(text):
    char_count= {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    sorted_char_count = sorted(char_count.items() ,reverse=True, key=sort_on)        
    
    return sorted_char_count        

main()