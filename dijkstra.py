def evaluate_expression(s):
    pass

def parse_numerical_value(exp, index = 0):
    """
    Parses a numerical value from a string expression starting at the given index.
    Args:
        exp (str): The string expression containing the numerical value.
        index (int, optional): The starting index to parse the numerical value. Defaults to 0.
    Returns:
        tuple: A tuple containing the parsed numerical value (float) and the index (int) 
                where the parsing ended.
    """
    is_neg = False
    if exp[index] == "-":
        is_neg = True
        index += 1

    value = 0
    decimal_place = -1
    while index < len(exp) and (exp[index].isdigit() or exp[index] == '.'):
        if exp[index] == '.':
            decimal_place = 0
        else:
            digit = int(exp[index])
            if decimal_place == -1:
                value = value * 10 + digit
            else:
                decimal_place += 1
                value += digit * (10 ** -decimal_place)
        index += 1

    if is_neg:
        value = -value

    return value, index