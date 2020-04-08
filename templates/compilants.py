def define_variable(variables_list):
    globals()[variables_list[0]] = None


def set_variable(variables_list):
    globals()[variables_list[0]] = variables_list[1]


def get_variable(variables_list):
    return globals()[variables_list[0]]


def get_type(variables_list):
    return type(globals()[variables_list[0]])
