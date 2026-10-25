
def encrypt(text, shift):
    result = ""

    for char in text:
        if "A" <= char <= "Z":
            base = ord("A")
        elif "a" <= char <= "z":
            base = ord("a")
        else:
            result += char
            continue

        new_position = (ord(char) - base + shift) % 26
        result += chr(base + new_position)

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def main():
    print("=== Decode Labs: Project 2 ===")
    print("Caesar Cipher Encryption & Decryption")

    text = input("\nEnter your message: ")

    try:
        shift = int(input("Enter shift key (1-25): "))
    except ValueError:
        print("Error: shift must be an integer.")
        return

    if not 1 <= shift <= 25:
        print("Error: shift must be between 1 and 25.")
        return

    encrypted = encrypt(text, shift)
    decrypted = decrypt(encrypted, shift)

    print("\nOriginal text:", text)
    print("Encrypted text:", encrypted)
    print("Decrypted text:", decrypted)

    if decrypted == text:
        print("\nVerification: PASSED")
    else:
        print("\nVerification: FAILED")


if __name__ == "__main__":
    main()
