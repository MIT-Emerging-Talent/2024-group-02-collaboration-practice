"""
Author: tvsirius
Date 22/01/2024

Takes a string containing parentheses and returns the minimum number of deletions 
needed to make the parentheses valid
"""


def deletions_to_make_valid_parentheses(input_string: str) -> int:
    """Check how many parentheses are not in place, and return number
    Leading close parenteses (even with following openeing) are also need to be deleted

    Args:
        input_string (str): String with parenthese

    Returns:
        int: number of parentheses to be deleted

    >>> deletions_to_make_valid_parentheses(')()(')
    2

    >>> deletions_to_make_valid_parentheses('((()))())')
    0

    >>> deletions_to_make_valid_parentheses('(()))())')
    1

    """

    assert isinstance(input_string, str), "Input argument must be string"

    opened_pars = 0
    wrong_pars = 0

    # just simple iteration
    for char in input_string:
        # open_pars counts currently open pars, so if we close them -> 0 -> no error
        if char == ')' and opened_pars > 0:
            opened_pars -= 1
        # closing parentses with no open par automatically counts as errors
        elif char == ')':
            wrong_pars += 1
        elif char == '(':
            opened_pars += 1

    # all not closed are errors + all wrong closing

    return opened_pars+wrong_pars
