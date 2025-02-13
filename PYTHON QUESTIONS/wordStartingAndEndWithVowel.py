def starts_and_ends_with_vowel(sentence):
    vowels="aeiouAEIOU"
    words = sentence.split()

    for word in words:
        if len(word)>1 and word[0] in vowels and word[-1] in vowels:
            return True
    return False
user_input = input("Enter a sentence:")
result = starts_and_ends_with_vowel(user_input)

print("Result: ",result)