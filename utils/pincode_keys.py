from constants import FIRST_2_DIGIT_PINCODE, FIRST_1_DIGIT_MEANING


def first_two_digit_meaning():
    meaning = {}
    for item in FIRST_2_DIGIT_PINCODE.items():
        if type(item[1]) != int:
            for code in range(item[1][0], item[1][1]):
                meaning.update({code: item[0]})
        else:
            meaning.update({item[1]: item[0]})
    return meaning


def get_pincode_details(pincode: str):
    pincode = pincode.strip()
    first_one_digit = int(pincode[0])
    first_two_digit = int(pincode[:2])
    return FIRST_1_DIGIT_MEANING.get(first_one_digit), first_two_digit_meaning().get(first_two_digit)


#


