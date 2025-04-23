from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
import base64

# to keep key consistent, stopped using random generation and went with one consistent key
global_key = b'\x05\xeat\x07&\t\x87B\xb0\xf6\xf8\xcbT\xf6r\x8f\xf9\xf6$\xf0\x19\x0b\x0c\x03,\x00\x98\xba\xdd\x8bl0' 


def AES_ENCRYPT(user_data, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(user_data.encode())
    print('E: ')
    print(cipher.nonce)
    bundle = cipher.nonce + tag + ciphertext
    return base64.b64encode(bundle).decode('utf-8')

def AES_DECRYPT(encoded_bundle, key):
    try:
        bundle = base64.b64decode(encoded_bundle)
        nonce = bundle[:16]
        tag = bundle[16:32]
        ciphertext = bundle[32:]
        cipher = AES.new(key, AES.MODE_EAX, nonce)
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        return plaintext.decode('utf-8')
    except (ValueError, KeyError) as e:
        return f"[Decryption failed: {str(e)}]"