class RSA:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.n = p * q
        self.phi = (p-1) * (q-1)
        self.e = self.generate_e(self.phi)
        self.d = self.mod_inverse(self.e, self.phi)

    def generate_e(self, phi):
        e = 65537
        while self.gcd(e, phi) != 1:
            e += 2
        return e

    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def mod_inverse(self, a, m):
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1

    def encrypt(self, msg):
        if msg >= self.n:
            raise ValueError("Message is too long to encrypt with this key")
        return pow(msg, self.e, self.n)

    def decrypt(self, msg):
        return pow(msg, self.d, self.n)