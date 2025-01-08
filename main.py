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
        #dictionary = { 'a'(key): x-times(value) }
        for char in lowered_file_contents:
            #if char is not in dictionary, means it is unique, so we add it in and initialize the value to 1
            if char not in dictionary:
                dictionary[char] = 1
            else:
                #if it reaches here means it exists, so we append the count
                dictionary[char] += 1
    print("--- Begin report of books/frankenstein.txt ---")
    total = sum(dictionary.values())
    print("\n")
    print(f"{total} words found in the document")
    for char in dictionary:
        #isalpha() makes sure that we only print characters that are within the alphabets
        if char.isalpha():
            #get the value from key-value dictionary
            count = dictionary[char]
            print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

count_specific_char()

