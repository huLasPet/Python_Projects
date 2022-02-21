class Converter:
    """Morse code converter. Takes a message and returns it in Morse code."""
    def __init__(self, message):
        self.message_list = list(message)

    def convert(self):
        return self.message_list
