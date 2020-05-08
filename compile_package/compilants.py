def define_variable(variables_list):
    globals()[variables_list[0]] = None
    print('Variable defined: {}'.format(globals()[variables_list[0]]))


def set_variable(variables_list):
    globals()[variables_list[0]] = variables_list[1]
    print('Variable value set: {}'.format(globals()[variables_list[0]]))


def get_variable(variables_list):
    print('{} value: {}'.format(variables_list[0], globals()[variables_list[0]]))


def get_type(variables_list):
    print('{} value type: {}'.format(variables_list[0], type(globals()[variables_list[0]])))
