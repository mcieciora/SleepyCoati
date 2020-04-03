import ast
from Expression import Expression


def read_co_file(file_path):
    read_output = []
    with open(file_path, 'r') as file:
        for line in file.readlines():
            split_command_list = line.replace('\n', '').split(' ')
            read_output.append(Expression(split_command_list[0], value_evaluation(split_command_list[1:])))
    return read_output


def value_evaluation(expression_list):
    for x in range(len(expression_list)):
        try:
            expression_list[x] = ast.literal_eval(expression_list[x])
        except ValueError:
            pass
    return expression_list
