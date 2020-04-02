from .Expression import Expression
from .Command import Command


# temporary read function
def read_co_file(file_path):
    read_output = []
    with open(file_path, 'r') as file:
        for line in file.readlines():
            split_command_list = line.replace('\n', '').split(' ')
            if check_usage_pattern_correctness(split_command_list[0], split_command_list[1:]):
                read_output.append(Expression(split_command_list[0], split_command_list[1:]))
    return read_output


def check_usage_pattern_correctness(structure, expression_list):
    if set(get_list_elements_type(expression_list)) == set(get_command_by_structure(structure).usage_pattern):
        return True
    return False


def get_list_elements_type(expression_list):
    return [type(x) for x in convert_ints(expression_list)]


def get_command_by_structure(structure):
    for command in command_list:
        if command.structure == structure:
            return command


def convert_ints(expression_list):
    new_list = []
    for element in expression_list:
        try:
            element = int(element)
        except ValueError:
            pass
        new_list.append(element)
    return new_list


command_list = [
    Command('#d', 'define_variable',  [str]),
    Command('#v', 'variable_define_set', [str, int]),
    Command('#s', 'set_variable',  [str, int]),
    Command('#g', 'get_variable', [str])
]
