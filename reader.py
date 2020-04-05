from ast import literal_eval
from Expression import Expression


def read_co_file(file_path):
    read_output = []
    with open(file_path, 'r') as file:
        for line in file.readlines():
            ret_val = validate_line(line)
            if ret_val[0]:
                read_output.append(ret_val[1])
    return read_output


def value_evaluation(expression_list):
    return_list = []
    for x in range(len(expression_list)):
        if expression_list[x] != '':
            try:
                return_list.append(literal_eval(expression_list[x]))
            except ValueError:
                return_list.append(expression_list[x])
    return return_list


def validate_line(line):
    if line != '\n':
        split_command_list = ' '.join(line.split())
        split_command_list = split_command_list.replace('\n', '').split(' ')
        return [True, Expression(split_command_list[0], value_evaluation(split_command_list[1:]))]
    else:
        return [False]
