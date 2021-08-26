# write a class called  Calculator()

class Calculator:

    # Write your first method
    def add(self, a, b):
        return a + b

    # Raise errors
    def add_with_raise_error(self, a, b):
        if a == 99:
            raise MysteryError
        return a + b


# Inherit Exception method
class MysteryError(Exception):
    pass
