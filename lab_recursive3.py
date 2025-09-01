def encode_char(char, rotor_position):
    # coding here
    if (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122):

        if ord(char) >= ord("A") and ord(char) <= ord("Z"):
            base = ord("A")
        elif ord(char) >= ord("a") and ord(char) <= ord("z"):
            base = ord("a")

        shift = rotor_position % 26
        # print(base + (ord(char) - base + shift) % 26)
        new_char = chr(base + (ord(char) - base + shift) % 26)
        # if char = h , need base 'a' to shift +7 to reach h , ord(char) - base + shift = 7
        if new_char == char:
            new_char = chr(base + (ord(char) - base + shift + 1) % 26)
        return new_char
    # print("hi")
    return char
    pass


def decode_char(char, rotor_position):
    if (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122):

        if ord(char) >= ord("A") and ord(char) <= ord("Z"):
            base = ord("A")
        else:
            base = ord("a")

        shift = rotor_position % 26
        # print(base + (ord(char) + shift) % 26)
        new_char = chr(
            base + ((ord(char) - base - shift) % 26)
        )  # if char = h , need base 'a' to shift +7 to reach h , ord(char) - base + shift = 7
        if new_char == char:
            new_char = chr(base + ((ord(char) - base - shift - 1) % 26))
        return new_char
    # print("hi")
    return char
    # coding here
    pass


def encode_message(message, rotor_position, index=0):
    if index >= len(message):
        return ""
    if (
        rotor_position + index
    ) % 26 == 0:  #############################################
        rotor_position += 1
    return encode_char(message[index], rotor_position + index) + encode_message(
        message, rotor_position, index + 1
    )
    # coding here
    pass


def decode_message(encoded_message, rotor_position, index=0):

    # coding here
    if index >= len(encoded_message):
        return ""
    if (
        rotor_position + index
    ) % 26 == 0:  #############################################
        rotor_position += 1
    return decode_char(encoded_message[index], rotor_position + index) + decode_message(
        encoded_message, rotor_position, index + 1
    )
    pass


# การใช้งาน
print("This is Caesar cipher")
message, initial_rotor_position = input("Enter Input : ").split(",")
encoded = encode_message(message, int(initial_rotor_position))
print("Encoded Message:", encoded)
decoded = decode_message(encoded, int(initial_rotor_position))
print("Decoded Message:", decoded)
