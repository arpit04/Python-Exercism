WORDS = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
         8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
         14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
         19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
         70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand',
         10**6: 'million', 10**9: 'billion'}

def say(number):
    if not 0 <= number <= 999999999999:
        raise ValueError("Value must be between 0 and 999,999,999,999.")
    result = []
    if number in WORDS and number <= 100:
        result = [WORDS[number]]
    else:
        for num in sorted(WORDS.keys(), reverse=True):
            if num == 0 or number < num:
                continue
            multiplier = number // num
            number -= num * multiplier
            if multiplier != 1:
                result.append(say(multiplier))
                result.append(WORDS[num])
            elif num in [100, 1000, 10**6, 10**9]:
                result.append(WORDS[1])
                result.append(WORDS[num])
            elif 20 <= num < 100 and number != 0:
                result.append("{}-{}".format(WORDS[num], WORDS[number]))
                number = 0
            else:
                result.append(WORDS[num])
    for i in sorted((i for i, v in enumerate(result) if v == "hundred"), reverse=True):
        if i + 1 < len(result) and result[i+1] != "and":
            result.insert(i+1, "and")

    return " ".join(result)

number = int(input("Enter Number :"))
print(say(number))
