from Parser import Parser

# TODO execute main.py with arguments:
# STAGE FILES: SleepyCoati --stage <file_name>
# COMPILE STAGED PACKAGE: SleepyCoati --compile <package_name>
# ENCRYPT/DECRYPT: SleepyCoati --encrypt or --decrypt <package_name>
# DISCOVER: SleepyCoati --discover

# ARCHIVE: SleepyCoati --zip <package_name>
# REPACK: Sleepy Coait --repack <file_name> <package_name>

new_parser = Parser('compile_package/compile.co', 'compile_package/command.xml')
commands = new_parser.parse_co_file()

print('abc')
