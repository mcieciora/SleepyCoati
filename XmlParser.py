from xmltodict import parse
from Command import Command


class XmlParser:
    def __init__(self, xml_parser_path):
        self.xml_parser_path = xml_parser_path

    def parse_commands(self):
        all_commands = []
        with open(self.xml_parser_path) as co:
            commands = parse(co.read())['commands']['command']
        if type(commands) != list:
            commands = [commands]
        for command in commands:
            all_commands.append(Command(command['structure'], command['name'],
                                        self.get_usage_patterns(command['usage_pattern'])))
        return all_commands

    @staticmethod
    def get_usage_patterns(command):
        try:
            usage_pattern_list = command['element']
            if type(usage_pattern_list) != list:
                usage_pattern_list = [usage_pattern_list]
            ret_val = [eval(element) for element in usage_pattern_list]
            return ret_val
        except (TypeError, KeyError):
            return []
