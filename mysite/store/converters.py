class dateConverter:
    regex = '([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))'

    def to_python(self, value):
        return str(value)

    def to_url(self, value):
        return value
