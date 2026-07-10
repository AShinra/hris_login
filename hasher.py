from argon2 import PasswordHasher

ph = PasswordHasher()

password = "password123"

hashed_password = ph.hash(password)

print(hashed_password)