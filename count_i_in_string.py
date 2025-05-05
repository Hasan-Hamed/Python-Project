def count_i_in_string(string):
    count = 0
    for char in string:
        if char == 'i':
            count += 1
    print(f"Total 'i' characters: {count}")

string = input("Input string: ")
count_i_in_string(string)
