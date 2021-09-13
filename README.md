# AffineCipher
The affine cipher is a type of substitution cipher, use a shift and decimation key to construct the cipher alphabet.
## Formula

```
  c = (a * m + b) mod n
  m = ((c - b) * inv(a, n)) mod n
