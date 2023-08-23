__all__ = ['convert_to_string']


def convert_to_string(my_input):
    if isinstance(my_input, list):
        return str(my_input)
    elif isinstance(my_input, int):
        return str(my_input)
    elif isinstance(my_input, float):
        return str(my_input)
    else:
        return my_input
    
def additional_helper_1(my_input):
    print('helping additional 1')
