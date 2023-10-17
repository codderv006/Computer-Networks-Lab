def encode_CRC(message, polynomial):
   message = message + '0' * (len(polynomial) - 1)
   int_message = int(message, 2)
   int_polynomial = int(polynomial, 2)
   int_remainder = int_message % int_polynomial
   remainder = bin(int_remainder)[2:].zfill(len(polynomial) - 1)
   encoded_message = message + remainder
   return encoded_message

def check_CRC(encoded_message, polynomial):
   int_encoded = int(encoded_message, 2)
   int_polynomial = int(polynomial, 2)
   int_remainder = int_encoded % int_polynomial
   if int_remainder == 0:
       print("No Error found")
   else:
       print("Error found")

# def main():
message = input("Enter the binary message: ")
polynomial = input("Enter the binary polynomial divisor: ")

encoded_message = encode_CRC(message, polynomial)
print("Encoded Message:", encoded_message)

# Simulate transmission by introducing errors (if desired)
# To simulate an error, you can toggle a bit in the encoded message.
# For example, to flip the first bit, you can use: encoded_message = "1" + encoded_message[1:]

check_CRC(encoded_message, polynomial)

# if __name__ == "__main__":
#    main()
