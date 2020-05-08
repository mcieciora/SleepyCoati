from os.path import join, abspath
from Parser import Parser
from reader import read_co_file
from compile_package.compilants import *


class CompilePackage:
    def __init__(self, compile_package='compile_package', read_co=None, commands_list=None):
        self.compile_package = abspath(compile_package)
        self.read_co = read_co
        self.commands_list = commands_list

    def compile_startup(self):
        print('[INF] Compile startup ..')
        self.read_co = read_co_file(join(self.compile_package, 'compile.co'))
        parser = Parser(self.read_co, join(self.compile_package, 'command.xml'))
        self.commands_list = parser.build_command_list()
        self.read_co = None
        print('[INF] Startup finished.')
        return self

    def compile(self):
        for command in self.commands_list:
            print('[INF] Executing command: {}'.format(command.name, command.body))
            exec('{}({})'.format(command.name, command.body))
        print('[INF] Compile finished.')
