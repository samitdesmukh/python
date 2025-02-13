import os
def count_vowels(line):
    vowels="AEIOUaeiou"
    return sum(1 for char in line if char in vowels)
def copy_file_with_vowel_count(sourcefile, destfile):
    if not os.path.exists(sourcefile):
        print("Error: source file not found!")
        return
    with open(sourcefile,'r') as src:
        lines= src.readlines()
    if not lines:
        print("Error: source file is blank!")
        return
    with open(destfile,'w') as dest:
        for line in lines:
            vowels_count= count_vowels(line)
            dest.write(f"{line.strip()} ({vowels_count} vowels) \n")
    print(f"content copied successfully to {destfile} with vowels count")
sourcefile = input("Enter the source file name:")
destfile = input("Enter thr destination file name:")
copy_file_with_vowel_count(sourcefile,destfile)