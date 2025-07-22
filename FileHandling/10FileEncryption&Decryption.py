import os

def encrypt_file(source_path, key):
    try:
        with open(source_path, 'rb') as f:
            data = f.read()

        encrypted_data = bytearray([b ^ key for b in data])
        encrypted_path = source_path + '.bin'

        with open(encrypted_path, 'wb') as f:
            f.write(encrypted_data)

        print(f"File encrypted and saved as: {encrypted_path}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error: {e}")

def decrypt_file(encrypted_path, key):
    try:
        with open(encrypted_path, 'rb') as f:
            encrypted_data = f.read()

        decrypted_data = bytearray([b ^ key for b in encrypted_data])
        output_path = encrypted_path.replace('.bin', '_decrypted.txt')

        with open(output_path, 'wb') as f:
            f.write(decrypted_data)

        print(f"File decrypted and saved as: {output_path}")
    except FileNotFoundError:
        print("Encrypted file not found.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    choice = input("Encrypt or Decrypt (e/d): ").lower()
    filepath = input("Enter the file path: ")
    try:
        key = int(input("Enter a number key (0–255): "))
        if not (0 <= key <= 255):
            raise ValueError("Key must be between 0 and 255.")
    except ValueError as ve:
        print(f"Invalid key: {ve}")
        return

    if choice == 'e':
        encrypt_file(filepath, key)
    elif choice == 'd':
        decrypt_file(filepath, key)
    else:
        print("Invalid choice.")

main()
