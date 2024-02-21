from random import randint
class DiffieHellman:
    def __init__(self, p, q, private_key=None):
        self.p = p
        self.q = q
        self.private_key = private_key
        self.public_key = None
        self.shared_key = None

    def generate_public_key(self):
        g = randint(1, 100)
        self.public_key = pow(g, self.private_key, self.p)

    def generate_shared_key(self, other_public_key):
        self.shared_key = pow(other_public_key, self.private_key, self.p)