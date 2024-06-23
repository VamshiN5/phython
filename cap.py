def capitalize_first_last(word):
    if len(word) < 2:
        return word.upper()
    else:
        return word[0].upper() + word[1:-1].lower() + word[-1].upper()

# Example usage:
word = input()
result = capitalize_first_last(word)
print(result)
