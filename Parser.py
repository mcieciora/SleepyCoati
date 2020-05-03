from xml_parser import generate_all_commands_list
from Command import Command


class Parser:
    def __init__(self, read_co, xml_file_path):
        self.read_co = read_co
        self.xml_file_path = xml_file_path

    def build_command_list(self):
        commands_list = []
        print('[INF] Building commands list ..')
        for expression in self.read_co:
            print('[INF] Parsing expression: {} from read compile'.format(expression))
            pattern = self.find_pattern_usage(expression)
            print('[INF] Pattern set: {}'.format(pattern))
            if pattern[0]:
                print('[INF] Pattern is correct\n[INF] Appending command object into command list:'
                      '\n[...] head: {}\n[...] name: {}\n[...] usage pattern: {}\n[...] body: {}'.format(expression.head, pattern[1].name,
                                                                                  pattern[1].usage_pattern, expression.body))
                commands_list.append(Command(expression.head, pattern[1].name, pattern[1].usage_pattern, expression.body))
            else:
                print('[ERR] Pattern is incorrect. Returning empty command list.')
                commands_list = []
                break
        return commands_list

    def find_pattern_usage(self, expression_object):
        print('[INF] Searching for pattern usage ..')
        for gcbs in self.get_command_by_structure(expression_object.head):
            if gcbs is not None and self.get_list_elements_type(expression_object.body) == gcbs.usage_pattern:
                print('[INF] Pattern is correct')
                return [True, gcbs]
        print('[ERR] Pattern not found')
        return [False]

    def get_command_by_structure(self, structure):
        full_commands_list = []
        print('[INF] Parsing commands in {}'.format(self.xml_file_path))
        for command in generate_all_commands_list(self.xml_file_path):
            print('[INF] For {} command checking if structures are equal ..'.format(command.name))
            if command.structure == structure:
                print('[INF] {} == {}'.format(command.structure, structure))
                full_commands_list.append(command)
        print('[INF] Returning all matching cases: {}'.format(*full_commands_list))
        return full_commands_list

    @staticmethod
    def get_list_elements_type(expression_list):
        return [type(x) for x in expression_list]
