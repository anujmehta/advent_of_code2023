def get_number(str):
    for char in str:
        if char.isdigit():
            first_digit = int(char)
            break

    for char in str[: :-1]:
        if char.isdigit():
            last_digit = int(char)
            break
    return first_digit * 10 + last_digit

sum = 0
with open("input.txt") as file:
    for line in file:
        sum += get_number(line.rstrip())

print("Sum: ", sum)
          