def verify_card_number(card_number: str):

    # removing whitespace and dashes
    card = ''
    for num in card_number:
        if num.isdigit():
            card += num

    # card needs to be read from right to left
    reversed_card = card[::-1]
    
    total = 0

    for index, char in enumerate(reversed_card):
        # convert str to int
        num = int(char)

        # double every other digit
        if index % 2 == 1:
            doubled = num * 2
            total += doubled - 9 if doubled > 9 else doubled
        else:
            total += num

    return 'VALID!' if total % 10 == 0 else 'INVALID!'
