class MySet:
    def __init__(self, initial=None):
        # Backing store required by the tests
        self.dictionary = {}

        if initial:
            for value in initial:
                self.dictionary[value] = True  # placeholder

    def add(self, value):
        self.dictionary[value] = True

    def delete(self, value):
        if value in self.dictionary:
            del self.dictionary[value]

    def has(self, value):
        return value in self.dictionary

    def size(self):
        return len(self.dictionary)
