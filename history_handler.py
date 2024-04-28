class HistoryHandler:
    def __init__(self, filename):
        self.filename = filename
        self.history = self.read_history()

    def read_history(self):
        try:
            with open(self.filename, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            return []

    def write_history(self, conversion):
        with open(self.filename, 'a') as file:
            file.write(conversion + '\n')

    def print_history(self):
        if not self.history:
            print("No conversion history available.")
        else:
            for i, conversion in enumerate(self.history, 1):
                print(f"{i}. {conversion.strip()}")