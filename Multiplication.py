def make_multiplication_table(num):
    results = []
    for i in range(1, num + 1):
        row = []
        for j in range(1, i + 1):
            print(f"{i} x {j} = {i * j}")
            row.append(i * j)
        results.append(row)
        print('--------------')
    return results


num = input("Enter a number: ")
while not num.isdigit():
    num = input("Enter a valid number: ")
num = int(num)

results = make_multiplication_table(num)
