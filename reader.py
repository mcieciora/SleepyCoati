from ast import literal_eval
from Expression import Expression


def read_co_file(file_path):
    read_output = []
    with open(file_path, 'r') as file:
        print('[INF] Reading {}'.format(file_path))
        for line in file.readlines():
            print('[INF] Reading line: {}'.format(line))
            ret_val = validate_line(line)
            if ret_val[0]:
                print('[INF] Positive return value. Appending into read output.')
                read_output.append(ret_val[1])
    return read_output


def value_evaluation(expression_list):
    return_list = []
    print('[INF] Evaluating expression list: {}'.format(expression_list))
    for x in range(len(expression_list)):
        print('[INF] Checking element: {}'.format(x))
        if expression_list[x] != '':
            try:
                print('[INF] Appending converted value ..')
                return_list.append(literal_eval(expression_list[x]))
            except ValueError:
                print('[WAR] Value is string. Appending element without converting.')
                return_list.append(expression_list[x])
    return return_list


def validate_line(line):
    if line != '\n' and line != '':
        split_command_list = ' '.join(line.split())
        split_command_list = split_command_list.replace('\n', '').split(' ')
        print('[INF] Line: {}[INF] Correctly parsed.\n[INF] Returning command head: {} and command body: {}'.format(line,
                                split_command_list[0], value_evaluation(split_command_list[1:])))
        return [True, Expression(split_command_list[0], value_evaluation(split_command_list[1:]))]
    else:
        print('[INF] Empty line discovered. Omitting...')
        return [False]
