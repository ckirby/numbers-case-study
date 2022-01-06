def do_humanize(number: int) -> str:
    THOUSAND = 10 ** 3
    MAGNITUDES = {
        10 ** 18: "quintillion",
        10 ** 15: "quadrillion",
        10 ** 12: "trillion",
        10 ** 9: "billion",
        10 ** 6: "million",
        THOUSAND: "thousand",
    }

    if number == 0:
        return "zero"

    humanized_number = []
    if number < 0:
        humanized_number.append("negative")
        number *= -1

    for magnitude, text in MAGNITUDES.items():
        if 0 < number < THOUSAND:
            break
        current, number = divmod(number, magnitude)
        if current > 0:
            humanized_number.append(get_text_for_magnitude(current))
            humanized_number.append(text)

    if number > 0:
        humanized_number.append(get_text_for_magnitude(number))

    return " ".join(humanized_number)


def get_text_for_magnitude(number: int) -> str:
    if number < 1:
        raise ValueError("Positive, non-zero number expected")
    if number > 999:
        raise ValueError("Number less than 1000 expected")

    TENS = {
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety",
    }

    SINGLES = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }
    TEENS = {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
    }

    hundreds, tens = divmod(number, 10 ** 2)
    text = []
    if hundreds > 0:
        text.append(f"{SINGLES[hundreds]} hundred")

    digit = 0
    if tens >= 20:
        ten = tens // 10
        text.append(TENS[ten])
        digit = tens - (ten * 10)
    elif 9 < tens:
        text.append(TEENS[tens])
    else:
        digit = tens

    if digit > 0:
        text.append(SINGLES[digit])
    return " ".join(text)
