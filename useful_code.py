class NumberPrinter:

    def __init__(self, max):
        self.max = max

    def print_numbers(self):
        for i in range(self.max + 1):
            print(i)
