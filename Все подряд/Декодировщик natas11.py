import base64
import json

def xor_encrypt_bytes(data: bytes) -> bytes:
    key = b'#ffffff'
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

# Пример полного цикла расшифровки:
cookie_base64 = "EGAgHwQ1IxYYMSQYGSZxTUksPFVHYDEQCC0/GBlgaVVIJDURDSQ1VRY="
raw_bytes = base64.b64decode(cookie_base64)
decrypted_json = xor_encrypt_bytes(raw_bytes).decode('utf-8')
print(decrypted_json)
result = json.loads(decrypted_json)

print(result)
