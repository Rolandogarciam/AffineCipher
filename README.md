# AffineCipher
The affine cipher is a type of substitution cipher, use a shift and decimation key to construct the cipher alphabet.
## Formula

```
  c = (a * m + b) mod n
  m = ((c - b) * inv(a, n)) mod n
```

## Usage

Generate the stdin.txt with the plaintext or ciphertext.

## Encrypt

    python main.py -a 4 -b 8 --cipher

## Decrypt

    python main.py --decipher

