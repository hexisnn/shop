import bcrypt

def hash_password(password: str):
    
    bytes = password.encode("utf-8")

    salt = bcrypt.gensalt()

    hash = bcrypt.hashpw(bytes, salt)

    return hash.decode("utf-8")

def equal_passwords(input_password: str, exist_password: str):
    hash_input_password = hash_password(input_password)
    
    if hash_input_password == exist_password:
        return True
    else:
        return False
