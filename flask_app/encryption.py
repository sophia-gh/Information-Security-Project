from Crypto.Random import get_random_bytes 
from Crypto.Cipher import AES
import base64

# randomly generated key
global_key = get_random_bytes(32)

# modified from tutorial to store ciphertext and associated data as a single string
def AES_ENCRYPT(user_data, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(user_data.encode())
    bundle = cipher.nonce + tag + ciphertext
    return base64.b64encode(bundle).decode('utf-8')

# parses single sting input into separted data to compute decryption 
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

# try to generate key, and save key in the table, retrieve key from table when decrypting 