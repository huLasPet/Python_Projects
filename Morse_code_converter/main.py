from morse_converter import Converter

if __name__ == "__main__":
    print("Morse code converter, use characters that are found in the International Morse table.")
    message = input("Type in the message you want to see in Morse code: ")
    convert = Converter()
    print(convert.convert_to_morse(message))
