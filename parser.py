import xml_parser
import reader
from Command import Command


def build_command_list(co_file_path, xml_file_path):
    commands_list = []
    for expression in reader.read_co_file(co_file_path):
        pattern = find_pattern_usage(expression, xml_file_path)
        if pattern[0]:
            commands_list.append(Command(expression.head, pattern[1].name, pattern[1].usage_pattern, expression.body))
        else:
            commands_list = []
            break
    return commands_list


def find_pattern_usage(expression_object, xml_file_path):
    for gcbs in get_command_by_structure(expression_object.head, xml_file_path):
        if gcbs is not None and get_list_elements_type(expression_object.body) == gcbs.usage_pattern:
            return [True, gcbs]
    return [False]


def get_list_elements_type(expression_list):
    return [type(x) for x in expression_list]


def get_command_by_structure(structure, xml_file_path):
    full_commands_list = []
    for command in xml_parser.generate_all_commands_list(xml_file_path):
        if command.structure == structure:
            full_commands_list.append(command)
    return full_commands_list
