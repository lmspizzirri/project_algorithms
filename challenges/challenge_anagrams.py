def is_anagram(first_string, second_string):
    first_string = first_string.lower()
    second_string = second_string.lower()

    first_string_sorted = ''.join(sorted(first_string))
    second_string_sorted = ''.join(sorted(second_string))

    anagram_check = first_string_sorted == second_string_sorted

    return first_string_sorted, second_string_sorted, anagram_check
