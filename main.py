def get_original_text():
    return 'as df'  # 파일로부터 text 받기

def get_shift_amount():
    return 1  # argparse로 shift 받기

def remove_nonletters(input_text):
    return 'asdf'  # 알파벳만 남기기

def cipher(text, shift_amount):
    return 'zxcv'  # shift하고 5글자마다 띄우기

def decipher(text, shift_amount):
    return 'asdf'  # 띄어쓰기 합치고 unshift

if __name__ == '__main__':
    original_text = get_original_text()
    shift_amount = get_shift_amount()
    text_letter_only = remove_nonletters(original_text)
    cipher_text = cipher(text_letter_only, shift_amount)
    print(f'cipher_text={cipher_text}')
    decipher_text = decipher(cipher_text, shift_amount)
    print(f'decipher_text={decipher_text}')