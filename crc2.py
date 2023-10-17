def encode_crc(message, polynomial):
    message1 = message + "0" * (len(polynomial) - 1)
    int_message = int(message1, 2)  # Convert the binary string to an integer
    int_polynomial = int(polynomial, 2)  # Convert the binary string to an integer
    int_remainder = int_message % int_polynomial
    remainder = bin(int_remainder)[2:].zfill(len(polynomial) - 1)
    encoded_message = message + remainder
    return encoded_message

def CRC_check(encoded_message, polynomial):
    int_message = int(encoded_message, 2)  # Convert the binary string to an integer
    int_polynomial = int(polynomial, 2)  # Convert the binary string to an integer
    int_remainder = int_message % int_polynomial
    if int_remainder == 0:
        print("No error found")
    else:
        print("Error found")

def main():
    message = input("Enter binary message: ")
    polynomial = input('Enter polynomial (in binary): ')
    enc_msg = encode_crc(message, polynomial)
    print('Encoded message is', enc_msg)
    CRC_check(enc_msg, polynomial)

if __name__ == '__main__':
    main()
