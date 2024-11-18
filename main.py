import src.encryption

def main():
    shift = int(input("Enter the shift value: "))
    caesar = src.encryption.CaesarCipher(shift)

    message = input("Enter message to encrypt: ")
    encrypted = caesar.encrypt(message)
    print(f"Encrypted Message: {encrypted}")

    decrypted = caesar.decrypt(encrypted)
    print(f"Decrypted message: {decrypted}")

if __name__ == "__main__":
    main()