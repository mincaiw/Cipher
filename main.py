def get_original_text():
    return 'as df'  # 파일로부터 text 받기

def get_shift_amount():
    return 1  # argparse로 shift 받기

def remove_nonletters(input_text):
    return 'asdf'  # 알파벳만 남기기

def cipher(text, shift_amount):
    result = []

    for char in text:
        if "a" <= char <= "z":
            shifted = chr((ord(char) - ord("a") + shift_amount) % 26 + ord("a"))
            result.append(shifted)
        elif "A" <= char <= "Z":
            shifted = chr((ord(char) - ord("A") + shift_amount) % 26 + ord("A"))
            result.append(shifted)

    groups = ["".join(result[i:i+5]) for i in range(0, len(result), 5)]
    return " ".join(groups)

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