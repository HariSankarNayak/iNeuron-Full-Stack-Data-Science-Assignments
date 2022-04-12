#  ASCII of a character


def char_ascii_value(chhrr):
    return ord(chhrr)


entered_char = input("Enter a character: ")

print(f"The ASCII value of {entered_char} is {char_ascii_value(entered_char)}")
