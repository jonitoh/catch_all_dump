#
""" """


def map_functions(funcs, elements):
    """The basic way
    result = []
    for el in elements:
        for f in funcs:
            el = f(el)
        result.append(el)
    
    """
    from functools import reduce
    return list(map(lambda elt: reduce(lambda e, f: f(e), funcs, elt), elements))


def is_none(x, none_values=None, excluded_none_values=None):
    """A more complete function to check if a value is null.
    It includes numpy.nan.

    """
    import numpy as np
    if none_values is None:
        none_values = ['nan']
    if excluded_none_values is None:
        excluded_none_values = []
    return ( np.isnan(x) if isinstance(x, (int, float)) else not x or x in none_values ) and x not in excluded_none_values

COMPARISON_FUNCS = {'=': (lambda x, val: x == val),
'<=': (lambda x, val: x <= val),
'<': (lambda x, val: x < val),
'>':(lambda x, val: x > val),
'>=': (lambda x, val: x >= val),
'!=': (lambda x, val: x != val)
}

def smart_which(x, inputs, outputs, default_value, missing_value, how='<', custom_which_func=None, custom_missing_value=None):
    """How to do a switch case in python without having a fixed length of conditions.

    Args:
        x, inputs, outputs, default_value, missing_value, how, custom_which_func, custom_missing_value

    
    Returns:
        result

    """
    if is_none(x):
        return missing_value
    result = default_value

    condition = COMPARISON_FUNCS.get(how, COMPARISON_FUNCS['<'])
    if custom_which_func is not None:
        condition = custom_which_func
    try:
        result = next(out for inp, out in zip(inputs[:-1], outputs[:-1]) if condition(x, inp))
    except:
        pass
    return result


def deduplicate_fields_with_no_remove(fields):
    """ Counter va permettre de compter les occurences.
        Par exemple: 
        fields = ['a', 'b', 'c', 'd', 'a', 'a', 'e', 'f', 'g', 'd', 'u', 'h']
        Counter(fields) = Counter({'a': 3,
         'b': 1,
         'c': 1,
         'd': 2,
         'e': 1,
         'f': 1,
         'g': 1,
         'u': 1,
         'h': 1})
         new_fields =  ['a', 'b', 'c', 'd', 'a_1', 'a_2', 'e', 'f', 'g', 'd_1', 'u', 'h']
    
    """
    from collections import Counter
    # ainsi il ne restera que les colonnes ayant des doublons
    my_counter = Counter(fields) - Counter(set(fields))
    new_fields = [ ]
    for col in reversed(fields):
        new_col = col
        if my_counter[col]:# il y a au moins un doublon
            new_col = "{}_{}".format(col, my_counter[col])
            my_counter[col] -= 1 # on retire un compteur
        new_fields.append(new_col)        
    new_fields = reversed(new_fields)
    return new_fields
