from os.path import exists, abspath
from logging import debug, error
from ast import literal_eval
from copy import copy
from XmlParser import XmlParser


class Parser:
    def __init__(self, co_file_path, xml_file_path):
        self.co_file_path = co_file_path
        self.xml_file_path = xml_file_path
        self.xml_commands = XmlParser(xml_file_path).parse_commands()

    @property
    def xml_file_path(self):
        return self.__xml_file_path

    @xml_file_path.setter
    def xml_file_path(self, xml_file_path):
        if exists(xml_file_path):
            self.__xml_file_path = abspath(xml_file_path)
        else:
            error('[ERR] Incorrect commands xml file path.')
            raise FileNotFoundError('Incorrect commands xml file path')

    @property
    def co_file_path(self):
        return self.__co_file_path

    @co_file_path.setter
    def co_file_path(self, co_file_path):
        if exists(co_file_path):
            self.__co_file_path = abspath(co_file_path)
        else:
            error('[ERR] Incorrect co file path.')
            raise FileNotFoundError('Incorrect co file path')

    def parse_co_file(self):
        commands = []
        with open(self.co_file_path, 'r') as co_file:
            for line in co_file.readlines():
                try:
                    expression = line.split()
                    new_command = self.find_existing_command(expression[0], self.evaluate_body_values(expression[1:]))
                    if new_command is not False:
                        commands.append(new_command)
                except IndexError:
                    debug('[DBG] "{}" line is not correct. Omitting!')
        return commands

    @staticmethod
    def evaluate_body_values(body):
        evaluated_values_list = []
        for value in body:
            try:
                evaluated_values_list.append(literal_eval(value))
            except ValueError:
                evaluated_values_list.append(value)
            except SyntaxError:
                return []
        return evaluated_values_list

    def find_existing_command(self, head, body):
        for command in self.xml_commands:
            if command.structure == head and command.usage_pattern == self.get_list_elements_type(body):
                command = copy(command)
                command.body = body
                return command
        return False

    @staticmethod
    def get_list_elements_type(body):
        return [type(x) for x in body]
