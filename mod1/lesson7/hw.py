def count_vowels(s):
    count = 0
    for i in s:
        if i in "aeiouAEIOU":
            count += 1
    return count


print(count_vowels("Hello World"))