def count_vowels():
    vowels = "aeiouAEIOU"
    string = input("Enter a string: ")
    vowels_count = 0
    for char in string:
        if char in vowels:
            vowels_count += 1
    return vowels_count


print("Number of vowels:", count_vowels())
