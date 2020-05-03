from xmltodict import parse
from Command import Command


def generate_all_commands_list(xml_file_path):
    print('[INF] Parsing {} xml file'.format(xml_file_path))
    with open(xml_file_path) as co:
        xml_file = parse(co.read())
    all_commands = []
    commands = xml_file['commands']['command']
    print('[INF] Commands found: {}'.format(commands))
    if type(commands) != list:
        print('[INF] Commands is not list type. Converting into list ..')
        commands = [commands]
    for command in commands:
        print('[INF] Reading command {}'.format(command))
        print('[INF] Creating Command object ..\n[...] structure: {}\n[...] name: {}\n[...] usage pattern: {}'.format(
            command['structure'], command['name'], get_usage_patterns(command['usage_pattern'])))
        new_command = Command(command['structure'], command['name'], get_usage_patterns(command['usage_pattern']))
        print('[INF] Appending object into all commands list ..')
        all_commands.append(new_command)
    return all_commands


def get_usage_patterns(command):
    if len(command) > 0:
        usage_pattern_list = command['element']
        print('[INF] Found element in command: {}'.format(usage_pattern_list))
        if type(usage_pattern_list) != list:
            print('[INF] Element is not list type. Converting into list ..')
            usage_pattern_list = [usage_pattern_list]
        ret_val = [eval(element) for element in usage_pattern_list]
        print('[INF] Returning evaluated list of elements: {}'.format(ret_val))
        return ret_val
    else:
        print('[ERR] command is null. Returning empty list ..')
        return []
