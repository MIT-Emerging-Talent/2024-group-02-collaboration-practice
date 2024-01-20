"""
Author: tvsirius
Date 18/01/2024

Adding string numbers challenge for learning
"""

def add_string_numbers(string_number_1: str, string_number_2: str) -> str:
    """Adds two numbers in string format, and returns a string with their sum

    Args:
        string_number_1 (str): String with number 1
        string_number_2 (str): Srting with number 2

    Returns:
        str: String with sum
    """

    def is_number(s: str) -> bool:
        """helper function for assertions
            s (_type_): string to check if it's number
        Returns: bool: True if s is number (int or float)
        """
        try:
            float(s)
            return True
        except ValueError:
            return False

    assert isinstance(
        string_number_1, str), "First argument must be string type"
    assert isinstance(
        string_number_2, str), "Second argument must be string type"
    assert is_number(string_number_1.strip()) and is_number(
        string_number_2.strip()), "Arguments must contain numbers"


    num1 = float(string_number_1.strip())
    num2 = float(string_number_2.strip())

    # Complex solution to get rid of float +.00000000001 errors
    # get the number of digits, and round the result to the max of it
    # Sum will never exceed number of digits of items

    digits_in_num1=string_number_1.find('.')
    if digits_in_num1>0:
        digits_in_num1=len(string_number_1)-digits_in_num1-1

    digits_in_num2=string_number_2.find('.')
    if digits_in_num2>0:
        digits_in_num2=len(string_number_2)-digits_in_num2-1

    # The main thing
    result = num1+num2

    # To make the result match the args type, if int - make int:
    if digits_in_num1<1 and digits_in_num2<1:
        return str(int(result))

    # Otherwise type is float
    return str(round(result,max(digits_in_num1,digits_in_num2)+1))
