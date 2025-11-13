import bcrypt

pswrd = b"enigmaa" # b - bytes type
hashed = bcrypt.hashpw(pswrd, bcrypt.gensalt())
print(hashed)