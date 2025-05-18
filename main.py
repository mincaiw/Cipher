import re
import argparse

def get_original_text(filename='input.txt'):
    # try:
    #     with open(filename, 'r', encoding='utf-8') as file:
    #         return file.read()
    # except FileNotFoundError:
    #     print(f"{filename} not found")
    #     return None 
    return 'ab sd'

def get_shift_amount():
    # parser = argparse.ArgumentParser(description="Caesar Cipher Encryption/Decryption Program.")
    # parser.add_argument(
    #     '--shift',
    #     type=int,     
    #     required=True,  
    #     help="The shift amount for the Caesar cipher (an integer)"
    # )

    # parser.add_argument(
    #     '--file',
    #     type=str,       
    #     required=True,  
    #     help="Path to the input file containing the original text"
    # )

    # args = parser.parse_args()

    # return args.shift, args.file
    return 1

def remove_nonletters(input_text):
    return re.sub(r'[^A-Za-z]', '', input_text)

def cipher(text, shift_amount):
    result = []

    for char in text:
        if "a" <= char <= "z":
            shifted = chr((ord(char) - ord("a") + shift_amount) % 26 + ord("a"))
            result.append(shifted)
        elif "A" <= char <= "Z":
            shifted = chr((ord(char) - ord("A") + shift_amount) % 26 + ord("A"))
            result.append(shifted)

    result = ["".join(result[i:i+5]) for i in range(0, len(result), 5)]
    return " ".join(result)

def decipher(text, shift_amount):
    text_nospace = text.replace(" ","")
    result = []

    for char in text_nospace:
        if "a" <= char <= "z":
            shifted = chr((ord(char) - ord("a") - shift_amount) % 26 + ord("a"))
            result.append(shifted)
        elif "A" <= char <= "Z":
            shifted = chr((ord(char) - ord("A") - shift_amount) % 26 + ord("A"))
            result.append(shifted)

    return "".join(result)

if __name__ == '__main__':
    original_text = get_original_text()
    shift_amount = get_shift_amount()
    text_letter_only = remove_nonletters(original_text)
    cipher_text = cipher(text_letter_only, shift_amount)
    print(f'cipher_text={cipher_text}')
    decipher_text = decipher(cipher_text, shift_amount)
    print(f'decipher_text={decipher_text}')