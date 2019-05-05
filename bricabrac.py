#
""" """
from itertools import reduce
import numpy as np


def map_functions(funcs, elements):
    """The basic way
    result = []
    for el in elements:
        for f in funcs:
            el = f(el)
        result.append(el)
    
    """
    return list(map(lambda elt: reduce(lambda e, f: f(e), funcs, elt), elements))


def is_none(x, none_values=None, excluded_none_values=None):
    """A more complete function to check if a value is null.
    It includes numpy.nan.

    """
    if none_values is None:
        none_values = ['nan']
    if excluded_none_values is None:
        excluded_none_values = []
    return ((np.isnan(x) if isinstance(x, (int, float) else not x)) or x in none_values) and x not in excluded_none_values