def is_anagram(first_string, second_string):
    first_string = first_string.replace(" ", "").lower()
    second_string = second_string.replace(" ", "").lower()

    if len(first_string) != len(second_string):
        return (sorted(first_string), sorted(second_string), False)

    if sorted(first_string) == sorted(second_string):
        return (sorted(first_string), sorted(second_string), True)
    else:
        return (sorted(first_string), sorted(second_string), False)
