from xmltodict import parse
from Command import Command


def generate_all_commands_list(xml_file_path):
    with open(xml_file_path) as co:
        xml_file = parse(co.read())
    all_commands = []
    commands = xml_file['commands']['command']
    if type(commands) != list:
        commands = [commands]
    for command in commands:
        new_command = Command(command['structure'], command['name'], get_usage_patterns(command['usage_pattern']))
        all_commands.append(new_command)
    return all_commands


def get_usage_patterns(command):
    if len(command) > 0:
        usage_pattern_list = command['element']
        if type(usage_pattern_list) != list:
            usage_pattern_list = [usage_pattern_list]
        return [eval(element) for element in usage_pattern_list]
    else:
        return []
