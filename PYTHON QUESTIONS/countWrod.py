input_string = input("Enter a string:")
word_to_count = input("Enter word to count:")
word_count = input_string.split().count(word_to_count)
print(f"count of the word '{word_to_count}' is: {word_count}")

if len(input_string)>=2:
    modified_string = input_string[-1]+ input_string[1:-1] + input_string[0]
else:
    modified_string = input_string
print(f"Modified string :{modified_string}")