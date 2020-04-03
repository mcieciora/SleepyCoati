class Command:
    def __init__(self, structure, name, usage_pattern, body=None):
        self.structure = structure
        self.name = name
        self.usage_pattern = usage_pattern
        self.body = body
