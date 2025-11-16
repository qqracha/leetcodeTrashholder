"""
bcrypt — адаптивная криптографическая хеш-функция формирования ключа, используемая для защищенного хранения паролей.
Пример использования библиотеки.
"""

import bcrypt

pswrd = b"enigmaa" # b - bytes type
hashed = bcrypt.hashpw(pswrd, bcrypt.gensalt())
print(hashed)