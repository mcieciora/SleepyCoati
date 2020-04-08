from xml_parser import generate_all_commands_list
from Command import Command


class Parser:
    def __init__(self, read_co, xml_file_path):
        self.read_co = read_co
        self.xml_file_path = xml_file_path

    def build_command_list(self):
        commands_list = []
        for expression in self.read_co:
            pattern = self.find_pattern_usage(expression)
            if pattern[0]:
                commands_list.append(Command(expression.head, pattern[1].name, pattern[1].usage_pattern, expression.body))
            else:
                commands_list = []
                break
        return commands_list

    def find_pattern_usage(self, expression_object):
        for gcbs in self.get_command_by_structure(expression_object.head):
            if gcbs is not None and self.get_list_elements_type(expression_object.body) == gcbs.usage_pattern:
                return [True, gcbs]
        return [False]

    def get_command_by_structure(self, structure):
        full_commands_list = []
        for command in generate_all_commands_list(self.xml_file_path):
            if command.structure == structure:
                full_commands_list.append(command)
        return full_commands_list

    @staticmethod
    def get_list_elements_type(expression_list):
        return [type(x) for x in expression_list]
