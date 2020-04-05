import xml_parser
import reader
from Command import Command


def build_command_list(co_file_path, xml_file_path):
    commands_list = []
    for expression in reader.read_co_file(co_file_path):
        if check_usage_pattern_correctness(expression, xml_file_path):
            command = get_command_by_structure(expression.head, xml_file_path)
            commands_list.append(Command(expression.head, command.name, command.usage_pattern, expression.body))
        else:
            commands_list = []
            break
    return commands_list


def check_usage_pattern_correctness(expression_object, xml_file_path):
    gcbs = get_command_by_structure(expression_object.head, xml_file_path)
    if gcbs is not None and get_list_elements_type(expression_object.body) == gcbs.usage_pattern:
        return True
    else:
        return False


def get_list_elements_type(expression_list):
    return [type(x) for x in expression_list]


def get_command_by_structure(structure, xml_file_path):
    for command in xml_parser.generate_all_commands_list(xml_file_path):
        if command.structure == structure:
            return command
