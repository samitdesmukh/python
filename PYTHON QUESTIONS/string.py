s1 = "I Love ICE CREAM"
words_with_e=[word for word in s1.split() if 'e' in word.lower()]
print("words containing 'e': ",words_with_e)

lowercase_string = s1.lower()
print("Lowercase output:", lowercase_string)

reversed_string= s1[::-1]
print("Reversed string: ",reversed_string)

starts_with_i= s1.startswith("I")
print("Starts with 'I':",starts_with_i)

replaced_string= s1.replace("ICE CREAM", "HOCKEY")
print("Modified string:", replaced_string)