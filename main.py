def get_file_contents(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def read_book(path_to_file):
    file_contents = get_file_contents(path_to_file)
    print(file_contents)
    return

def count_words(file_content):
    words = file_content.split()
    word_count = len(words)
    return word_count

def count_characters(file_contents):
    characters = {}
    for i in range(0,len(file_contents)):
        character = file_contents[i].lower()
        #check if character is in the dictionary
        if characters.get(character) == None:
            characters[character] = 0
            
        characters[character] += 1

    return characters

def sort_on(Dictionary, Value):
    return Dictionary[Value]

def generate_report(path_to_file):
    file_contents = get_file_contents(path_to_file)
    word_count = count_words(file_contents)
    characters = count_characters(file_contents)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")

    # Sort characters by count in descending order
    sorted_characters = sorted(characters.items(), key=lambda item: item[1], reverse=True)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for character, count in sorted_characters:
        if  character.isalpha() == True:
            print(f"The '{character}' character was found {count} times")
    return

def main():
    generate_report(r".\Books\Frankenstein.txt")
    return

main()