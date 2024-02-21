if __name__ == '__main__':

    pA, gA, xA, kA = 127, 7, 63, 25
    pB, gB, xB, kB = 97, 10, 48, 19
    M = 485

    # 1) Calculating the open keys
    openKeyA = pow(gA, xA, pA)
    openKeyB = pow(gB, xB, pB)

    # 2) Calculating the shared secret for A and B
    secretA = pow(gB, xB * kA, pB)
    secretB = pow(gA, xA * kB, pA)

    # 3) Encryption and decryption
    a = pow(gB, kA, pB)
    b = (M * pow(secretB, kA, pA)) % pA

    decryptedM = (b * pow(a, pA - 1 - xA, pA)) % pA

    print("Открытый ключ A:", openKeyA)
    print("Открытый ключ B:", openKeyB)
    print("Общий секрет A:", secretA)
    print("Общий секрет B:", secretB)
    print("Шифротекст, который A отсылает B: {" + str(a) + ", " + str(b) + "}")
    print("Дешифрованный текст, который B получает от A:", decryptedM)