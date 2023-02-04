num = int(input("Enter a Number :  "))  # input from user
def number_to_words(num):
    units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eitht", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventheen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if num < 20:
        return units[num]
    elif num < 100:
        return tens[num // 10] + (' ' if num % 10 == 0 else ' ' + units [num % 10])
    elif num < 1000:
        return units[num // 100] + " hundred" + (' ' if num % 100 == 0
                                                 else ' ' + number_to_words(num % 100))
    elif num < 1000000:
        return number_to_words (num // 1000) + " thousand" + (
            ' ' if num % 1000 == 0 else ' ' + number_to_words (num % 1000))
    elif num < 1000000000:
        return number_to_words (num // 1000000) + " million" + (
            ' ' if num % 1000000 == 0 else ' ' + number_to_words (num % 1000000))
    else: 
        return "Number out of range."

print(number_to_words(num))
        