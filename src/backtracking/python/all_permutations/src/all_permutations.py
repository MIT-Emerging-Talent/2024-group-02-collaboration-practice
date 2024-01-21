"""
uthor: tvsirius
Date: 19/01/2024

Function all_permutaions, that will makie all possible combination of items in a list. 
"""
from typing import Collection


def all_permutations(input_list: Collection[any]) -> list[list[any]]:
    """ Will return a list of 2^n elements, where n is a lenght of input_list
    With all possible combination of items in the list

    Args:
        input_list (list[any]): Collection with elements of any type

    Returns:
        list[any]: List of lists with all possible combinations of elements

    >>> all_permutaions([1,2])
    [[1, 2], [2, 1]]

    >>> all_permutaions([1])
    [[1]]

    """
    assert isinstance(input_list, (list, tuple, set, str)
                      ), "input_list must be a collection"


    # Returns [] for emtpy collection
    if len(input_list) < 1:
        return []


    # lets use recursion

    def all_permutations_recursion(input_list: list) -> list[list]:
        """Helper recursion function

        Args:
            input_list (list): input list

        Returns:
            list[list]: list of lists with input elements combination
        """
        # Zero case
        if len(input_list) < 2:
            return [input_list]

        result_list = []

        # this helper function returs a list of lists with all combinations.
        # So we take the one element out, run the function on shortend list,
        # and add all results to the taken element.
        # To do the adding we will use list comprehension
        # Outer loop will take one element one by one

        for i, element in enumerate(input_list):
            permutaion_variants=all_permutations_recursion(input_list[:i]+input_list[i+1:])
            result_list+=[[element]+variant for variant in permutaion_variants]

        return result_list

    return all_permutations_recursion(list(input_list))
