from RSAFunctions import RSA


if __name__ == '__main__':
    p = 2003
    q = 1667
    rsa = RSA(p, q)

    message = 1835527
    encrypted_message = rsa.encrypt(message)
    decrypted_message = rsa.decrypt(encrypted_message)

    print(f"Public Key: (e={rsa.e}, n={rsa.n})")
    print(f"Private Key: (d={rsa.d}, n={rsa.n})")
    print(f"Original Message: {message}")
    print(f"Encrypted Message: {encrypted_message}")
    print(f"Decrypted Message: {decrypted_message}")
    print(f"Decryption successful: {decrypted_message == message}")
