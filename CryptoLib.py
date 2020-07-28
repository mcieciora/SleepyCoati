from cryptography.fernet import Fernet
from logging import debug, info, warning, error


def encrypt_co_file(compile_co_file):
    key = Fernet.generate_key()
    key_object = Fernet(key)
    save_data_to_file(key, 'compile_package/key.key')
    if read_file('compile_package/key.key') != key:
        error('[ERR] Key was not saved to file properly!')
    else:
        info('[INF] Key saved to file successfully!')
    data = read_file(compile_co_file).encode()
    if data != '':
        save_data_to_file(key_object.encrypt(data), 'compile_package/encrypt.data')
    else:
        warning('[WAR] Data is empty. Omitting!')
    if read_file('compile_package/encrypt.data') != data:
        error('[ERR] Encrypted data was not saved to file properly!')
    else:
        info('[INF] Encrypted data saved to file successfully!')


def decrypt_into_co_file(key_file, encrypt_data_file):
    key = read_file(key_file)
    data = read_file(encrypt_data_file)
    key_object = Fernet(key.encode('utf-8'))
    data = key_object.decrypt(data.encode('utf-8'))
    save_data_to_file(data, 'compile_package/compile.co')
    if read_file('compile_package/compile.co') != data:
        error('[ERR] compile co file was not saved to file properly!')
    else:
        info('[INF] compile co file saved to file successfully!')


def save_data_to_file(data, file_name):
    file = open(file_name, 'wb')
    file.write(data)
    file.close()


def read_file(file):
    with open(file, 'r') as f:
        return f.read()
