def count_letter_input(input: str, letter: str) -> int:
    if not input:
        return 0
    if input[0] == letter:
        return 1 + count_letter_input(input[1:], letter)
    else:
        return count_letter_input(input[1:], letter)


print(count_letter_input('aabbccddsasfjccjsc', 'c'))

