def evaluate_expression(s):
    pass

def parse_numerical_value(exp, index=0):
    """
    Parses a numerical value from a string expression starting at the given index.
    Args:
        exp (str): The string expression containing the numerical value.
        index (int, optional): The starting index to parse the numerical value. Defaults to 0.
    Returns:
        tuple: A tuple containing the parsed numerical value (float) and the index (int) 
                where the parsing ended.
    """
    start_index = index
    if exp[index] == "-":
        index += 1

    while index < len(exp) and (exp[index].isdigit() or exp[index] == '.'):
        index += 1

    value = float(exp[start_index:index])
    return value, index