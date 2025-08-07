def encode_char(char, rotor_position):
    #coding here
    pass

def decode_char(char, rotor_position):
    #coding here
    pass

def encode_message(message, rotor_position):
    #coding here
    pass
    
def decode_message(encoded_message, rotor_position):
    #coding here
    pass
    

# การใช้งาน
print("This is Caesar cipher")
message ,initial_rotor_position = input("Enter Input : ").split(',')
encoded = encode_message(message, int(initial_rotor_position))
print("Encoded Message:",encoded)
decoded = decode_message(encoded, int(initial_rotor_position))
print("Decoded Message:", decoded)
