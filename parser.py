import xml_parser
import reader
from Command import Command


def build_command_list(co_file_path):
    commands_list = []
    for expression in reader.read_co_file(co_file_path):
        command = get_command_by_structure(expression.head)
        commands_list.append(Command(expression.head, command.name, command.usage_pattern, expression.body))
    return commands_list


def check_usage_pattern_correctness(expression_object):
    if set(get_list_elements_type(expression_object.body)) == \
            set(get_command_by_structure(expression_object.head).usage_pattern):
        return True
    return False


def get_list_elements_type(expression_list):
    return [type(x) for x in expression_list]


def get_command_by_structure(structure):
    for command in xml_parser.generate_all_commands_list('command.xml'):
        if command.structure == structure:
            return command
