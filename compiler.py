def define_variable(variable_name):
    globals()[variable_name] = None


def set_variable(variable_name, variable_value):
    globals()[variable_name] = variable_value


def get_variable(variable_name):
    return globals()[variable_name]
