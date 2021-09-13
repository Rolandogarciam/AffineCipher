"""

            __  __ _               _____ _       _               
     /\    / _|/ _(_)             / ____(_)     | |              
    /  \  | |_| |_ _ _ __   ___  | |     _ _ __ | |__   ___ _ __ 
   / /\ \ |  _|  _| | '_ \ / _ \ | |    | | '_ \| '_ \ / _ \ '__|
  / ____ \| | | | | | | | |  __/ | |____| | |_) | | | |  __/ |   
 /_/    \_\_| |_| |_|_| |_|\___|  \_____|_| .__/|_| |_|\___|_|   
                                          | |                    
                                          |_|   
    Author:
        Rolando García Mogollón
    University: El Bosque
 
"""
import sys
import math
import string

class AffineCipher:

    alphabet = list(string.ascii_uppercase)

    def __init__(self):
        self.alphabet.insert(14, 'Ñ')
        print('\t alphabet: ', self.alphabet)

    def encrypt(self, plaintext, a, b):
        cipher_text = []
        
        if not (self.coprime(a, len(self.alphabet))):
            print('invalid value for key a: ', a)
            print('the value <a> must be chosen such that <a>(%s) and <m>(%s) are coprime' % (a, len(self.alphabet)))
            sys.exit(1)

        for m in plaintext:
            c = (a * self.alp_idx(m) + b) % len(self.alphabet)
            cipher_text.append(self.alphabet[c])
        return ''.join(cipher_text)

    def decrypt(self, cipher_text, a, b):
        decipher_text = []
        
        if not (self.coprime(a, len(self.alphabet))):
            print('invalid value for key a: ', a)
            print('the value <a> must be chosen such that <a>(%s) and <m>(%s) are coprime' % (a, len(self.alphabet)))
            return

        for c in cipher_text:
            m = (self.alp_idx(c) - b) * pow(a, -1, len(self.alphabet)) % len(self.alphabet)
            decipher_text.append(self.alphabet[m])
        return ''.join(decipher_text)

    def decimation(self, freq_es_first, freq_es_second, freq_first, freq_second):
        a = (self.alp_idx(freq_second) - self.alp_idx(freq_first)) * pow((self.alp_idx(freq_es_second) - self.alp_idx(freq_es_first)), -1, len(self.alphabet)) % len(self.alphabet)
        return a

    def shift(self, freq_es_second, decimation, freq_second): 
        b = (self.alp_idx(freq_second) - (self.alp_idx(freq_es_second) * decimation)) % len(self.alphabet)
        return b

    def alp_idx(self, char):
        return self.alphabet.index(char)

    def frequency_analysis(self, cipher_text):
        values = {}
        for i in cipher_text:
            if i in values:
                values[i] += 1
            else:
                values[i] = 1
        values_sorted = sorted(values.items(), key= lambda x: x[1], reverse= 1)
        for i in values_sorted[0:3]:
            print('\t char: %s total: %s avg: %0.f%%' % (i[0], i[1], (i[1]/len(cipher_text))*100))
        return list(dict(values_sorted[0:3]).keys())

    def coprime(self, a, n):
        return math.gcd(a, n) == 1
