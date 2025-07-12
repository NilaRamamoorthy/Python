# Message Encoder/Decoder

# Function to encode a message to ASCII
def encode_message(message):
    encoded = [str(ord(char)) for char in message]
    return ' '.join(encoded)

# Function to decode an ASCII message back to text
def decode_message(encoded_message):
    try:
        codes = encoded_message.split()
        decoded = ''.join([chr(int(code)) for code in codes])
        return decoded
    except ValueError:
        return " Invalid encoded message format."

# Main menu
def message_tool():
    print(" Message Encoder/Decoder")
    while True:
        print("\nChoose an option:")
        print("1. Encode Message")
        print("2. Decode Message")
        print("3. Exit")

        choice = input("Enter your choice (1–3): ").strip()

        if choice == "1":
            msg = input("Enter message to encode: ")
            print(" Encoded Message:", encode_message(msg))
        elif choice == "2":
            encoded = input("Enter encoded message (ASCII codes separated by space): ")
            print(" Decoded Message:", decode_message(encoded))
        elif choice == "3":
            print(" Exiting Encoder/Decoder.")
            break
        else:
            print("Invalid choice. Try again.")

# Run the app
message_tool()
