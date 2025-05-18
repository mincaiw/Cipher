import re
import argparse

def get_original_text(filename='input.txt'):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"{filename} not found")
        return ""  

def get_shift_amount():
    parser = argparse.ArgumentParser(description="Caesar Cipher Encryption/Decryption Program.")
    parser.add_argument('--shift', type=int, required=True, help="Shift amount for the Caesar cipher (an integer)")
    parser.add_argument('--file', type=str, required=True, help="Path to the input file containing the original text")
    args = parser.parse_args()
    return args.shift, args.file

def remove_nonletters(input_text):
    return re.sub(r'[^A-Za-z]', '', input_text)

def cipher(text, shiftAmount):
    result = []

    for char in text:
        if "a" <= char <= "z":
            shifted = chr((ord(char) - ord("a") + shiftAmount) % 26 + ord("a"))
            result.append(shifted)
        elif "A" <= char <= "Z":
            shifted = chr((ord(char) - ord("A") + shiftAmount) % 26 + ord("A"))
            result.append(shifted)

    grouped = ["".join(result[i:i+5]) for i in range(0, len(result), 5)]
    return " ".join(grouped)

def decipher(cipherText, shiftAmount):
    textNoSpace = cipherText.replace(" ", "")
    result = []

    for char in textNoSpace:
        if "a" <= char <= "z":
            shifted = chr((ord(char) - ord("a") - shiftAmount) % 26 + ord("a"))
            result.append(shifted)
        elif "A" <= char <= "Z":
            shifted = chr((ord(char) - ord("A") - shiftAmount) % 26 + ord("A"))
            result.append(shifted)

    return "".join(result)

if __name__ == '__main__':
    shiftAmount, filePath = get_shift_amount()
    originalText = get_original_text(filePath)
    letterOnlyText = remove_nonletters(originalText)
    cipherText = cipher(letterOnlyText, shiftAmount)
    print("=== Cipher Text ===")
    print(cipherText)
    decipheredText = decipher(cipherText, shiftAmount)
    print("\n=== Deciphered Text ===")
    print(decipheredText)
