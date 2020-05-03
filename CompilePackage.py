from Parser import Parser
from reader import read_co_file
from templates import compilants


class CompilePackage:
    def __init__(self, co_file, xml_file, py_compiler, read_co=None, commands_list=None):
        self.co_file = co_file
        self.xml_file = xml_file
        self.py_compiler = py_compiler
        self.read_co = read_co
        self.commands_list = commands_list

    def compile_startup(self):
        print('[INF] Compile startup ..')
        self.read_co = read_co_file(self.co_file)
        parser = Parser(self.read_co, self.xml_file)
        self.commands_list = parser.build_command_list()
        self.read_co = None
        print('[INF] Compile finished.')
        return self

    def compile(self):
        for command in self.commands_list:
            print('[INF] Executing command: {}'.format(command))
            exec('compilants.{}({})'.format(command.name, command.body))
