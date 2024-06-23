def divide_word_without_repeats(word, n):
    word_len = len(word)
    part_len = word_len // n
    remainder = word_len % n

    parts = []
    used_letters = set()
    for i in range(n):
        part = ""
        while len(part) < part_len + (1 if i < remainder else 0):
            for char in word:
                if char not in used_letters:
                    part += char
                    used_letters.add(char)
                    break
        parts.append(part)

    return parts

# Test the function
word = input()
n = 3
parts = divide_word_without_repeats(word, n)
print("Divided into", n, "parts without repeating letters:")
for i, part in enumerate(parts, 1):
    print(f"Part {i}: {part}")
