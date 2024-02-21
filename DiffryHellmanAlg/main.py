from DiffieHellman import DiffieHellman
if __name__ == '__main__':
    p = 283
    q = 12
    nA = 31
    nB = 56

    # Создание объектов для пользователей A и B
    user_A = DiffieHellman(p, q, private_key=nA)
    user_B = DiffieHellman(p, q, private_key=nB)

    # Генерация открытых ключей для A и B
    user_A.generate_public_key()
    user_B.generate_public_key()

    # Обмен открытыми ключами и вычисление общего ключа
    user_A.generate_shared_key(user_B.public_key)
    user_B.generate_shared_key(user_A.public_key)

    # Вывод результатов
    print(f"Public key for user A: {user_A.public_key}")
    print(f"Public key for user B: {user_B.public_key}")
    print(f"Shared key for user A: {user_A.shared_key}")
    print(f"Shared key for user B: {user_B.shared_key}")