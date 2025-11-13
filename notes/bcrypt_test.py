import bcrypt

pswrd = b"enigma" # b - bytes type
hashed = bcrypt.hashpw(pswrd, bcrypt.gensalt())
print(hashed)