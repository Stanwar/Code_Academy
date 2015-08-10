def anti_vowel(text):
    result = ""
    for i in text:
        if i in ('aeiouAEIOU'):
            result = result
        else:
            result = result + i
    return result

anti_vowel('Hey You!')