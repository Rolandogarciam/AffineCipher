import re
import argparse
from cipher import AffineCipher

char_freq_es_first = 'E'
char_freq_es_second = 'A'
stdin_file = 'stdin.txt'

def read_stdin_file(src):
    txt = None

    with open(src, 'r', encoding='utf-8') as txt_file:
        txt = txt_file.read()

    return re.sub('[^A-Za-zñÑ]+', '', txt.replace("\n", "").upper())

def main():
    parser = argparse.ArgumentParser(prog='NAH', description="A simple Affine Cipher")
    parser.add_argument('-a', dest='decimation')
    parser.add_argument('-b', dest='shift')
    parser.add_argument('--cipher', action='store_true', dest='cipher', required=False)
    parser.add_argument('--decipher', action='store_true', dest='decipher', required=False)

    plaintext = read_stdin_file(stdin_file)
    print('[ >] plaintext: ', plaintext)
    
    args = parser.parse_args()

    affine_cipher = AffineCipher()
    
    if args.cipher:
        cipher_text = affine_cipher.encrypt(plaintext, int(args.decimation), int(args.shift))
        print('[ >] cipher text: ', cipher_text)

    elif args.decipher:
        first, second, third = affine_cipher.frequency_analysis(plaintext)
        decimation = affine_cipher.decimation(char_freq_es_first, char_freq_es_second, first, second)
        print('[ >] decimation value: ', decimation)
        shift = affine_cipher.shift(char_freq_es_second, decimation, second)
        print('[ >] shift value: ', shift)
        first_iteration = affine_cipher.decrypt(plaintext, decimation, shift)
        print('[ >] first iteration: ', first_iteration)

        decimation = affine_cipher.decimation(char_freq_es_second, char_freq_es_first, first, second)
        print('[ >] decimation value: ', decimation)
        shift = affine_cipher.shift(char_freq_es_first, decimation, second)
        print('[ >] shift value: ', shift)
        second_iteration = affine_cipher.decrypt(plaintext, decimation, shift)
        print('[ >] second iteration: ', second_iteration)
        
        decimation = affine_cipher.decimation(char_freq_es_first, char_freq_es_second, first, third)
        print('[ >] decimation value: ', decimation)
        shift = affine_cipher.shift(char_freq_es_second, decimation, third)
        print('[ >] shift value: ', shift)
        third_iteration = affine_cipher.decrypt(plaintext, decimation, shift)
        print('[ >] third iteration: ', third_iteration)

if __name__ == '__main__':
    main()
