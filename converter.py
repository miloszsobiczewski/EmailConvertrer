import re

class EmailConverter:
    regex = r'[^@]+@[^@]+\.[^@]+'
    def to_python(self, value):
        EMAIL_REGEX = re.compile(self.regex)
        if not EMAIL_REGEX.match(value):
            raise ValueError
        return value
    def to_url(self, value):
        return str(value)
