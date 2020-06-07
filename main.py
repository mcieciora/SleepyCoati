from Parser import Parser

# TODO execute main.py with arguments:
# compile [-d package_directory] or [-z zipped_package]

new_parser = Parser('compile_package/compile.co', 'compile_package/command.xml')
commands = new_parser.parse_co_file()
