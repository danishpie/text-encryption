import argparse
import src.encryption as encryption

def main():
    parser = argparse.ArgumentParser(description="Cipher Encryption/Decryption Program")
    
    parser.add_argument('cipher', choices=['caesar', 'vigenere'], help='Choose the cipher to use: caesar or vigenere')
    parser.add_argument('action', choices=['encrypt', 'decrypt'], help='Action to perform')
    parser.add_argument('message', help='The message to encrypt or decrypt')
    parser.add_argument('--shift', type=int, help='Shift value for Caesar cipher')
    parser.add_argument('--key', help='Key for Vigenère cipher')
    
    args = parser.parse_args()

    if args.cipher == 'caesar':
        if not args.shift:
            parser.error("The --shift argument is required for Caesar cipher")
        cipher = encryption.CaesarCipher(args.shift)
        if args.action == 'encrypt':
            result = cipher.encrypt(args.message)
        else:
            result = cipher.decrypt(args.message)
    elif args.cipher == 'vigenere':
        if not args.key:
            parser.error("The --key argument is required for Vigenère cipher")
        cipher = encryption.VigenereCipher(args.key)
        if args.action == 'encrypt':
            result = cipher.encrypt(args.message)
        else:
            result = cipher.decrypt(args.message)

    print(f"Result: {result}")

if __name__ == "__main__":
    main()