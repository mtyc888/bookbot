def count_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        for i in range(1,len(words)+1):
            print(i)


def count_specific_char():
    dictionary = {}
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        lowered_file_contents = file_contents.lower()
        #we will use a dictionary to count how many times each specific char is in the text files
        #dictionary = { 'a': x-times(int) }
        
        for char in lowered_file_contents:
            if char not in dictionary:
                dictionary[char] = 1
            else:
                dictionary[char] += 1
    print("--- Begin report of books/frankenstein.txt ---")
    total = sum(dictionary.values())
    print("\n")
    print(f"{total} words found in the document")
    for char in dictionary:
        if char.isalpha():
            count = dictionary[char]
            print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

count_specific_char()

