from django.http import JsonResponse, HttpResponse
from django.shortcuts import render


def work_with_string(request):
    input_string = request.GET.get('input_string', 'guest')
    upper_case = input_string.upper()

    lower_case = input_string.lower()

    replace_spaces = input_string.replace(' ', '_')

    cleaned_chars = []
    for char in input_string:
        if char.isalnum():
            cleaned_chars.append(char)
    cleaned_string = ''.join(cleaned_chars)
    palindrome = cleaned_string == cleaned_string[::-1]

    letters_count = 0
    for letter in input_string:
        if letter.isalpha():
            letters_count += 1

    numbers_count = 0
    for number in input_string:
        if number.isdigit():
            numbers_count += 1

    capitalize_words = []
    for word in input_string.split():
        capitalize_words.append(word.capitalize())
    capitalize_words = ' '.join(capitalize_words)

    result = {
        'upper_case': upper_case,
        'lower_case': lower_case,
        'replace_spaces': replace_spaces,
        'palindrome': palindrome,
        'letters_count': letters_count,
        'numbers_count': numbers_count,
        'capitalize_words': capitalize_words
    }
    return JsonResponse(result, json_dumps_params={'indent': 2})
