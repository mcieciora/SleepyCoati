class Command:
    def __init__(self, structure, name, usage_pattern, body=None):
        self.structure = structure
        self.name = name
        self.usage_pattern = usage_pattern
        self.body = body

    @property
    def usage_pattern(self):
        return self.__usage_pattern

    @usage_pattern.setter
    def usage_pattern(self, usage_pattern):
        if not usage_pattern:
            print('[ERR] Usage pattern cannot be empty list!')
        else:
            self.__usage_pattern = usage_pattern
