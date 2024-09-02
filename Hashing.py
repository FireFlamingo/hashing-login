import hashlib
import random
import string



def generate_salt(length=5):
    chc_total = string.ascii_letters + string.digits + string.punctuation.replace(',','')
    return ''.join(random.choice(chc_total) for _ in range(length))


def mixture(salt_generated,password):
    pass_process = salt_generated + password
    return pass_process


def hashing(salt_generated,pass_input):


    print("This is pass_input : " + pass_input)
    pass_input1= pass_input.encode()
    h=hashlib.sha256()
    h.update(pass_input1)
    h.digest()
    return h.hexdigest()
